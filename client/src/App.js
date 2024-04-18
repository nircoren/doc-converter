import './App.css';
import React from 'react';
import Login from './views/Login';
import FileUpload from './components/FileUpload';
import Home from './views/Home';

function App() {
  return (
    <div className="App">
      <Home/>
      {/* <section class="flex justify-center flex-col">
        <Login />
        <FileUpload />
      </section> */}
     
    </div>
  );
}

export default App;


