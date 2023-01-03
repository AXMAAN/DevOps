In this step, we aim to set up the obstacles for our Flappy Bird game. Your job is to give appropriate styling to the obstacle elements.

## What will you do?

In this step you are tasked to give some styling to the pipe elements. The pipe elements are `<div>` element with classes of `pipe` and `obstacles`.

1.  Give width and height to the pipe elements.

    ```css
    .pipe {
      width: 50px;
      height: 40%;
    }
    ```

    Please remember that both pipes will have different heights, and we will resize them with JavaScript using random values. The second pipe element will be styled later in this step.

2.  We want to place the pipes at a certain position relative to our game container. To make positioning it easy, we will set the `position` property to `absolute`.

    ```css
    .pipe {
      width: 50px;
      height: 40%;
      position: absolute;
      top: 0;
      left: 100%;
    }
    ```

    We have placed the pipes to the extreme right of the game container. Please note that you may not see them because they overflow the game container. Also, the first pipe will stick to the top of the game container. We have used the `top: 0` property to accomplish this.

3.  Give the pipes a nice background image. The pipe image `pipe.png` is kept inside the `/assets` folder.

    ```css
    .pipe {
      width: 50px;
      height: 40%;
      position: absolute;
      top: 0;
      left: 100%;
      background-image: url(/assets/pipe.png);
      background-size: cover;
      background-repeat: no-repeat;
    }
    ```

4.  Since the first pipe comes from the top, it is inverted. To achieve this, we will use the `transform` property to rotate the pipe by 180 degrees.

    ```css
    .pipe {
      width: 50px;
      height: 40%;
      position: absolute;
      top: 0;
      left: 100%;
      background-image: url(/assets/pipe.png);
      background-size: cover;
      background-repeat: no-repeat;
      transform: rotate(180deg);
    }
    ```

5.  The second pipe will be straight, so we need to find a way to style the second pipe. We will use the `:nth-child()` selector. It selects the nth child of the same class or tag name. To apply additional styles to the second pipe, we will use the `:nth-child()` selector as follows:

    ```css
    .pipe:nth-child(2) {
      transform: rotate(360deg);
    }
    ```

6.  Finally, give the second pipe a height and position it correctly. To find the height of the second pipe, we will use the following formula:

    ```plaintext
    (Height of 1st pipe) + (Height of 2nd pipe) + (Gap between the two pipes) = 100%
    ```

    We are taking the gap to be 25% of the total game container height for this game. Therefore, according to the formula, the height of the second pipe is 35%.

    Also, the position of the second pipe will be the sum of height of the first pipe and the gap i.e. 65%.

    ```css
    .pipe:nth-child(2) {
      height: 35%;
      top: 65%;
      transform: rotate(360deg);
    }
    ```

The pipe elements are now set up. Let's now move to the next step and animate the obstacles of the game.
