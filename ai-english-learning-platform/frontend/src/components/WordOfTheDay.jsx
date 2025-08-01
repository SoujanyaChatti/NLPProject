import React, { useEffect, useState } from 'react';

const WordOfTheDay = () => {
    const [word, setWord] = useState('');
    const [definition, setDefinition] = useState('');
    const [example, setExample] = useState('');

    useEffect(() => {
        const fetchWordOfTheDay = async () => {
            try {
                const response = await fetch('/api/word-of-the-day');
                const data = await response.json();
                setWord(data.word);
                setDefinition(data.definition);
                setExample(data.example);
            } catch (error) {
                console.error('Error fetching Word of the Day:', error);
            }
        };

        fetchWordOfTheDay();
    }, []);

    return (
        <div className="word-of-the-day">
            <h2>Word of the Day</h2>
            <h3>{word}</h3>
            <p><strong>Definition:</strong> {definition}</p>
            <p><strong>Example:</strong> {example}</p>
        </div>
    );
};

export default WordOfTheDay;