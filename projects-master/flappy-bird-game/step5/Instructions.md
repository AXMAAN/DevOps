The goal of this step is to understand how our core logic works. All of the game logic will be written in JavaScript. We use global variables to keep track of various game states, such as the bird's position, score, and so on. Some functions will constantly update these variables based on the user input.

## Global variables

There are two main global variables:

1. `BIRD_POS`
2. `SCORE`

These variables represent the game state. The variable `BIRD_POS` is used to keep track of the bird's position. It represents the number of pixels from the top of the game container. On the other hand, the variable `SCORE` is used to contain the score count. The score represents the number of obstacles the player manages to avoid.

There are three more global varialbes:

1. `GRAVITY`
2. `JUMP`
3. `GAP`

These are constant variables that decide the game's behavior. The variable `GRAVITY` represents the speed at which the bird will fall, and `JUMP` represents how long the bird can jump up. The variable `GAP` contains the gap between the two pipes.

## Logic

Apart from the global variables, we have a few functions that constantly generate new obstacles and update the game state as the player continues to play.

There are three main functions:

1. `play`
2. `collided`
3. `gameOver`

The core game logic is included in the `play` function. It adds new obstacles, updates the bird's position based on user input, checks for game-over situations, and so on. The `collided` function is a utility function that will be used to determine if two game objects have collided. To reset the game states and begin a new game, we utilize the `gameOver` method.

Now that we have understood the core components let's move on to the next step and develop the game logic.
