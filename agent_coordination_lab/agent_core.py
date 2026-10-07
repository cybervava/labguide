import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
MODEL = os.getenv("OPENAI_MODEL", "gpt-6-luna")

def run_agent(name: str, role: str, task: str, memory: str = "") -> str:
    prompt = f"""You are the {name} agent.
ROLE: {role}
MEMORY AVAILABLE TO YOU:
{memory or '[none]'}
TASK:
{task}
Return a concise, practical answer. Do not pretend to know information outside the supplied task and memory."""
    response = client.responses.create(model=MODEL, input=prompt)
    return response.output_text
