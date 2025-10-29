from pymongo.database import Database
from app.database import get_database
from sentence_transformers import SentenceTransformer, util
from typing import List, Dict

class ComprehensionService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.comprehension
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.seed_data()

    def seed_data(self):
        if self.collection.count_documents({}) == 0:
            passages = [
                {
                    "passage": "The quick brown fox jumps over the lazy dog.",
                    "questions": [
                        "What color is the fox?",
                        "What does the fox jump over?",
                    ],
                    "answers": ["brown", "the lazy dog"],
                }
            ]
            self.collection.insert_many(passages)

    def get_passage(self) -> Dict[str, any]:
        passage_data = self.collection.find_one()
        passage_data.pop("_id", None)
        return passage_data

    def grade_answer(self, user_answer: str, correct_answer: str) -> float:
        user_embedding = self.model.encode(user_answer, convert_to_tensor=True)
        correct_embedding = self.model.encode(correct_answer, convert_to_tensor=True)
        cosine_score = util.pytorch_cos_sim(user_embedding, correct_embedding).item()
        return cosine_score

    def submit_answers(self, user_answers: List[str]) -> Dict[str, any]:
        passage_data = self.get_passage()
        passage = passage_data["passage"]
        questions = passage_data["questions"]
        correct_answers = passage_data["answers"]

        score = 0
        feedback = []
        for i, user_answer in enumerate(user_answers):
            grade = self.grade_answer(user_answer, correct_answers[i])
            score += grade
            feedback.append(
                {
                    "question": questions[i],
                    "user_answer": user_answer,
                    "is_correct": grade > 0.8, # Consider correct if score is above 0.8
                }
            )
        return {"score": score, "feedback": feedback}
