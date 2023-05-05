import React from "react";
import Chat from "./Chat";
import Contacts from "./Contacts";

export default function Home() {
  return (
    <div>
      <div className="row">
        <div className="col-3" >
          <Contacts />
        </div>
        <div className="col-9">
          <Chat />
        </div>
      </div>
    </div>
  );
}
