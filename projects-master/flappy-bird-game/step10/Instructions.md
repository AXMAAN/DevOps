In this step, we aim to implement the logic to calculate the players' scores while playing the game.

## What will you do?

Write the logic to calculate the players' scores while playing the game.

1. Calculating a player's score is pretty straightforward. If the pipes move from right to left without a game over, it means that the player has successfully avoided the obstacle. In this case, it will increase the player's score by 10. Let's update our random obstacles implementation as follows:

   ```javascript
   setInterval(() => {
     const randomHeight = Math.floor(Math.random() * 50) + 5;
     pipes[1].style.height = `${randomHeight}%`;
     pipes[0].style.height = `${100 - (randomHeight + GAP)}%`;
     pipes[0].style.top = `${randomHeight + GAP}%`;
     SCORE += 10;
   }, 3000);
   ```

2. After changing the score, we must update it in the DOM. To do this, we will update our `setInterval` implementation, where we update the bird's position:

   ```javascript
   setInterval(() => {
     bird.style.top = `${BIRD_POS}px`;
     score.innerText = SCORE;
   }, 100);
   ```

Now that we can keep track of the player's score, let's move on to the final step and implement game over.
