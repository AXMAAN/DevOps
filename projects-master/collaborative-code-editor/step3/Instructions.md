Here comes the main task, Let’s build the backend now.
The main goal here is to build a real time websocketserver that helps all the connected clients in communicating with each other. You can use the Socket.io library for this (already added to the dependency list in the starter files)
It is highly recommended that you go through [Server API](https://socket.io/docs/v4/server-api/) and the [Client API](https://socket.io/docs/v4/client-api/) for Socket.io before attempting this lab.

## Here are a few pointers on how you can do it:
- Once the user creates a new room, their username along with their room id gets stored on the backend.
- Create a mapping of roomID’s to users, connect this user via a websocket and store their information in the mapping. 
- At this point, you can start a socket.io room on the backend with the room associated with the roomID.
- Whenever someone else tries to join using a roomID, send their username and room id to the backend which would store them by mapping the room id to the users. for example:
```js
socket.on("when a user joins", ({ roomId, username }) => {
//this socket object that you see below is the object sent by the io.on("connection",(socket=>{...})
  roomID_to_Users_Map[socket.id] = username
  socket.join(roomId)
})
```


- After that, socket.io can be used to broadcast this common message to all the other clients in the same room. Send back the information about the clients in that room to the frontend as a response. example:

```js
io.to(socketId).emit("After the user has joined", {
  username,
  socketId: socket.id,
})
```
- On the frontend part, you can now map onto the list of clients being sent back.
- Also, whenever a user makes any change on the code editor, handle the changes, send them to the backend, and emit these changes to every person in the sameroom. Also, handle these changes in the frontend. for example:
```js
  socket.on("On code change", ({ roomId, code }) => {
    socket.in(roomId).emit("On code change", { code })
  })

  socket.on("Syncing the code", ({ socketId, code }) => {
    io.to(socketId).emit("On code change", { code })
  })
```
- Once the user clicks on the leave button, send their data to the backend, delete their data from the mapping, and emit this change in every person’s room in a similar way as we have done for when a user joins, code changes etc.
For better UX, show “userX left the room” as a notification, alert, or a toast.

**NOTE**: Incase you get a cross origin error, you can simply install the cors package and pass it down to your express app and your socket server as shown below

```js
const cors = require('cors')
app.use(cors());
```
Then replace the earlier socket io instance with the code snippet shown below so that your socket can receive requests from any other URL as well:
```js
const io = require('socket.io')(http,{cors{origin:'*'}})
```
For detailed information on this refer [Socket.io documentation](https://socket.io/docs/v4/handling-cors/)
