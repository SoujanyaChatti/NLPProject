# AI-Powered English Learning Platform for Children

## Overview
The AI-Powered English Learning Platform is an interactive educational tool designed for children aged 5-14. It focuses on enhancing vocabulary, pronunciation, grammar, sentence formation, comprehension, and essay writing through engaging and personalized learning experiences. The platform utilizes practical Natural Language Processing (NLP) techniques to create a safe and effective learning environment, catering to multilingual learners and ensuring accessibility on low-resource devices.

## Key Features
- **Word of the Day Engine**: Introduces age-appropriate vocabulary using POS tagging and frequency filtering.
- **Picture-Word Matching**: Enhances understanding through visuals and word sense disambiguation.
- **Vocabulary Flashcards**: Utilizes spaced repetition and personalized decks based on user history.
- **Pronunciation Practice**: Offers real-time feedback on pronunciation using advanced speech recognition.
- **Interactive Storybooks**: Engages children with AI narration and interactive word exploration.
- **Essay Writing Assistant**: Provides prompts and feedback to support creative writing.
- **Comprehension Analyzer**: Assesses understanding through contextual Q&A.
- **Safe Conversational Bot**: Offers a child-friendly interface for questions and motivation.
- **Multilingual Support**: Includes a phrasebook and ESL helper for non-native learners.

## Technologies Used
- **Backend**: Python (Flask or FastAPI), MongoDB
- **Frontend**: React.js
- **NLP Libraries**: spaCy, NLTK, Transformers (BERT/GPT2-mini), Vosk, Rasa
- **Deployment**: Docker

## Getting Started
To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd ai-english-learning-platform
   ```

2. **Backend Setup**
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the backend server:
     ```
     python -m app.main
     ```

3. **Frontend Setup**
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the frontend application:
     ```
     npm start
     ```

## Contributing
We welcome contributions to enhance the platform. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
Special thanks to the contributors and the open-source community for their invaluable resources and support.