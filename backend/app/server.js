// npm run devStart, to start application

const express = require('express')
const app = express()

const port = 3000
const serveChat = require('./routes/serveChats')

// code

app.use('/chat', serveChat)

app.listen(port)