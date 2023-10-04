This step requires you to build the logic of tic-tac-toe game. Once the game starts, you have to build a 3x3 board on screen where:

-   The computer randomly assigns `X` to one user and `O` to another user.
-   The user can only click on the board when it is their turn
-   The turn starts with `user1` always.
-   Once user1 clicks, a broadcast message is sent to user2 that their turn is enabled. And this happens similarly with user2.
-   On every turn, the frontend JS has to check if there is any row, column or diagonal row that consists of same symbols (either `X` or `O`). If yes, the game is over.
-   Game over message is broadcasted by the winning client to the losing client and a game over message is displayed to both.

This is how the UI can look like:

![](https://raw.githubusercontent.com/codedamn-projects/Tic-Tac-Toe-Multiplayer/master/designs/cover-image.png)
