from gtts import gTTS
import os

class TextToSpeechService:
    def __init__(self, language='en'):
        self.language = language

    def text_to_speech(self, text, filename='output.mp3'):
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save(filename)
        return os.path.abspath(filename)

    def speak(self, text):
        filename = self.text_to_speech(text)
        os.system(f"start {filename}")  # For Windows, use 'open' for macOS and 'xdg-open' for Linux

# Example usage:
# if __name__ == "__main__":
#     tts_service = TextToSpeechService()
#     tts_service.speak("Hello, welcome to the AI-powered English learning platform!")