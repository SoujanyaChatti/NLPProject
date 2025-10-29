from typing import Dict

class ConversationalBotService:
    def __init__(self):
        pass

    def get_response(self, user_input: str) -> Dict[str, str]:
        # Simple rule-based response for demonstration
        if "hello" in user_input.lower():
            return {"response": "Hello! How can I help you today?"}
        elif "bye" in user_input.lower():
            return {"response": "Goodbye! Have a great day!"}
        else:
            return {"response": "I'm sorry, I don't understand. Can you please rephrase?"}
