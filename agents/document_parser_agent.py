from pathlib import Path

def parse_claim_document(file_path):
    print("[Document Parser Agent] Parsing claim document...")

    text = Path(file_path).read_text()

    parsed_data = {
        "customer_id": "CUST-1001",
        "claim_amount": 8500,
        "incident_type": "Water Damage",
        "raw_text": text
    }

    return parsed_data