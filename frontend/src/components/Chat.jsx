import React, { useState, useEffect } from "react";
import messages from "../dummy_data/messages.js";
// import messages from "../dummy_data//groupMessages.js";
import MessageService from "../services/messageService.js";

export default function Chat({ user }) {
  // useEffect(() => {
  //   const interval = setInterval(() => {
  //     window.location.reload();
  //   }, 1000);
  //   return () => clearInterval(interval);
  // }, []);
  const user_ = { name: "Kartikeya", id: 112 };
  const isGroup = false;
  const reciever = !isGroup
    ? { name: "Rohit", id: 123 }
    : { name: "myGrp", id: 124 };

  const messageBlobs = messages.map((m, i) => {
    return (
      <div
        key={Math.random()}
        className={`${
          m.sender.toLowerCase() === user_.name.toLowerCase()
            ? "messager"
            : "reciever"
        } mx-3 my-1 `}
      >
        <div key={Math.random()} className={`message rounded py-1 px-2`}>
          {isGroup && m.sender.toLowerCase() !== user_.name.toLowerCase() && (
            <div className="groupMsg-others">{m.sender}</div>
          )}
          {m.body}
        </div>
      </div>
    );
  });
  const [newMessage, setNewMessage] = useState("");
  return (
    <div className="chat ">
      <div className="chat-details ">
        <nav className="navbar navbar-expand-lg bg-body-tertiary">
          <div className="container-fluid">
            <a className="navbar-brand" href="#">
              {reciever.name}
            </a>
          </div>
        </nav>
      </div>
      <div className="input-group mb-3"></div>
      <div className="message-area ">{messageBlobs}</div>
      <div className="px-2 my-3 position-absolute fixed-bottom d-flex">
        <input
          type="text"
          className="form-control"
          placeholder="Send a message..."
          value={newMessage}
          onChange={handleMessageChange}
        />
        <button className="btn border ms-1">
          <img src="send.svg" alt="send" />
        </button>
      </div>
    </div>
  );
  function handleMessageChange(e) {
    setNewMessage(e.target.value);
  }
  function handleMessageSend() {
    const newMessageObject = {
      accessor: user_.name,
      accessed: reciever.name,
      body: newMessage,
    };
    const response = MessageService.postMessage(newMessageObject);
  }
}
