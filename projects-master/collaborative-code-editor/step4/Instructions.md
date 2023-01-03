Finally, on the frontend part make sure to listen to all the events being sent by the users, send them to the backend, listen to the responses on the frontend and make the state changes accordingly.

For example:
Whenever the backend emits the "when a user joins" event
```js
    socket.on(
        "when a user joins",
        ({ username, socketId }) => {
          if (username !== location.state?.username) {
          //showing notification using react-hot-toast package
            toast.success(`${username} joined the room.`)
            console.log(`${username} joined`)
          }
        }
      )
```
Also, when a user clicks on the leave button, reroute them to the '/' page.

Quick note: Make sure to listen to all the changes inside useEffect!


And you're done!
All the best!
