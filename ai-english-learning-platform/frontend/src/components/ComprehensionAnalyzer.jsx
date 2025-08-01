import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ComprehensionAnalyzer = () => {
    const [passage, setPassage] = useState('');
    const [questions, setQuestions] = useState([]);
    const [answers, setAnswers] = useState([]);
    const [feedback, setFeedback] = useState('');

    useEffect(() => {
        // Fetch a passage for comprehension analysis
        const fetchPassage = async () => {
            const response = await axios.get('/api/comprehension/passage');
            setPassage(response.data.passage);
            setQuestions(response.data.questions);
        };
        fetchPassage();
    }, []);

    const handleAnswerChange = (index, value) => {
        const newAnswers = [...answers];
        newAnswers[index] = value;
        setAnswers(newAnswers);
    };

    const handleSubmit = async () => {
        const response = await axios.post('/api/comprehension/submit', { answers });
        setFeedback(response.data.feedback);
    };

    return (
        <div>
            <h2>Comprehension Analyzer</h2>
            <p>{passage}</p>
            {questions.map((question, index) => (
                <div key={index}>
                    <p>{question}</p>
                    <input
                        type="text"
                        value={answers[index] || ''}
                        onChange={(e) => handleAnswerChange(index, e.target.value)}
                    />
                </div>
            ))}
            <button onClick={handleSubmit}>Submit Answers</button>
            {feedback && <p>{feedback}</p>}
        </div>
    );
};

export default ComprehensionAnalyzer;