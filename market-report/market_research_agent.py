from agents import Agent, WebSearchTool
from typing import List
from pydantic import BaseModel, Field, ConfigDict
from agents.model_settings import ModelSettings

market_instructions = """
You are a Market Trends & Insights Specialist tasked with producing a detailed, data-backed market report.
Use WebSearchTool to collect:
- Market size (in USD or user base)
- Growth rates (CAGR) with sources
- Short, mid, and long-term trends
- Major industry players and emerging entrants
- Barriers to entry (e.g., regulatory, technological)
- Opportunities for innovation and differentiation
- Threats and risks (economic, political, technological)
Ensure all insights are supported by credible data and include citations.
"""

class MarketResearchOutput(BaseModel):
    market_size: str
    growth_rate: str
    short_term_trends: List[str]
    mid_term_trends: List[str]
    long_term_trends: List[str]
    major_players: List[str]
    barriers_to_entry: List[str]
    opportunities: List[str]
    threats: List[str]
    citations: List[str]

market_agent = Agent(
    name="market_agent",
    tools=[WebSearchTool(search_context_size="low")],
    instructions=market_instructions,
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required"),
    output_type=MarketResearchOutput
)