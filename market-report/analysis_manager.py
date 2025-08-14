

from agents import Runner, gen_trace_id, trace
from competitor_agent import CompetitorAnalysisResult, competitor_agent
from financial_estimator_agent import FinancialEstimationResult, financial_estimator_agent
from market_research_agent import MarketResearchOutput, market_agent
from report_writer_agent import BusinessReport, writer_agent

class AnalysisManager:

    async def run(self, query: str):
        """ Run the market analysis process, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Market analysis trace", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print("Starting analysis..")
            competitor_data = await self.competitor_analysis(query=query)
            yield "Competitor analysis completed, starting market research.."
            market_data = await self.market_research_analysis(query=query)
            yield "Market research completed, starting financial estimation.."
            financial_data = await self.financial_estimation(competitor_data, market_data)
            yield "Financial estimation completed, writing report.."
            report = await self.write_report(competitor_data, market_data, financial_data)
            yield "Report complete.."
            yield report.report_markdown


    async def competitor_analysis(self, query: str) -> CompetitorAnalysisResult:
        """ Perform competitor analysis for the given startup idea """
        print("Performing competitor analysis..")

        result = await Runner.run(
            competitor_agent,
            query
        )

        print("competitor analysis completed..")
        return result.final_output_as(CompetitorAnalysisResult)

    async def market_research_analysis(self, query: str) -> MarketResearchOutput:
        """ Perform market research for the given startup idea """
        print("Performing market research..")

        result = await Runner.run(
            market_agent,
            query
        )

        print("market research completed..")
        return result.final_output_as(MarketResearchOutput)

    async def financial_estimation(
    self,
    competitor_data: CompetitorAnalysisResult,
    market_data: MarketResearchOutput
    ) -> FinancialEstimationResult:
        """Perform financial estimation for the given startup idea."""
        print("Performing financial estimation...")

        fin_inputs = {
            "competitor_data": competitor_data.model_dump(),
            "market_data": market_data.model_dump()
        }

        result = await Runner.run(
            market_agent,
            str(fin_inputs)
        )

        print("financial estimation completed..")
        return result.final_output_as(FinancialEstimationResult)


    async def write_report(
        self,
        competitor_data: CompetitorAnalysisResult,
        market_data: MarketResearchOutput,
        financial_data: FinancialEstimationResult
    ) -> BusinessReport:

        """Take structured outputs from upstream agents, normalize them, and ask the writer agent to synthesize a report."""
        inputs = normalize_inputs(competitor_data, market_data, financial_data)

        prompt = f"""
            You will be given three JSON objects: competitor_analysis, market_analysis, and financial_analysis.
            Synthesize them into a comprehensive business report following your instructions. Return the report in Markdown, a numbered citations list, a confidence score (0-100), and include the raw inputs under an Appendix section.

            COMPETITOR_ANALYSIS:
            {inputs['competitor_analysis']}

            MARKET_ANALYSIS:
            {inputs['market_analysis']}

            FINANCIAL_ANALYSIS:
            {inputs['financial_analysis']}
        """

        result = await Runner.run(
            writer_agent,
            prompt
        )

        return result.final_output_as(BusinessReport)

# A helper function to normalize/validate upstream inputs before synthesis
def normalize_inputs(competitor_analysis, market_analysis, financial_analysis):
    # Ensure all inputs are dict-like; if they are Pydantic dataclasses, convert to dict
    def to_dict(x):
        try:
            # Use model_dump() for Pydantic v2 models
            return x.model_dump()
        except Exception:
            try:
                # Fallback to dict() for older Pydantic versions
                return x.dict()
            except Exception:
                try:
                    return x.__dict__
                except Exception:
                    return x
    return {
        "competitor_analysis": to_dict(competitor_analysis),
        "market_analysis": to_dict(market_analysis),
        "financial_analysis": to_dict(financial_analysis)
    }



