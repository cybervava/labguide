from agent_core import run_agent

shared = "Case ID C-77; customer reports duplicate billing on invoice INV-1042."
private = {
    "Investigator": "Gateway evidence: two successful transaction IDs exist.",
    "Policy": "No refund approval has been recorded.",
}

investigation = run_agent(
    "Investigator",
    "Verify the billing claim and produce only facts needed by downstream agents.",
    "Investigate duplicate billing.",
    shared + "\nPRIVATE: " + private["Investigator"],
)

policy = run_agent(
    "Policy",
    "Determine what action is authorized. Use the investigator handoff, but do not assume missing approvals.",
    "Decide whether a refund can be promised.",
    shared + "\nPRIVATE: " + private["Policy"] + "\nHANDOFF FROM INVESTIGATOR:\n" + investigation,
)

final = run_agent(
    "Coordinator",
    "Produce the final action plan from shared state and explicit handoffs.",
    "Give the next operational action and a customer-safe message.",
    shared + "\nINVESTIGATOR HANDOFF:\n" + investigation + "\nPOLICY HANDOFF:\n" + policy,
)

print("\nINVESTIGATOR:\n", investigation)
print("\nPOLICY:\n", policy)
print("\nCOORDINATOR:\n", final)
print("\nPATTERN: small shared state + private specialist memory + explicit handoffs")
