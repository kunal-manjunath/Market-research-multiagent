# Idea Validator - AI-Powered Market Research & Business Validation Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange.svg)](https://openai.com/)

A sophisticated multi-agent AI system that validates business ideas through comprehensive market research, competitor analysis, and financial estimation. Built with OpenAI's GPT-4o-mini and advanced agent orchestration.

## 🚀 Features

### 🤖 Multi-Agent Architecture
- **Competitor Analysis Agent**: Identifies and profiles up to 5 direct/indirect competitors
- **Market Research Agent**: Analyzes market size, growth trends, and opportunities
- **Financial Estimator Agent**: Provides revenue projections and financial insights
- **Report Writer Agent**: Synthesizes findings into comprehensive business reports

### 🔍 Comprehensive Analysis
- **Competitive Intelligence**: Detailed competitor profiling with strengths, weaknesses, and market positioning
- **Market Validation**: Market size estimation, growth rates, and trend analysis
- **Financial Projections**: Revenue estimates and financial feasibility assessment
- **Risk Assessment**: Barriers to entry, threats, and market challenges identification

### 📊 Rich Outputs
- Structured data models for each analysis type
- Markdown-formatted business reports
- Confidence scoring for all estimates
- Traceable analysis with OpenAI platform integration

## 🛠️ Technology Stack

- **Python 3.8+**
- **OpenAI GPT-4o-mini** for intelligent analysis
- **OpenAI-Agent-SDK** For creating agentic workflows
- **Pydantic** for data validation and serialization
- **Async/await** for concurrent agent execution
- **OPEN AI Web Search Tool** for real-time market data
- **Jupyter Notebooks** for interactive development

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/kunal-manjunath/Market-research-multiagent.git
   cd idea-validator
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env  # Create .env file
   # Add your OpenAI API key to .env
   OPENAI_API_KEY=your_api_key_here
   ```

## 🚀 Quick Start

### Basic Usage

```python
brew install uv
uv run analysis.py
```

### Jupyter Notebook Example

Open `idea.ipynb` to see a complete working example:

```python
# Example from the notebook
message = "AI Journalling app"

with trace("competition_research"):
    competitor_data = await Runner.run(competitor_agent, message)
    print(competitor_data.final_output)
```

## 📋 API Reference

### Analysis Manager

The main orchestrator that coordinates all agents:

```python
class AnalysisManager:
    async def run(self, query: str) -> AsyncGenerator[str, None]
    async def competitor_analysis(self, query: str) -> CompetitorAnalysisResult
    async def market_research_analysis(self, query: str) -> MarketResearchOutput
    async def financial_estimation(self, competitor_data, market_data) -> FinancialEstimationResult
    async def write_report(self, competitor_data, market_data, financial_data) -> BusinessReport
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1  # Optional: for custom endpoints
```

### Model Settings

Customize agent behavior in `market-report/` files:

```python
from agents.model_settings import ModelSettings

ModelSettings(
    tool_choice="required",
    temperature=0.1,
    max_tokens=4000
)
```

## 📁 Project Structure

```
idea-validator/
├── market-report/           # Core analysis modules
│   ├── analysis_manager.py  # Main orchestrator
│   ├── competitor_agent.py  # Competitor analysis agent
│   ├── market_research_agent.py  # Market research agent
│   ├── financial_estimator_agent.py  # Financial analysis agent
│   └── report_writer_agent.py  # Report generation agent
├── idea.ipynb              # Interactive development notebook
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── venv/                   # Virtual environment
```

## 🧪 Testing

Run the analysis with a sample business idea:

```bash
# Activate virtual environment
source venv/bin/activate

# Run the Jupyter notebook
jupyter notebook idea.ipynb
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4o-mini model
- The open-source community for the excellent Python packages used in this project

## Sample Output
<img width="2940" height="8142" alt="journal_app_report" src="https://github.com/user-attachments/assets/9bb368fe-92fd-4cf7-8a35-dc8656070ec1" />

## Agent workflow

<img width="1305" height="543" alt="Screenshot 2025-08-21 at 3 40 48 PM" src="https://github.com/user-attachments/assets/739c9586-f4b3-49f2-9b25-bf0b69fec405" />
