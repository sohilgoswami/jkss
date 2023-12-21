import logo from './logo.svg';
import './App.css';
import Menubar from './components/Menubar';
import InputFields from './components/InputFields';
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import ViewGrades from './components/ViewGrades';
import ViewProfessor from './components/ViewProfessor';
function App() {
  return (
    <div className="App">
      <Menubar/>
      <BrowserRouter>
        <Routes>
          <Route path ="/" element={<InputFields/>} />
          <Route path = "/viewGrades/:course/:code" element={<ViewGrades/>}/>
          <Route path = "/viewProfessor/:profName" element={<ViewProfessor/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
