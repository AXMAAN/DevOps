In this step, we aim to move the bird in our Flappy Bird game. Your job is to write the logic to move the bird based on the player's input.

## What will you do?

Write the logic to move the bird based on the player's input.

1. Inside the `play` function, we listen for the `keyup` event. If the spacebar was pressed, we would decrease the bird's position by the value specified by the `JUMP` variable.

   ```javascript
   window.addEventListener('keyup', function (e) {
     if (e.code !== 'Space') return;
     BIRD_POS -= JUMP;
   });
   ```

2. If the player presses the spacebar continuously, the bird will move out of the game container. Therefore, we reposition the bird to the top every time it tries to go beyond the frame. We will update our gravity implemetation a little bit.

   ```javascript
   setInterval(() => {
     BIRD_POS += GRAVITY;

     if (BIRD_POS >= FRAME_SIZE + BIRD_SIZE) gameOver();
     if (BIRD_POS <= 0) BIRD_POS = 0;
   }, 100);
   ```

Now that we can move the bird, let's move on to the next step and implement collision detection.
