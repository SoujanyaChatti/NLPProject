import React from 'react';
import WordOfTheDay from '../components/WordOfTheDay';
import PronunciationPractice from '../components/PronunciationPractice';
import EssayAssistant from '../components/EssayAssistant';
import ComprehensionAnalyzer from '../components/ComprehensionAnalyzer';

const LearningDashboard = () => {
    return (
        <div className="learning-dashboard">
            <h1>Learning Dashboard</h1>
            <WordOfTheDay />
            <PronunciationPractice />
            <EssayAssistant />
            <ComprehensionAnalyzer />
        </div>
    );
};

export default LearningDashboard;