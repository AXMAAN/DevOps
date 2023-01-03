This step would enhance the UI and security of your app. These steps are bonus and your app would still work without them, but they are good to implement:

-   On game over, the popup should ask for retry. If yes, users can be taken to a new game page.
-   The board data can be synced with the server. This way, instead of client, server decides who is the winner which is more reliable.
-   Make sure to have validation checks via server (i.e. whose turn it is should also be decided by a server variable, and if some user tries to go forward with a turn, server can kick that user)
-   If a user disconnects in the middle of the game, server should broadcast appropriate message to the other user saying that the user has disconnected.

All the best!
