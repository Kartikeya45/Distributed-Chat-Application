import "./App.css";
import { Routes, Route } from "react-router-dom";
import Chat from "./components/Chat";
import Register from './components/Register'
import Login from "./components/Login";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/chat" element={<Chat />} />
      </Routes>
    </div>
  );
}

export default App;
