import InputFields from './components/InputFields';
import Menubar from './components/Menubar';
import ViewGrades from './components/ViewGrades';
import ViewProfessor from './components/ViewProfessor';
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Menubar />
      <BrowserRouter>
        <Routes>
          <Route path = '/' element = {<InputFields/>}/>
          <Route path = "/viewGrades/:course/:code" element={<ViewGrades/>}/>
          <Route path = "/viewProfessor/:profName/:subject" element={<ViewProfessor/>}/>
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;