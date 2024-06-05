import React from 'react';

function Results({ results }) {
  if (!results) return null;

  return (
    <div>
      <h2>Analysis Results in JSON Format:</h2>
      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>
  );
}

export default Results;
