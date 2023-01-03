In this step, the main goal is to build a real-time websocket server that can help both the connected clients communicate with each other. You can use Socket.io library for this.

It is highly recommended that you go through [Server API](https://socket.io/docs/v4/server-api/) and the [Client API](https://socket.io/docs/v4/client-api/) for Socket.io before attempting this lab.

## Important pointers:

-   Once the user creates a new game, they get an invite code to share. You can connect this user1 via a websocket. You can start a socket.io room on backend at this point with the room associated with the roomID (random generated invited code).
-   Once the second user joins this room, socket.io can be used to broadcast a common message to both the clients. Once that common message of "start" game arrives, both the users should be shown a Game screen. Here is where we would build our game board.

For this step, the only important part is to get this linking done right.
