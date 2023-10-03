In this step, we aim to implement collision detection in our Flappy Bird game.

## What will you do?

Implement the `collided` function to detect collisions between the game objects.

1. We will now implement the `collided` function. To detect collision between two elements, we need the DOMRect. A DOMRect object provides information about the size of an element and its position relative to the viewport. To get the DOMRect object, the `Element.getBoundingClientRect()` method is used. We will determine the DOMRect object of the `source` and the `target` elements inside the `collided` function.

   ```javascript
   function collided(source, target) {
     const sourceRect = source.getBoundingClientRect();
     const targetRect = target.getBoundingClientRect();
   }
   ```

   Now that we have the DOMRect object of both the `source` and the `target` elements, we can easily find if they are colliding using following logic:

   ```javascript
   function collided(source, target) {
     var sourceRect = source.getBoundingClientRect();
     var targetRect = target.getBoundingClientRect();

     return (
       sourceRect.right >= targetRect.left &&
       sourceRect.left <= targetRect.right &&
       sourceRect.bottom >= targetRect.top &&
       sourceRect.top <= targetRect.bottom
     );
   }
   ```

2. Since we have implemented collision detection; we can now check for collisions inside our gravity implementation as follows:

   ```javascript
   setInterval(() => {
     BIRD_POS += GRAVITY;

     if (BIRD_POS >= FRAME_SIZE + BIRD_SIZE) gameOver();
     if (BIRD_POS <= 0) BIRD_POS = 0;

     if (collided(bird, pipes[0]) || collided(bird, pipes[1])) gameOver();
   }, 100);
   ```

Now that we can detect collisions, let's move on to the next step and implement the score calculation functionality.
