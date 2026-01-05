# Legal Contract Analytics Agent (Experimental PoC)

![Title Animation](https://raw.githubusercontent.com/aniket-work/legal-contract-agent-poc/main/images/title-animation.gif)

## Overview
This is an experimental Proof-of-Concept for an autonomous agent designed to process legal contracts, extract critical clauses, and perform risk assessment using structured output (Pydantic). 

> [!IMPORTANT]
> This project is a personal experiment and PoC. It is NOT intended for production legal advice.

## System Architecture

![Architecture](https://raw.githubusercontent.com/aniket-work/legal-contract-agent-poc/main/images/architecture-diagram.png)

## Features
1. **Automated Clause Extraction**: Identifies Termination, Indemnification, and Liability clauses.
2. **Risk Scoring**: Assigns heuristic risk scores to each extracted provision.
3. **Structured Output**: Uses Pydantic models for reliable downstream integration.
4. **Data Visualization**: Includes scripts for analyzing clause distributions and performance trends.

## Statistical Insights

| Chart | Description |
|---|---|
| ![Clause Distribution](https://raw.githubusercontent.com/aniket-work/legal-contract-agent-poc/main/images/clause-distribution.png) | Distribution of common legal provisions. |
| ![Risk Correlation](https://raw.githubusercontent.com/aniket-work/legal-contract-agent-poc/main/images/risk-correlation.png) | Latency vs. Risk Complexity. |
| ![Accuracy Trend](https://raw.githubusercontent.com/aniket-work/legal-contract-agent-poc/main/images/accuracy-trend.png) | F1-score improvement over simulated epochs. |

## Quickstart

```bash
# Clone the repository
git clone https://github.com/aniket-work/legal-contract-agent-poc.git
cd legal-contract-agent-poc

# Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run simulation
python -m src.agent
```

## Disclaimer
The views and opinions expressed here are solely my own and do not represent the views, positions, or opinions of my employer or any organization I am affiliated with. The content is based on my personal experience and experimentation.
