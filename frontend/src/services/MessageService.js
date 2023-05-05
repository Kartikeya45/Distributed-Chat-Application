import axios from "axios";

const http = axios.create({
  baseURL: "http://localhost:8000/",
  headers: {
    "Content-type": "application/json",
  },
});

class MessageService {
  async postMessage(data) {
    try {
      return await http.post("/chat/", data);
    } catch (error) {}
  }

  async postLogin(data) {
    try {
      // console.log(data);
      return await http.post("/login", data);
    } catch (error) {
      console.log(`Error in Message Service/postLogin: ${error}`);
    }
  }

  async getContacts() {
    try {
      // console.log(data);
      const x = {
        data: [
          { name: "rohit", phone: 9932902390 },
          { name: "kartik", phone: 2393290390 },
        ],
      };
      console.log(x);
      return x;
      return await http.post("/chat/contacts", data);
    } catch (error) {
      console.log(`Error in Message Service/getContacts: ${error}`);
    }
  }
}
export default new MessageService();
