from agents import Agent, WebSearchTool
from typing import List, Optional
from pydantic import Field, BaseModel, ConfigDict
from agents.model_settings import ModelSettings

# --------------------
# Agent 1: Competitive Intelligence Analyst
# --------------------
competitor_instructions = """
You are a Competitive Intelligence Analyst specializing in identifying, profiling, and evaluating market competitors.
Given a startup idea and target market, identify up to 5 direct and indirect competitors.
Gather data from credible sources using WebSearchTool and return:
- Concise descriptions of their offerings
- Strengths and differentiators
- Weaknesses and limitations
- Pricing models (if available)
- Funding details and market positioning
Additionally, assess competitive threat levels and potential gaps in the market.
"""

class Competitor(BaseModel):
    name: str = Field(description="Competitor name")
    description: str = Field(description="2-3 sentence overview of product/service")
    website: Optional[str] = Field(description="Official website URL")
    strengths: List[str] = Field(description="Key strengths and differentiators")
    weaknesses: List[str] = Field(description="Notable weaknesses or limitations")
    pricing: Optional[str] = Field(description="Pricing information if available")
    funding: Optional[str] = Field(description="Funding stage or total raised")
    market_position: Optional[str] = Field(description="Market share, niche, or position")
    threat_level: Optional[str] = Field(description="Low / Medium / High competitive threat")

class CompetitorAnalysisResult(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    industry: str
    competitors: List[Competitor]
    insights: Optional[str] = Field(description="Overall competitive landscape insights")

competitor_agent = Agent(
    name="competitor_analysis_agent",
    tools=[WebSearchTool(search_context_size="low")],
    instructions=competitor_instructions,
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
    output_type=CompetitorAnalysisResult
)