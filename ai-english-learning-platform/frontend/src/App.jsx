import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import LearningDashboard from './pages/LearningDashboard';
import WordOfTheDay from './components/WordOfTheDay';
import PronunciationPractice from './components/PronunciationPractice';
import EssayAssistant from './components/EssayAssistant';
import ComprehensionAnalyzer from './components/ComprehensionAnalyzer';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/dashboard" component={LearningDashboard} />
        <Route path="/word-of-the-day" component={WordOfTheDay} />
        <Route path="/pronunciation-practice" component={PronunciationPractice} />
        <Route path="/essay-assistant" component={EssayAssistant} />
        <Route path="/comprehension-analyzer" component={ComprehensionAnalyzer} />
      </Switch>
    </Router>
  );
};

export default App;