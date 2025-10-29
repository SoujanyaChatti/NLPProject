from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.word_of_the_day import WordOfTheDay
from app.models.pronunciation import PronunciationService
from app.models.essay_assistant import EssayAssistant
from app.services.comprehension_service import ComprehensionService
from app.services.conversational_bot_service import ConversationalBotService
import os
import shutil

router = APIRouter()

@router.get("/word-of-the-day")
async def get_word_of_the_day():
    word_of_the_day_service = WordOfTheDay()
    word = word_of_the_day_service.get_word_of_the_day()
    word.pop("_id", None)
    return word

@router.post("/pronunciation")
async def check_pronunciation(text: str, audio: UploadFile = File(...)):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    # Save the audio file
    file_path = f"temp_{audio.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    service = PronunciationService()
    feedback = service.analyze_pronunciation(file_path, text)

    os.remove(file_path)

    return feedback

@router.post("/essay-assistant")
async def assist_essay_writing(topic: str, essay: str):
    if not topic or not essay:
        raise HTTPException(status_code=400, detail="Topic and essay are required")

    assistant = EssayAssistant()
    feedback = assistant.provide_feedback(essay)

    return feedback

@router.get("/comprehension/passage")
async def get_comprehension_passage():
    service = ComprehensionService()
    passage_data = service.get_passage()
    return passage_data

@router.post("/comprehension/submit")
async def submit_comprehension_answers(answers: list[str]):
    if not answers:
        raise HTTPException(status_code=400, detail="No answers provided")

    service = ComprehensionService()
    feedback = service.submit_answers(answers)

    return feedback

@router.post("/bot")
async def bot(message: str):
    if not message:
        raise HTTPException(status_code=400, detail="No message provided")

    service = ConversationalBotService()
    response = service.get_response(message)

    return response
