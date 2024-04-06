const express = require("express");
const http = require("http");
const socketIO = require("socket.io");
const app = express();
const server = http.createServer(app);
const io = socketIO(server);

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

io.on("connection", (socket) => {
  console.log("1 user connected");

  socket.on("chat message", (msg) => {
    console.log("msg", msg);
    io.emit("chat message", msg);
  });

  socket.on("disconnect", () => {
    console.log("1 user disconnected");
  });
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
