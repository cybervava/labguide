from concurrent.futures import ThreadPoolExecutor
from agent_core import run_agent

problem = "We want to launch an AI support assistant that can answer billing questions. Identify launch risks and a recommendation."

specialists = [
    ("Security", "Focus only on security, privacy, and access-control risks."),
    ("Operations", "Focus only on support workflow, escalation, monitoring, and failure handling."),
    ("Customer Experience", "Focus only on accuracy, clarity, trust, and customer experience."),
]

def call(spec):
    name, role = spec
    return name, run_agent(name, role, problem)

with ThreadPoolExecutor(max_workers=3) as pool:
    results = dict(pool.map(call, specialists))

for name, result in results.items():
    print(f"\n===== {name.upper()} =====\n{result}")

combined = "\n\n".join(f"{k}:\n{v}" for k, v in results.items())
final = run_agent(
    "Supervisor",
    "Synthesize specialist analyses, resolve conflicts, and make a final recommendation. Do not add unsupported facts.",
    problem,
    memory=combined,
)
print("\n===== SUPERVISOR DECISION =====\n", final)
print("\nFLOW: specialists run in parallel -> supervisor synthesizes")
