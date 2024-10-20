import React from 'react';
import { Github } from 'lucide-react';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md text-center">
        <h1 className="text-3xl font-bold mb-4">Welcome to Nexus-P</h1>
        <p className="mb-6">Your project is set up and ready to go!</p>
        <a
          href="https://github.com/your-username/Nexus-P"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center px-4 py-2 bg-gray-800 text-white rounded-md hover:bg-gray-700 transition-colors"
        >
          <Github className="mr-2" size={20} />
          View on GitHub
        </a>
      </div>
    </div>
  );
}

export default App;