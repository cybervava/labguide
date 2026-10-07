# Lab Guide: Agent Coordination Lab

Six small Python scripts that teach how multiple AI "agents" can work together
on one problem. Every script uses the same worked example: a customer says
invoice INV-1042 was charged twice, and the team has to decide how to respond.

All agents are the same language model. What makes them different is the
*role* each one is given and the *memory* (context) each one is allowed to see.

## Setup

```bash
cd agent_coordination_lab
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then put your OPENAI_API_KEY in .env
python 01_role_based_agents.py
```

## The lessons

| Script | Pattern | What it shows |
|--------|---------|---------------|
| `01_role_based_agents.py` | Role-based agents | Same model, three role prompts, three specialised answers. |
| `02_sequential_coordination.py` | Sequential pipeline | Investigator -> Policy Reviewer -> Responder. Each step feeds the next. |
| `03_parallel_supervisor.py` | Parallel + supervisor | Three specialists run at once, a supervisor merges their findings. |
| `04_shared_memory.py` | Shared memory | Everyone sees the same case file. Consistent, but context spreads. |
| `05_isolated_memory.py` | Isolated memory | Each agent sees only what it needs. Safer, but facts must be passed by hand. |
| `06_hybrid_memory_coordination.py` | Hybrid | Small shared state, private specialist memory, explicit handoffs. |

`agent_core.py` holds the single helper, `run_agent(name, role, task, memory)`,
that builds the prompt and calls the OpenAI Responses API.
