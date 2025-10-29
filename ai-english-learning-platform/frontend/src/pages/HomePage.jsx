import React from 'react';
import WordOfTheDay from '../components/WordOfTheDay';
import PronunciationPractice from '../components/PronunciationPractice';
import EssayAssistant from '../components/EssayAssistant';
import ComprehensionAnalyzer from '../components/ComprehensionAnalyzer';
import ConversationalBot from '../components/ConversationalBot';

const HomePage = () => {
    return (
        <div className="home-page">
            <h1>Welcome to the AI-Powered English Learning Platform!</h1>
            <WordOfTheDay />
            <PronunciationPractice />
            <EssayAssistant />
            <ComprehensionAnalyzer />
            <ConversationalBot />
        </div>
    );
};

export default HomePage;