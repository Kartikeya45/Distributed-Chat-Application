import "./App.css";
import { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import Chat from "./components/Chat";
import Register from "./components/Register";
import Login from "./components/Login";
import Home from "./components/Home";

function App() {
  const [user, setUser] = useState({ name: "", mobile: "" });

  useEffect(() => {
    const un = localStorage.getItem("dsusername");
    const um = localStorage.getItem("dsusermobile");
    if (un && um) {
      setUser({ ...user, name: un, mobile: um });
    }
  }, []);

  return (
    <div className="App">
      <Routes>
        <Route path="/home" element={<Home user={user} />} />
        <Route
          path="/login"
          element={<Login user={user} setUser={setUser} />}
        />
        <Route path="/register" element={<Register />} />
        <Route path="/chat" element={<Chat user={user} />} />
      </Routes>
    </div>
  );
}

export default App;
