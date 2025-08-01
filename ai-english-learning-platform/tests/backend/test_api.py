import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the AI-Powered English Learning Platform!"}

def test_word_of_the_day():
    response = client.get("/api/word_of_the_day")
    assert response.status_code == 200
    assert "word" in response.json()
    assert "definition" in response.json()

def test_pronunciation_endpoint():
    response = client.post("/api/pronunciation", json={"word": "example"})
    assert response.status_code == 200
    assert "phonetic" in response.json()

def test_essay_assistant():
    response = client.post("/api/essay_assistant", json={"topic": "My favorite animal"})
    assert response.status_code == 200
    assert "suggestions" in response.json()

def test_comprehension_analysis():
    response = client.post("/api/comprehension", json={"passage": "This is a test passage.", "question": "What is this?"})
    assert response.status_code == 200
    assert "answer" in response.json()