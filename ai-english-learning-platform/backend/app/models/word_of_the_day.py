from datetime import datetime
import random

class WordOfTheDay:
    def __init__(self):
        self.words = self.load_words()
        self.word_of_the_day = self.select_word_of_the_day()

    def load_words(self):
        # This method should load words from a data source (e.g., a database or a file)
        # For demonstration, we will use a static list of words
        return [
            {"word": "abacus", "definition": "A tool used for counting and calculating."},
            {"word": "benevolent", "definition": "Well-meaning and kindly."},
            {"word": "candid", "definition": "Truthful and straightforward."},
            {"word": "diligent", "definition": "Showing care and effort in one's work."},
            {"word": "ebullient", "definition": "Cheerful and full of energy."},
        ]

    def select_word_of_the_day(self):
        # Select a random word from the list
        return random.choice(self.words)

    def get_word_of_the_day(self):
        return {
            "word": self.word_of_the_day["word"],
            "definition": self.word_of_the_day["definition"],
            "date": datetime.now().strftime("%Y-%m-%d")
        }