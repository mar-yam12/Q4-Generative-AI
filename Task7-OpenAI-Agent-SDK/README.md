# 🤖 OpenAI Agents SDK – Intelligent Multi-Agent System

Welcome to the **OpenAI Agents SDK Demo**!  
This project showcases how to build intelligent, collaborative AI agents using the [OpenAI Agents SDK](https://platform.openai.com/docs/agents).  
Part of **Task 7** in the AI & Python course.

---

## 🚀 Overview

The **OpenAI Agents SDK** empowers you to:

- **Create agents** that reason, act, and communicate in natural language.
- **Customize** agent instructions, goals, and personalities.
- **Integrate tools** (APIs, Python functions, web fetchers, etc.).
- **Enable multi-agent collaboration** and seamless handoffs.
- **Monitor & debug** with tracing tools.
- **Enforce guardrails** for safe, valid interactions.

Build advanced assistants, bots, and autonomous workflows with ease!

---

## ✨ Features

| Feature         | Description |
|-----------------|-------------|
| 🧩 **Tools**        | Attach any function (calculator, API, database, etc.) |
| 🧠 **Custom Agents** | Define agent behavior with natural language |
| 🔁 **Handoff**       | Agents can delegate tasks to others |
| 🚦 **Guardrails**    | Validate inputs and outputs |
| 🔍 **Tracing**       | Debug and visualize agent decisions |
| 🧪 **Testing**       | Simulate conversations for testing |

---

## 🌍 Real-World Use Cases

- **E-commerce:** Smart assistant for product Q&A and order placement
- **Education:** AI tutor with math/calculator tools
- **Research:** Agent searching and summarizing articles
- **Productivity:** Multi-agent workflows (travel planning, report generation, etc.)

---

## ⚡ Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/agents-sdk-demo.git
cd agents-sdk-demo
```

### 2. Set Up Environment

```bash
python -m venv env
# Activate:
# On macOS/Linux:
source env/bin/activate
# On Windows:
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install openai-agents
```

### 4. Configure API Key

Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys).

```bash
# On macOS/Linux:
export OPENAI_API_KEY=your-api-key
# On Windows (PowerShell):
$env:OPENAI_API_KEY="your-api-key"
```

---

## 📝 Code Examples

### ✅ Basic Agent

```python
from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant who answers technical questions."
)

response = Runner.run_sync(agent, "What is the difference between a list and a tuple in Python?")
print(response.final_output)
```

---

### 🔧 Agent with Tool

```python
def multiply(a: int, b: int) -> int:
    return a * b

from agents import Tool

tool = Tool.from_function(multiply)

agent = Agent(
    name="MathExpert",
    instructions="You help users by doing math using the multiply tool.",
    tools=[tool]
)

response = Runner.run_sync(agent, "Can you multiply 6 and 9?")
print(response.final_output)
```

---

### 🤝 Multi-Agent Handoff

```python
agent_a = Agent(name="GreetingBot", instructions="Greet the user then handoff.")
agent_b = Agent(name="InfoBot", instructions="Ask the user's favorite programming language.")

response = Runner.run_sync(agent_a, "Hello!", handoff_chain=[agent_b])
print(response.final_output)
```

---

## 📁 Project Structure

```
agents-sdk-demo/
├── main.py         # Main agent logic
├── tools.py        # Custom tools/functions
├── agents.py       # Agent configurations
├── README.md       # Documentation
└── env/            # Virtual environment
```

---

## 📚 Resources

- [Official SDK Docs](https://platform.openai.com/docs/agents)
- [Agents SDK GitHub](https://github.com/openai/openai-python)
- [OpenAI Platform](https://platform.openai.com/)

---

## 👤 Author & Credits

Created by: [mar-yam12](https://github.com/mar-yam12)  
**Task 07 – OpenAI Agents SDK**

---
