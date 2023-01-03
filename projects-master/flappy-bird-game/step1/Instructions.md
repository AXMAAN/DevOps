In this step, our goal is to set up the scene (or container) for our Flappy Bird game. The basic boilerplate HTML is already setup for you. Your job is to give appropriate styling to the HTML elements.

## What will you do?

In this step you are tasked to give some styling to the `game` container. The game container is a `<main>` element with a class of `game`.

1. Add some styling to the document. Set `margin` and `padding` to `0`, and `box-sizing` to `border-box`, for all the elements of the HTML Document.

   ```css
   * {
     margin: 0;
     padding: 0;
     box-sizing: border-box;
   }
   ```

2. Make all the elements, such as the `<header>` and the `<main>`, move to the center of the screen. Also, add a nice font.

   ```css
   body {
     display: flex;
     flex-direction: column;
     justify-content: center;
     align-items: center;
     font-family: 'Courier New', Courier, monospace;
   }
   ```

3. Now we will style the game container. Since the game elements inside the container should move freely, we'll set the position of the container as `relative` and set some `height` and `width`.

   ```css
   .game {
     position: relative;
     width: 300px;
     height: 500px;
   }
   ```

4. We'll give the game container a nice background to make the game more engaging for the players. You can find the background image `bg.png` inside the `/assets` folder.

   ```css
   .game {
     position: relative;
     width: 300px;
     height: 500px;
     background-image: url(/assets/bg.png);
     background-size: cover;
     background-repeat: no-repeat;
   }
   ```

   The `background-size: cover` property ensures that the background image covers the entire container. And the `background-repeat: no-repeat` ensures that the background image does not repeat.

5. Finally, give a nice border to the game container and set the `overflow` property to `hidden` so that elements moving outside the game container are hidden from the players.

   ```css
   .game {
     position: relative;
     width: 300px;
     height: 500px;
     background-image: url(/assets/bg.png);
     background-size: cover;
     background-repeat: no-repeat;
     border: 5px solid black;
     border-radius: 5px;
     overflow: hidden;
   }
   ```

The game container is now set up. Let's now move to the next step and structure the bird element for the game.
