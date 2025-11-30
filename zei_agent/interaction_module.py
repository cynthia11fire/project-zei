# interaction_module.py
class InteractionModule:
    """Handles user intent, routes tasks to internal modules, and manages Zei's outward behavior."""

    def __init__(self, persona_engine, narrative_logic):
        self.persona = persona_engine
        self.narrative = narrative_logic

    def respond(self, user_input: str) -> str:
        """Main entry point: receives user message and generates Zei-style response."""
        intent = self._detect_intent(user_input)
        return self._handle_intent(intent, user_input)

    def _detect_intent(self, text: str) -> str:
        """Simple placeholder — later we can expand this."""
        if "story" in text.lower():
            return "story_mode"
        return "chat"

    def _handle_intent(self, intent: str, text: str) -> str:
        if intent == "story_mode":
            return self.narrative.generate_story(text)
        return self.persona.reply_as_zei(text)
