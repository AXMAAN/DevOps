In this step, we aim to generate random obstacles for our Flappy Bird game. Your job is to write the logic to generate pipes with random heights but with a constant gap between them.

## What will you do?

Write the logic to generate pipes with random heights. The pipe elements are already selected for you in the `pipes` array.

1. The `move` animation moves the pipes from right to left every three seconds. Therefore, we must generate a random pipe height every three seconds. To do this, we will use the `setInterval` function. Inside the `play` function, we will write the `setInterval` to generate a random number every three seconds:

   ```javascript
   setInterval(() => {
     const randomHeight = Math.floor(Math.random() * 50) + 5;
   }, 3000);
   ```

   The above code will generate a random integer between 5 and 50 every three seconds.

2. Using the formula discussed earlier, apply the random height to the pipes.

   ```javascript
   setInterval(() => {
     const randomHeight = Math.floor(Math.random() * 50) + 5;
     pipes[1].style.height = `${randomHeight}%`;
     pipes[0].style.height = `${100 - (randomHeight + GAP)}%`;
     pipes[0].style.top = `${randomHeight + GAP}%`;
   }, 3000);
   ```

Now every three seconds, we get a randomly sized obstacle. Let's move on to the next step and add the gravity.
