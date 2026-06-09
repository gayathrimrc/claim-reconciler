# Utility Bill & Claim Discrepancy Agent

A multi-agent AI solution built using CrewAI, ChromaDB, and LLM-powered semantic search to analyze utility bill anomalies and insurance claim discrepancies against enterprise policy documents.

## Architecture

The system uses a multi-agent architecture:

1. **Document Parsing Agent**
   - Extracts structured data from unstructured PDF claims or utility bills

2. **Policy Retrieval Agent**
   - Uses vector similarity search to retrieve relevant policy clauses

3. **Reconciliation Agent**
   - Compares extracted claim data against policy rules
   - Detects anomalies and inconsistencies
   - Drafts customer response summaries

## Tech Stack

- CrewAI
- ChromaDB
- OpenAI / Azure OpenAI
- Python
- LangChain
- PyPDF
- Sentence Transformers

## Features

- Multi-agent orchestration
- Semantic policy search
- PDF ingestion pipeline
- Vector embeddings
- AI-powered discrepancy detection
- Enterprise-ready architecture

## Project Structure

```
utility-claim-discrepancy-agent/
├── agents/
├── data/
├── vectordb/
├── services/
├── prompts/
├── main.py
├── requirements.txt
└── README.md
```

## Run the Project

```bash
pip install -r requirements.txt
python main.py
```

## Sample Use Cases

- Insurance claim validation
- Utility billing anomaly detection
- Fraud analysis
- Policy compliance checks

## Future Enhancements

- LangGraph workflow orchestration
- Human-in-the-loop approval
- Power BI dashboard integration
- Snowflake integration
- Real-time event processing