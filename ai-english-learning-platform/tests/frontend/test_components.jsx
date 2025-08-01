import React from 'react';
import { render, screen } from '@testing-library/react';
import WordOfTheDay from '../../src/components/WordOfTheDay';
import PronunciationPractice from '../../src/components/PronunciationPractice';
import EssayAssistant from '../../src/components/EssayAssistant';
import ComprehensionAnalyzer from '../../src/components/ComprehensionAnalyzer';

describe('Frontend Components Tests', () => {
  
  test('renders Word of the Day component', () => {
    render(<WordOfTheDay />);
    const wordElement = screen.getByText(/Word of the Day/i);
    expect(wordElement).toBeInTheDocument();
  });

  test('renders Pronunciation Practice component', () => {
    render(<PronunciationPractice />);
    const pronunciationElement = screen.getByText(/Pronunciation Practice/i);
    expect(pronunciationElement).toBeInTheDocument();
  });

  test('renders Essay Assistant component', () => {
    render(<EssayAssistant />);
    const essayElement = screen.getByText(/Essay Assistant/i);
    expect(essayElement).toBeInTheDocument();
  });

  test('renders Comprehension Analyzer component', () => {
    render(<ComprehensionAnalyzer />);
    const comprehensionElement = screen.getByText(/Comprehension Analyzer/i);
    expect(comprehensionElement).toBeInTheDocument();
  });

});