from pydantic import BaseModel
from typing import List, Optional
from happytransformer import HappyTextToText, TTSettings

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
        self.happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

    def generate_prompt(self, topic: str) -> EssayPrompt:
        # Logic to generate an essay prompt based on the topic
        return EssayPrompt(
            topic=topic,
            guidelines="Write at least 100 words about the topic. Make sure to include an introduction, a body, and a conclusion.",
            example_sentences=[
                "For example, you could start with a sentence like: 'The topic of " + topic + " is very interesting.'",
                "Another example sentence could be: 'In this essay, I will discuss the main points of " + topic + ".'",
            ]
        )

    def provide_feedback(self, essay_text: str) -> EssayFeedback:
        # Logic to analyze the essay and provide feedback
        args = TTSettings(max_length=50)
        suggestions = self.happy_tt.generate_text(essay_text, args=args)
        return EssayFeedback(
            suggestions=[suggestions.text],
            grammar_errors=[],
            style_improvements=[]
        )
