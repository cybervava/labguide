from agent_core import run_agent

shared_memory = """CASE MEMORY
Customer: Acme Corp
Invoice: INV-1042
Observed evidence: payment gateway log contains two successful transaction IDs for the same invoice.
Constraint: No refund approval has yet been recorded.
"""

task = "Assess the duplicate-charge case and state the next safe action."

for name, role in [
    ("Investigator", "Analyze evidence and remaining uncertainty."),
    ("Policy Reviewer", "Assess approval/risk implications."),
    ("Responder", "Explain what can safely be communicated to the customer."),
]:
    print(f"\n===== {name.upper()} / SHARED MEMORY =====")
    print(run_agent(name, role, task, shared_memory))

print("\nTEACHING POINT: every agent sees the same case state; consistency improves, but irrelevant/sensitive context may spread.")
