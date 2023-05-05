import React, { useState, useEffect } from "react";

import MessageService from "../services/messageService.js";

export default function ChatNew({ user, selected }) {
  const receiver = selected;
  console.log("reciever", receiver);
  const [messages, setMessages] = useState([]);
  useEffect(() => {
    const intervalId = setInterval(() => {
      getMessages();
    }, 100);
    return () => clearInterval(intervalId);
  }, [user, receiver]);

  const isGroup = false;

  const messageBlobs =
    messages &&
    messages.map((m, i) => {
      return (
        <div
          key={Math.random()}
          className={`${
            m.sender.toLowerCase() === user.mobile.toLowerCase()
              ? "messager"
              : "receiver"
          } mx-3 my-1 `}
        >
          <div key={Math.random()} className={`message rounded py-1 px-2`}>
            {isGroup &&
              m.sender.toLowerCase() !== user.mobile.toLowerCase() && (
                <div className="groupMsg-others">{m.sender}</div>
              )}
            {m.body}
          </div>
        </div>
      );
    });
  const [newMessage, setNewMessage] = useState("");
  console.log(selected && selected.phone !== "");
  return (
    <div className="chat ">
      {selected && selected.phone !== "" && (
        <>
          <div className="chat-details ">
            <nav className="navbar navbar-expand-lg bg-body-tertiary">
              <div className="container-fluid">
                <a className="navbar-brand" href="#">
                  {receiver.name}
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
            <button className="btn border ms-1" onClick={handleMessageSend}>
              <img src="send.svg" alt="send" />
            </button>
          </div>
        </>
      )}
    </div>
  );
  function handleMessageChange(e) {
    setNewMessage(e.target.value);
  }
  async function handleMessageSend() {
    const newMessageObject = {
      accessor: { name: user.mobile },
      accessed: { name: receiver.phone },
      body: newMessage,
    };
    console.log(newMessageObject);
    const response = MessageService.postMessage(newMessageObject);
    setNewMessage("");
  }
  async function getMessages() {
    // console.log("first", user, selected);
    const data = {
      accessor: user.mobile,
      accessed: receiver.phone,
      group: isGroup,
    };
    console.log(data);
    const response = await MessageService.getMessages(data);
    console.log(response.data);
    setMessages(response.data);
  }
}
