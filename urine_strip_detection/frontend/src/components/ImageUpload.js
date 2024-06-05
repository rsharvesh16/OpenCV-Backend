// urine-strip-detection-app/frontend/src/components/ImageUpload.js
import React, { useState } from 'react';
import axios from 'axios';

function ImageUpload({ setResults }) {
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image) return;

    const formData = new FormData();
    formData.append('image', image);

    try {
      setLoading(true);
      const response = await axios.post('http://localhost:5000/analyze', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResults(response.data);
    } catch (error) {
      console.error('Error uploading image', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleImageChange} />
        <button type="submit" disabled={!image || loading}>
          {loading ? 'Analyzing...' : 'Upload and Analyze'}
        </button>
      </form>
    </div>
  );
}

export default ImageUpload;
