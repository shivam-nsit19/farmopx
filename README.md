# farmopx

# 🌱 AutoGen Agriculture Agent System (Template)

This repository is a **template project** demonstrating how to build a **multi-agent system** for agricultural use cases using the [AutoGen framework](https://microsoft.github.io/autogen/) and the **Groq API**.

## 🧠 What It Does

This sample project includes four agents working together in a simple pipeline:

- **🧪 SoilTestingAgent** – Simulates soil analysis
- **🌾 LandOptimizationAgent** – Suggests optimal land usage
- **🗣️ UserProxyAgent** – Interfaces with user requests
- **🔍 CriticAgent** – Evaluates and gives feedback on suggestions

A **GroupChatManager** orchestrates the agents, enabling them to collaboratively solve tasks.

## 🧪 Example Scenario

When a user sends the request:

> "Test the soil sample from 'Field A' and optimize land usage accordingly."

The agents will:
1. Interpret the request
2. Simulate a soil test
3. Optimize land usage
4. Critique and provide feedback

## 🔧 Technologies Used

- [AutoGen](https://github.com/microsoft/autogen) – multi-agent framework by Microsoft
- [Groq API](https://console.groq.com/) – lightning-fast inference for LLMs (e.g. Mixtral)
- Python 3.9+

## 🚧 Future Plans

This is just the beginning. We're building toward a **much more complex multi-agent ecosystem**, which may include:

- Real-time weather + satellite data integration
- Autonomous planning agents
- Ground-level IoT sensor interfaces
- Map-based land simulation
- Web agents for fetching market data or regulations

## 🚀 Getting Started

1. **Install dependencies**
   ```bash
   pip install pyautogen groq
