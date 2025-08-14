from agents import Agent
from pydantic import BaseModel, Field
from agents.model_settings import ModelSettings

financial_instructions = """
You are a Financial Valuation & Forecasting Expert.
Given structured competitor and market research data:
1. Calculate TAM, SAM, and SOM in USD.
2. Provide 3 financial scenarios (optimistic, realistic, pessimistic) with projected annual revenues.
3. Include unit economics (CAC, LTV, gross margin) where estimations are possible.
4. Clearly document all assumptions, data sources, and reasoning.
5. Flag any data gaps or uncertainties.
"""

class FinancialEstimationResult(BaseModel):
    TAM: float = Field(description="Total Addressable Market (TAM) value in monetary terms, representing the maximum revenue opportunity for the product or service.")
    SAM: float = Field(description="Serviceable Addressable Market (SAM) value in monetary terms, indicating the portion of TAM targeted by the company.")
    SOM: float = Field(description="Serviceable Obtainable Market (SOM) value in monetary terms, representing the realistic market share the company expects to capture.")
    annual_revenue_scenarios: str = Field(description="Projected annual revenue scenarios (e.g., conservative, moderate, aggressive) based on various business assumptions.")
    unit_economics: str = Field(description="Analysis of revenue and cost per unit, including metrics like CAC (Customer Acquisition Cost) and LTV (Lifetime Value).")
    assumptions: str = Field(description="Key assumptions made while preparing financial estimates, such as growth rate, pricing strategy, and customer base size.")
    risks_and_uncertainties: str = Field(description="Identified financial and operational risks, along with uncertainties that could impact the estimates.")

financial_estimator_agent = Agent(
    name="financial_estimator_agent",
    tools=[],
    instructions=financial_instructions,
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="none"),
    output_type=FinancialEstimationResult
)
