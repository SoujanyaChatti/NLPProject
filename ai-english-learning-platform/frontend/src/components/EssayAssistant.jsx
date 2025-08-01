import React, { useState } from 'react';

const EssayAssistant = () => {
    const [topic, setTopic] = useState('');
    const [essay, setEssay] = useState('');
    const [feedback, setFeedback] = useState('');

    const handleTopicChange = (e) => {
        setTopic(e.target.value);
    };

    const handleEssayChange = (e) => {
        setEssay(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        // Call the backend API to get feedback on the essay
        const response = await fetch('/api/essay-assistant', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ topic, essay }),
        });
        const data = await response.json();
        setFeedback(data.feedback);
    };

    return (
        <div className="essay-assistant">
            <h2>Essay Writing Assistant</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="topic">Topic:</label>
                    <input
                        type="text"
                        id="topic"
                        value={topic}
                        onChange={handleTopicChange}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="essay">Your Essay:</label>
                    <textarea
                        id="essay"
                        value={essay}
                        onChange={handleEssayChange}
                        required
                    />
                </div>
                <button type="submit">Get Feedback</button>
            </form>
            {feedback && (
                <div className="feedback">
                    <h3>Feedback:</h3>
                    <p>{feedback}</p>
                </div>
            )}
        </div>
    );
};

export default EssayAssistant;