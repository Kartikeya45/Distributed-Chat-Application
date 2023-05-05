import React, { useEffect, useState } from "react";
import MessageService from "../services/MessageService";

export default function Contacts({ user }) {
  const [contacts, setContacts] = useState([]);
  useEffect(() => {
    getContacts();
  }, []);

  const contactsList = contacts.map((c, i) => {
    console.log(c);
    return (
      <div key={c.phone} className={i == 0 ? `py-3` : 0}>
        <div className="px-2">{c.name.toUpperCase()}</div>
        <hr />
      </div>
    );
  });
  return (
    <div className="">
      <div className="contact">{contactsList}</div>
    </div>
  );

  async function getContacts() {
    const response = await MessageService.getContacts(user);
    setContacts(response.data);
  }
}
