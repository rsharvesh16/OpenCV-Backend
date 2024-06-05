// urine-strip-detection-app/frontend/src/components/Results.js
import React from 'react';

function Results({ results }) {
  if (!results) return null;

  return (
    <div>
      <h2>Analysis Results</h2>
      <ul>
        {Object.entries(results).map(([key, value]) => (
          <li key={key}>
            <strong>{key}:</strong> {value.join(', ')}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Results;
