import React, { useState, useEffect } from "react";

import MessageService from "../services/messageService.js";

export default function ChatNew({ user, selected }) {
  const reciever = selected;

  const [messages, setMessages] = useState([]);
  console.log(selected, "outside");
  useEffect(() => {
    const intervalId = setInterval(() => {
      console.log(user, "inside");
      getMessages();
    }, 500);
    return () => clearInterval(intervalId);
  }, [user]);

  const isGroup = false;

  const messageBlobs =
    messages &&
    messages.map((m, i) => {
      return (
        <div
          key={Math.random()}
          className={`${
            m.sender.toLowerCase() === user.name.toLowerCase()
              ? "messager"
              : "reciever"
          } mx-3 my-1 `}
        >
          <div key={Math.random()} className={`message rounded py-1 px-2`}>
            {isGroup && m.sender.toLowerCase() !== user.name.toLowerCase() && (
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
  async function handleMessageSend() {
    const newMessageObject = {
      accessor: { name: user.name },
      accessed: { name: reciever.name, group: isGroup },
      body: newMessage,
    };
    const response = MessageService.postMessage(newMessageObject);
  }
  async function getMessages() {
    console.log("first", user, selected);
    const data = {
      accessor: { name: user.mobile },
      accessed: { name: reciever.phone, group: isGroup },
    };

    response = await MessageService.getMessages(data);
  }
}
