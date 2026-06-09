import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection("policy_rules")

collection.add(
    documents=[
        "Water damage claims above 5000 require manager approval.",
        "Utility anomalies greater than 40 percent require investigation."
    ],
    ids=["rule1", "rule2"]
)

def retrieve_policy_rules(claim_data):
    print("[Policy Retrieval Agent] Fetching relevant policy rules...")

    results = collection.query(
        query_texts=[claim_data["incident_type"]],
        n_results=2
    )

    return results["documents"]
