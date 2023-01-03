In this step, we aim to animate the obstacles for our Flappy Bird game. Your job is to write a CSS animation that moves the obstacles from right to left.

## What will you do?

In this step you are tasked to write a CSS animation to move the pipe elements. The pipe elements are `<div>` element with classes of `pipe` and `obstacles`.

1.  We will use the `@keyframe` CSS rule to write our animation. At 0%, i.e., the start of the animation, the position of the pipes will be the extreme right, and at 100%, i.e., at the end of the animation, the position will be at the start of the game container.

    ```css
    @keyframes move {
      0% {
        left: 100%;
      }
      100% {
        left: -50px;
      }
    }
    ```

2.  Now, apply this animation to the `obstacles` class.

    ```css
    .obstacles {
      animation: move var(--speed) linear infinite;
    }
    ```

3.  Finally, let's put the score counter in place. We want to be at the front all of the time. To do so, we'll give it an `absolute` position and a `z-index` of `2` to put it ahead of all the other elements.

    ```css
    .score {
      position: absolute;
      top: 5px;
      left: 5px;
      z-index: 2;
    }
    ```

The pipe elements are now moving. Let's now move to the next step and write the core game logic using JavaScript.
