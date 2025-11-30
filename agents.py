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
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"[Logic System Error]: {str(e)}"

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
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return "[Style Default]: Warm and mysterious."

class InteractionModule(Module):
    """The Orchestrator: Synthesizes everything."""
    def __init__(self):
        super().__init__()
        self.logic = NarrativeLogicModule()
        self.persona = PersonaEngine()

    def generate_response(self, user_input):
        print(f"\n[System] Orchestrating agents for input: '{user_input}'...")
        
        # 1. Parallel execution (Simulated sequentially here)
        # In a production app, these would run in parallel threads
        logic_context = self.logic.get_context(user_input)
        print(f"[Logic Module] Context Retrieved: {str(logic_context).strip()[:50]}...")
        
        style_guide = self.persona.get_style_guidelines(user_input, "General Chat")
        print(f"[Persona Engine] Style Defined: {str(style_guide).strip()[:50]}...")
        
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
        
        try:
            response = self.model.generate_content(final_prompt)
            return response.text
        except Exception as e:
            return "Zei is currently recharging. Please try again later."
