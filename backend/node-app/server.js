// npm run devStart, to start application

const express = require('express')
const socketio = require("socket.io")
const http = require("http")
const redis = require('redis')
const cors = require('cors')


app = express()
const httpServer = http.createServer(app)
const io = socketio(httpServer, {
  cors : {
    origin : "*",
  }
})



const port = 3000
const serveChat = require('./routes/serveChats')

// code

app.use('/chat', serveChat)

app.listen(port)