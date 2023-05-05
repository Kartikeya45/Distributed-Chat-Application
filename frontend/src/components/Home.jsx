import React, { useState } from "react";
import Chat from "./Chat";
import ChatNew from "./ChatNew";
import Contacts from "./Contacts";

export default function Home({ user }) {
  // const user = "1";
  // const selected = { name: "", phone: "" };
  const [selected, setSelected] = useState({ name: "", phone: "" });
  return (
    <div>
      <div className="row">
        <div className="col-3">
          <Contacts user={user} setSelected={setSelected} />
        </div>
        <div className="col-9">
          <ChatNew user={user} selected={selected} />
        </div>
      </div>
    </div>
  );
}
