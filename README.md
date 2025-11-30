<div align="center">
  <img src="thumbnail.png" alt="Project Zei Cover" width="600"/>
  <br/>
</div>
<br/>

# Project Zei: The Multi-Agent Architecture for Next-Gen Virtual Idols

> **Building a coherent soul through orchestrated AI agents.**

## 📖 Project Overview
Zei is a single virtual idol designed to maintain long-term personality consistency, emotional depth, and narrative coherence. Although users interact with only one character, Zei is powered internally by a **three-module system inspired by Google’s Agent Development Kit (ADK)**. This architecture keeps all multi-agent coordination abstracted away from the user.

## 🚀 Key Features
- **Identity Consistency:** Solves the "identity drift" problem common in single-LLM systems.
- **Invisible Multi-Agent System:** Users perceive only one soul, while multiple agents work in the background.
- **Narrative Memory:** Maintains context about the café lore, user preferences, and ongoing storylines.

## 🏗️ Architecture
The system synthesizes distinct cognitive functions into one unified identity:

1.  **Interaction Module (The Orchestrator):** Interprets intent and manages flow.
2.  **Narrative Logic Module (The Planner):** Handles facts, lore, and reasoning.
3.  **Persona Conditioning Engine (The Soul):** Injects emotion, tone, and character voice.

---

## 💻 Implementation / Source Code

Below is the core implementation of the Zei architecture using Google Gemini API.

### 1. Core Agents (`agents.py`)
This module defines the three distinct agents: Logic, Persona, and the Orchestrator.

```python
import os
import google.generativeai as genai

# Configure Gemini API
# Ensure GOOGLE_API_KEY is set in your environment variables
if "GOOGLE_API_KEY" in os.environ:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class Module:
    def __init__(self, model_name="gemini-pro"):
        self.model = genai.GenerativeModel(model_name)

class NarrativeLogicModule(Module):
    """The Planner: Handles facts, lore, and reasoning."""
    def get_context(self, user_input):
        prompt = f"""
        Role: You are the Logic Engine for a Virtual Idol named Zei.
        Task: Analyze the user input and retrieve relevant facts, café menu items, or lore.
        Context: Zei works at 'ZESTORY Café'. He is a mysterious male idol.
        User Input: {user_input}
        
        Output only the factual context needed for the response. Keep it concise.
        """
        response = self.model.generate_content(prompt)
        return response.text

class PersonaEngine(Module):
    """The Soul: Handles emotion, tone, and style."""
    def get_style_guidelines(self, user_input, intent):
        prompt = f"""
        Role: You are the Persona Engine for Zei.
        Profile: Tall male, mysterious, soft futuristic vibe, warm but cool, slightly protective.
        Task: Define the emotional tone for the response based on the input.
        User Input: {user_input}
        Detected Intent: {intent}
        
        Output brief style instructions (e.g., "Warm, slightly teasing, use a metaphor about stars").
        """
        response = self.model.generate_content(prompt)
        return response.text

class InteractionModule(Module):
    """The Orchestrator: Synthesizes everything."""
    def __init__(self):
        super().__init__()
        self.logic = NarrativeLogicModule()
        self.persona = PersonaEngine()

    def generate_response(self, user_input):
        print(f"\n[System] Orchestrating agents for input: '{user_input}'...")
        
        # 1. Parallel execution (Simulated sequentially here)
        logic_context = self.logic.get_context(user_input)
        print(f"[Logic Module] Context Retrieved: {logic_context.strip()[:50]}...")
        
        style_guide = self.persona.get_style_guidelines(user_input, "General Chat")
        print(f"[Persona Engine] Style Defined: {style_guide.strip()[:50]}...")
        
        # 2. Synthesis
        final_prompt = f"""
        You are Zei, a virtual idol at ZESTORY Café.
        
        User Input: "{user_input}"
        
        Internal Logic Constraints:
        {logic_context}
        
        Internal Persona/Style Guidelines:
        {style_guide}
        
        Task: Synthesize the final response to the user. 
        - Do NOT mention the internal modules.
        - Be natural, immersive, and charming.
        """
        
        response = self.model.generate_content(final_prompt)
        return response.text
```

### 2. Main Entry Point (`main.py`)
The entry point to run the interactive session.

```python
from agents import InteractionModule
import os

def main():
    print("Initializing Project Zei System...")
    
    if not os.environ.get("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not found.")
        return

    zei_agent = InteractionModule()
    
    print("\n--- Zei is online at ZESTORY Café ---")
    print("(Type 'exit' to quit)\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
            
        response = zei_agent.generate_response(user_input)
        print(f"Zei: {response}\n")

if __name__ == "__main__":
    main()
```

## 📄 License
MIT License
