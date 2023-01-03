In this step, we aim to set up the bird for our Flappy Bird game. Your job is to give appropriate styling to the bird HTML element.

## What will you do?

In this step you are tasked to give some styling to the bird element. The bird element is an `<img>` element with a class of `bird`.

1. Give width to the bird element.

   ```css
   .bird {
     width: 50px;
   }
   ```

2. The bird element should be able to move freely inside the game container. We will set the `position` property to `absolute` to accomplish this.

   ```css
   .bird {
     width: 50px;
     position: absolute;
     top: 50%;
   }
   ```

   The `top: 50%` property positions the bird vertically at the middle of the game container at the start of the game.

3. While playing the game, the players will move the bird vertically. To do this, we will change the `top` property on the bird element. To make the motion look smoother, we will give it a `transition` property.

   ```css
   .bird {
     width: 50px;
     position: absolute;
     top: 50%;
     transition: top 100ms linear;
   }
   ```

The bird element is now set up. Let's now move to the next step and structure the obstacles for the game.
