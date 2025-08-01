from pydantic import BaseModel
from typing import List, Optional

class EssayPrompt(BaseModel):
    topic: str
    guidelines: Optional[str] = None
    example_sentences: Optional[List[str]] = None

class EssayFeedback(BaseModel):
    suggestions: List[str]
    grammar_errors: List[str]
    style_improvements: List[str]

class EssayAssistant:
    def __init__(self):
        pass

    def generate_prompt(self, topic: str) -> EssayPrompt:
        # Logic to generate an essay prompt based on the topic
        return EssayPrompt(topic=topic)

    def provide_feedback(self, essay_text: str) -> EssayFeedback:
        # Logic to analyze the essay and provide feedback
        return EssayFeedback(suggestions=[], grammar_errors=[], style_improvements=[])