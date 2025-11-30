# agent.py
from .interaction_module import InteractionModule
from .persona_engine import PersonaEngine
from .narrative_logic import NarrativeLogic


class ZeiAgent:
    """
    Main orchestrator for Project Zei.
    Connects interaction module, persona engine, and narrative logic.
    """

    def __init__(self):
        self.persona = PersonaEngine()
        self.narrative = NarrativeLogic()
        self.interaction = InteractionModule(
            persona_engine=self.persona,
            narrative_logic=self.narrative,
        )

    def chat(self, user_text: str) -> str:
        """User-facing entry point."""
        return self.interaction.respond(user_text)


# Quick manual test
if __name__ == "__main__":
    agent = ZeiAgent()
    while True:
        text = input("You: ")
        print("Zei:", agent.chat(text))
