import React, { useState } from 'react';

const PronunciationPractice = () => {
    const [inputText, setInputText] = useState('');
    const [feedback, setFeedback] = useState('');

    const handleInputChange = (event) => {
        setInputText(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        // Call the backend API for pronunciation feedback
        const response = await fetch('/api/pronunciation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: inputText }),
        });

        const data = await response.json();
        setFeedback(data.feedback);
    };

    return (
        <div className="pronunciation-practice">
            <h2>Pronunciation Practice</h2>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={inputText}
                    onChange={handleInputChange}
                    placeholder="Type a sentence to practice pronunciation"
                    rows="4"
                    cols="50"
                />
                <button type="submit">Check Pronunciation</button>
            </form>
            {feedback && <div className="feedback">{feedback}</div>}
        </div>
    );
};

export default PronunciationPractice;