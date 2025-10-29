from pymongo.database import Database
from app.database import get_database
import random

class WordOfTheDay:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.words
        self.seed_data()

    def seed_data(self):
        if self.collection.count_documents({}) == 0:
            words = [
                {"word": "abacus", "definition": "A tool used for counting and calculating.", "example": "The child learned to count using an abacus."},
                {"word": "benevolent", "definition": "Well-meaning and kindly.", "example": "The benevolent queen was loved by all her subjects."},
                {"word": "candid", "definition": "Truthful and straightforward.", "example": "She gave a candid interview about her struggles."},
                {"word": "diligent", "definition": "Showing care and effort in one's work.", "example": "The diligent student always completed her homework on time."},
                {"word": "ebullient", "definition": "Cheerful and full of energy.", "example": "He was in an ebullient mood after his team won the championship."},
            ]
            self.collection.insert_many(words)

    def get_word_of_the_day(self):
        words = list(self.collection.find())
        return random.choice(words)
