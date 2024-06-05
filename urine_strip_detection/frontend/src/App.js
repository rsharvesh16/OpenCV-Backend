// urine-strip-detection-app/frontend/src/App.js
import React, { useState } from 'react';
import ImageUpload from './components/ImageUpload';
import Results from './components/Results';
import './App.css';

function App() {
  const [results, setResults] = useState(null);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Urine Strip Detection</h1>
      </header>
      <main>
        <ImageUpload setResults={setResults} />
        <Results results={results} />
      </main>
    </div>
  );
}

export default App;
