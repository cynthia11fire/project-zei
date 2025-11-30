# Project Zei – Multi-Agent Architecture for Next-Gen Virtual Idols

Zei is a single virtual idol powered by a modular multi-agent system.  
Although users interact with only one character, Zei is orchestrated internally by coordinated AI modules, enabling consistent personality, emotional depth, and narrative stability.

This architecture solves common problems found in traditional single-model virtual characters, such as identity drift, tone inconsistency, and unstable narrative flow.

---

## Architecture Overview

### 1. Interaction Module (The Orchestrator)
- Receives user input  
- Detects intent  
- Routes tasks to the correct internal engine  
- Produces Zei’s final output  

### 2. Narrative Logic Module (The Planner)
- World grounding  
- Rules and context  
- Multi-step reasoning  
- Maintains story and lore consistency  

### 3. Persona Conditioning Engine (The Soul)
- Style and tone shaping  
- Emotional expression  
- Maintains Zei’s personality boundaries  

---

## Project Structure

zei_agent/
│
├── agent.py # Main orchestrator
├── interaction_module.py # Intent detection and routing
├── narrative_logic.py # Story and contextual reasoning
└── persona_engine.py # Style and persona shaping

---

## How to Run (Local Test)

Run the agent in interactive mode:

```bash
python -m zei_agent.agent

You will enter an interactive loop where you can chat with Zei:
You: tell me a short story  
Zei: Once upon a time in the Zei universe...

Requirements

The following packages are required:
google-generativeai
python-dotenv

Install with:
pip install -r requirements.txt

License

This project is released under the Apache 2.0 License.

Citation

Tseng, Safi. Project Zei – Multi-Agent Virtual Idol Architecture. Kaggle, 2025.









