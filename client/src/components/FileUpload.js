import React, { useState } from 'react';
import axios from 'axios';
import { useSelector, useDispatch } from 'react-redux';
import { setDocContent } from '../features/doc/docSlice';

function FileUpload({rowIndex, inputIndex}) {
  const dispatch = useDispatch()
  const onFileUpload = event => {
    const doc = event.target.files[0];
    dispatch(setDocContent({ rowIndex, inputIndex, doc}));
  };

function onConvertDoc() {

}

  // const onFileUpload = async () => {
  //   const formData = new FormData();
  //   formData.append("file", file);
  //   try {
  //     const response = await axios.post('http://127.0.0.1:8000/doc/convert', formData, {
  //       headers: {
  //         'Content-Type': 'multipart/form-data'
  //       }
  //     });
  //     console.log('File uploaded successfully', response.data);
  //   } catch (error) {
  //     console.error('Error uploading file:', error);
  //   }
  // };

  return (
    <div>
      <input type="file" onChange={onFileUpload} />
      <button onClick={onConvertDoc}>
        Upload!
      </button>
    </div>
  );
}

export default FileUpload;
