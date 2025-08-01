from pydantic import BaseModel

class PronunciationModel(BaseModel):
    word: str
    phonetic_spelling: str
    audio_url: str
    examples: list[str]

class PronunciationFeedback(BaseModel):
    word: str
    is_correct: bool
    feedback: str
    phonetic_distance: float