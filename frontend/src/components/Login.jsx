import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import MessageService from "../services/MessageService";

export default function Login({ user, setUser }) {
  const navigate = useNavigate();
  const [password, setPassword] = useState("");
  const [mobile, setMobile] = useState("");
  return (
    <div className="container my-5">
      <h1 className="text-center">Login</h1>

      <div className="mb-3">
        <label htmlFor="mobile" className="form-label">
          Mobile Number:
        </label>
        <input
          value={mobile}
          type="text"
          className="form-control"
          id="mobile"
          onChange={(e) => setMobile(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="mobile" className="form-label">
          Password:
        </label>
        <input
          value={password}
          type="password"
          className="form-control"
          id="pass"
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button type="submit" className="btn btn-primary" onClick={handleLogin}>
        Login
      </button>
      <p className="text-center">
        Don't an account? <Link to="/register">Register Here</Link>
      </p>
    </div>
  );
  async function handleLogin() {
    const response = await MessageService.postLogin({
      phone: mobile,
      password: password,
    });
    console.log(response);
    if (!response || response.status != 200) {
      setMobile("");
      setPassword("");
      alert("Invalid cred");
    } else {
      localStorage.setItem("dsusername", response.data);
      localStorage.setItem("dsusermobile", mobile);
      setUser({ ...user, name: response.data, mobile: mobile });
      navigate("/home");
    }
  }
}
