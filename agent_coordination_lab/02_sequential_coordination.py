from agent_core import run_agent

request = "Customer says invoice INV-1042 was charged twice and wants an immediate refund."

investigation = run_agent(
    "Investigator",
    "Extract claims, uncertainties, and verification steps.",
    request,
)
policy = run_agent(
    "Policy Reviewer",
    "Review proposed handling for policy/risk. Do not invent company policy.",
    f"Customer request: {request}\nInvestigator output: {investigation}",
)
response = run_agent(
    "Customer Responder",
    "Create a safe response based on upstream findings; distinguish verified facts from pending checks.",
    f"Customer request: {request}\nInvestigation: {investigation}\nPolicy review: {policy}",
)

print("\n1. INVESTIGATOR ->\n", investigation)
print("\n2. POLICY REVIEWER ->\n", policy)
print("\n3. RESPONDER ->\n", response)
print("\nFLOW: Investigator -> Policy Reviewer -> Responder")
