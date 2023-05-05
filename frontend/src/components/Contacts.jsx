import React, { useEffect, useState } from "react";
import MessageService from "../services/MessageService";

export default function Contacts({ user }) {
  const [contacts, setContacts] = useState([]);
  useEffect(() => {
    getContacts();
  }, [user]);

  const contactsList =
    contacts &&
    contacts.map((c, i) => {
      return (
        <div key={Math.random()} className={i == 0 ? `py-3` : 0}>
          <div className="px-2">{c.name}</div>
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
    if (user.name !== "") {
      const response = await MessageService.getContacts({ user: user.mobile });
      // console.log(response);
      setContacts(response.data);
    }
  }
}
