import pytest
from fastapi.testclient import TestClient
from app.main import app
import mongomock
from app.database import get_database
import os

@pytest.fixture
def mock_db(monkeypatch):
    client = mongomock.MongoClient()
    db = client['ai-english-learning-platform']

    def mock_get_database():
        return db

    monkeypatch.setattr("app.database.get_database", mock_get_database)
    monkeypatch.setattr("app.models.word_of_the_day.get_database", mock_get_database)
    monkeypatch.setattr("app.services.comprehension_service.get_database", mock_get_database)
    return db

@pytest.fixture
def client(mock_db):
    return TestClient(app)

def test_get_word_of_the_day(client):
    response = client.get("/api/word-of-the-day")
    assert response.status_code == 200
    data = response.json()
    assert "word" in data
    assert "definition" in data
    assert "example" in data

def test_check_pronunciation(client):
    with open("ai-english-learning-platform/tests/backend/test.wav", "rb") as f:
        response = client.post(
            "/api/pronunciation",
            params={"text": "hello"},
            files={"audio": ("test.wav", f, "audio/wav")}
        )
    assert response.status_code == 200
    data = response.json()
    assert "word" in data
    assert "is_correct" in data
    assert "feedback" in data
    assert "phonetic_distance" in data

def test_essay_assistant(client):
    response = client.post("/api/essay-assistant", params={"topic": "A memorable journey", "essay": "This is an essay about a memorable journey."})
    assert response.status_code == 200
    data = response.json()
    assert "suggestions" in data
    assert "grammar_errors" in data
    assert "style_improvements" in data

def test_get_comprehension_passage(client):
    response = client.get("/api/comprehension/passage")
    assert response.status_code == 200
    data = response.json()
    assert "passage" in data
    assert "questions" in data

def test_submit_comprehension_answers(client):
    response = client.post("/api/comprehension/submit", json=["brown", "the lazy dog"])
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "feedback" in data

def test_bot(client):
    response = client.post("/api/bot", params={"message": "hello"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
