from agent_core import run_agent

problem = "A SaaS customer reports that invoice INV-1042 was charged twice. Decide how support should respond."

roles = {
    "Investigator": "Identify facts that must be verified before action.",
    "Policy": "Identify policy, risk, and approval considerations.",
    "Responder": "Draft a customer-facing response using only established facts."
}

outputs = {}
for name, role in roles.items():
    outputs[name] = run_agent(name, role, problem)
    print(f"\n===== {name.upper()} =====\n{outputs[name]}")

print("\nTEACHING POINT: Same model + different role instructions => specialized agent behavior.")
