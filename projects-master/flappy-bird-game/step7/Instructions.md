In this step, we aim to add gravity to our Flappy Bird game. Your job is to write the logic to simulate gravity, so the bird falls toward the ground.

## What will you do?

Write the logic to simulate gravity in the game.

1. We will use the `setInterval` function inside the `play` function to increase the bird's position every 100 milliseconds so that it appears to be falling.

   ```javascript
   setInterval(() => {
     BIRD_POS += GRAVITY;
   }, 100);
   ```

2. We know that if the bird falls down completely to the ground, the game overs. To do this, everytime we increase the birds position, we will check if the bird is above the ground.

   ```javascript
   setInterval(() => {
     BIRD_POS += GRAVITY;
     if (BIRD_POS >= 550) gameOver();
   }, 100);
   ```

   The number 550 accounts for the game container's height, i.e., 500px, and the bird size, i.e., 50px. Also, don't worry about the `gameOver()` function; we will implement it later.

3. To position the bird, we have to change the bird's `top` CSS property according to the `BIRD_POS` variable. To do this, we will write another `setInterval` function inside the `play` function. Doing it this way prevents us from race conditions where two `setInterval` functions are trying to modify the bird's `top` property simultaneously.

   ```javascript
   setInterval(() => {
     bird.style.top = `${BIRD_POS}px`;
   }, 100);
   ```

We have now successfully simulated gravity. Let's move on to the next step and make the bird jump up based on the player's input.
