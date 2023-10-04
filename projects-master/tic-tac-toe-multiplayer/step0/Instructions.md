Hello there, welcome to the first step of building a multiplayer tic-tac-toe app on your own. In this step, your task is to only build the UI. We will build the underlying functionality in later steps.

You can see that the project is broken into two folders: `client` and `server`. The `client` folder starts a React app which serves the UI. The server folder consists of a Node.js project that can be used to build the functionality for websockets.

In this step, we only have to work with `client` folder.

## Landing page design

The landing page will be shown in the `/` route. This page should have the buttons to start and join a game. The maximum number of players is 2. So there can only exist two connections to the web socket (from player1 - server & player2 - server)

![](https://raw.githubusercontent.com/codedamn-projects/Tic-Tac-Toe-Multiplayer/master/designs/Landing%20Page%20%5BDesktop%5D.png)

### Start new game UI

On clicking `Start New` the user is prompted to enter his name. On submitting a random room code is generated. The player-1 has to share the room code with player-2 to join the game.

![](https://raw.githubusercontent.com/codedamn-projects/Tic-Tac-Toe-Multiplayer/master/designs/Player%201%20-%20Details.png)

On clicking on `Let's Go` the user is prompted to copy the room code and share it with player-2

![](https://raw.githubusercontent.com/codedamn-projects/Tic-Tac-Toe-Multiplayer/master/designs/Player%201%20-%20Prompt.png)

### Join game UI

Player 2 is supposed to join the game by clicking on `Join Game` the player-2 is prompted to Enter his name along with the room code

![](https://raw.githubusercontent.com/codedamn-projects/Tic-Tac-Toe-Multiplayer/master/designs/Player%202%20-%20Join%20Prompt.png)
