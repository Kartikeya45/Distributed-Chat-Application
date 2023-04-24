import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Register() {
    const [name, setName] = useState("");
    const [password, setPassword] = useState("")
    const [mobile, setMobile] = useState()
  return (
    <div className="container my-5">
      <h1 className="text-center">Register</h1>
      <div className="mb-3">
        <label htmlFor="name" className="form-label">
          Name:
        </label>
        <input
          value={name}
          type="text"
          className="form-control"
          id="name"
          onChange={(e) => setName(e.target.value)}
        />
      </div>
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
      <button
        type="submit"
        className="btn btn-primary"
        onClick={handleRegister}
      >
        Register
      </button>
      <p className="text-center">
        Already have an account? <Link to="/login">Login Here</Link>
      </p>
    </div>
  );
  async function handleRegister() {}
}
