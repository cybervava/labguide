from agent_core import run_agent

task = "Assess the duplicate-charge case and state the next safe action."

memories = {
    "Investigator": "Invoice INV-1042 has two successful payment transaction IDs in gateway logs.",
    "Policy Reviewer": "Refunds require an approval decision; no approval decision is present in your context.",
    "Responder": "Customer reported a duplicate charge. You may acknowledge investigation, but do not promise a refund without confirmed approval.",
}
roles = {
    "Investigator": "Analyze technical/payment evidence.",
    "Policy Reviewer": "Assess policy and authorization only.",
    "Responder": "Create customer-safe communication only.",
}

for name in memories:
    print(f"\n===== {name.upper()} / ISOLATED MEMORY =====")
    print(run_agent(name, roles[name], task, memories[name]))

print("\nTEACHING POINT: least-privilege context reduces leakage/noise, but orchestration must explicitly pass required facts between agents.")
