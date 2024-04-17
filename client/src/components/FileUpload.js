import React, { useState } from 'react';
import axios from 'axios';

function FileUpload() {
  const [file, setFile] = useState(null);

  const onFileChange = event => {
    setFile(event.target.files[0]);
  };

  const onFileUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    try {
      const response = await axios.post('http://127.0.0.1:8000/doc/convert', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('File uploaded successfully', response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={onFileChange} />
      <button onClick={onFileUpload}>
        Upload!
      </button>
    </div>
  );
}

export default FileUpload;
