from agents.document_parser_agent import parse_claim_document
from agents.policy_retrieval_agent import retrieve_policy_rules
from agents.reconciliation_agent import reconcile_claim

def main():
    print("Starting Utility Bill & Claim Discrepancy Agent...")

    claim_data = parse_claim_document("data/sample_claim.txt")

    policy_rules = retrieve_policy_rules(claim_data)

    final_response = reconcile_claim(claim_data, policy_rules)

    print("\n=== FINAL RESPONSE ===")
    print(final_response)

if __name__ == "__main__":
    main()