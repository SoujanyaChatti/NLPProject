from pydantic import BaseModel
from vosk import Model, KaldiRecognizer
import wave
import json
import os

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

class PronunciationService:
    def __init__(self):
        self.model = Model(model_name="vosk-model-small-en-us-0.15")

    def analyze_pronunciation(self, audio_file_path: str, expected_text: str):
        wf = wave.open(audio_file_path, "rb")
        rec = KaldiRecognizer(self.model, wf.getframerate())

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                recognized_text = result.get('text', '')

                # Simple comparison for demonstration
                is_correct = expected_text.lower() in recognized_text.lower()
                feedback = "Good job!" if is_correct else "Keep practicing."

                return PronunciationFeedback(
                    word=expected_text,
                    is_correct=is_correct,
                    feedback=feedback,
                    phonetic_distance=0.0  # Placeholder
                )

        return PronunciationFeedback(
            word=expected_text,
            is_correct=False,
            feedback="Could not recognize speech.",
            phonetic_distance=0.0
        )
