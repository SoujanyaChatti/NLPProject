import React from 'react';
import { render, screen } from '@testing-library/react';
import HomePage from './pages/HomePage';
import LearningDashboard from './pages/LearningDashboard';

describe('Frontend Pages Tests', () => {
    test('renders HomePage correctly', () => {
        render(<HomePage />);
        const headingElement = screen.getByText(/Welcome to the AI-Powered English Learning Platform!/i);
        expect(headingElement).toBeInTheDocument();
    });

    xtest('renders LearningDashboard correctly', () => {
        render(<LearningDashboard />);
        const dashboardElement = screen.getByText(/Your Learning Dashboard/i);
        expect(dashboardElement).toBeInTheDocument();
    });
});
