import axios from "axios";

const http = axios.create({
  baseURL: "http://localhost:5000/api/v1/messaging/",
  headers: {
    "Content-type": "application/json",
  },
});

class MessageService {
  async postMessage(data) {
    try {
      return await http.post('/msg', data)
    } catch (error) {
      
    }
  }
}
export default new MessageService();
