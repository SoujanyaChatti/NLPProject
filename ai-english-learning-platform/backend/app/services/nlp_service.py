from typing import List, Dict, Any
import spacy
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer

class NLPService:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_keywords(self, text: str) -> List[str]:
        doc = self.nlp(text)
        keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
        return keywords

    def get_word_synonyms(self, word: str) -> List[str]:
        synonyms = set()
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        return list(synonyms)

    def generate_tfidf_matrix(self, documents: List[str]) -> Any:
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)
        return tfidf_matrix

    def get_word_of_the_day(self, words: List[str]) -> str:
        # Placeholder for logic to select a word of the day
        return words[0] if words else ""

    def analyze_sentence_structure(self, sentence: str) -> Dict[str, Any]:
        doc = self.nlp(sentence)
        return {
            "tokens": [token.text for token in doc],
            "pos_tags": [token.pos_ for token in doc],
            "dependencies": [(token.text, token.dep_, token.head.text) for token in doc]
        }