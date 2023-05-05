import React from "react";
import Chat from "./Chat";
import ChatNew from "./ChatNew";
import Contacts from "./Contacts";

export default function Home({ user }) {
  // const user = "1";
  const selected = { name: "second", phone: "2" };
  console.log(user, "home")
  return (
    <div>
      <div className="row">
        <div className="col-3">
          <Contacts user={user} />
        </div>
        <div className="col-9">
          <ChatNew user={user} selected={selected} />
        </div>
      </div>
    </div>
  );
}
