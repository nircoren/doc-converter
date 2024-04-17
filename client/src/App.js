import './App.css';
import React from 'react';
import Login from './views/Login';
import FileUpload from './components/FileUpload';

function App() {
  return (
    <div className="App">
      <section class="flex justify-center flex-col">
        <Login />
        <FileUpload />
      </section>
     
    </div>
  );
}

export default App;


