import { useState } from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import MainPage from './components/MainPage/MainPage';
import CreateBlog from './components/CreateBlog/CreateBlog';
import EditBlog from './components/EditBlog/EditBlog';
import Card from './components/Card/Card';
import Login from './components/Login/Login';
import UserRegister from './components/Registro/Registro';
function App() {

  return (
    

      <BrowserRouter>
        <Routes>
          <Route path='/' element= {<Login />} />
          <Route path = '/UserRegister' element={<UserRegister/>} />
          <Route path="/MainPage" element={<MainPage />} />
          <Route path="/CreateBlog" element = {<CreateBlog />} />
          <Route path="/EditBlog" element = {<EditBlog />} />
          <Route path='/Card' element= {<Card />} />
        </Routes>
      
      </BrowserRouter>

    
  )
}

export default App
