from typing import List, Dict
from transformers import pipeline

class ComprehensionService:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering")

    def analyze_comprehension(self, passage: str, questions: List[str]) -> Dict[str, str]:
        answers = {}
        for question in questions:
            result = self.qa_pipeline(question=question, context=passage)
            answers[question] = result['answer']
        return answers

    def grade_answer(self, user_answer: str, correct_answer: str) -> float:
        # Simple grading based on exact match
        if user_answer.strip().lower() == correct_answer.strip().lower():
            return 1.0  # Full score
        else:
            return 0.0  # No score

    def highlight_keywords(self, passage: str, keywords: List[str]) -> str:
        for keyword in keywords:
            passage = passage.replace(keyword, f"**{keyword}**")  # Highlighting keywords
        return passage