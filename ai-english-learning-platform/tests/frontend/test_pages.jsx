import React from 'react';
import { render, screen } from '@testing-library/react';
import HomePage from '../../src/pages/HomePage';
import LearningDashboard from '../../src/pages/LearningDashboard';

describe('Frontend Pages Tests', () => {
    test('renders HomePage correctly', () => {
        render(<HomePage />);
        const headingElement = screen.getByText(/Welcome to the AI-Powered English Learning Platform/i);
        expect(headingElement).toBeInTheDocument();
    });

    test('renders LearningDashboard correctly', () => {
        render(<LearningDashboard />);
        const dashboardElement = screen.getByText(/Your Learning Dashboard/i);
        expect(dashboardElement).toBeInTheDocument();
    });
});