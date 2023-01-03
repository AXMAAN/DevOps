## Goal of the step

- The main aim of this step is to add a `div` for displaying the fact.
- You can also add some transitions and animations on your `div` or text.

It is advised that you go though the [HTML & CSS Fundamentals course](https://codedamn.com/learn/html-css) for a comprehensive and detailed understanding of the fundamentals of HTML and CSS for this project.

## Things to do

1. Add the box
    - Add a box like this which will show Loading... or add some loading animations at the time of fetching facts.

    ```html
    <div class="fact">
        <p>Loading...</p>
    </div>
    ```

    - You can also add `neomorphism` to your div to look cool, link given in resources.
    - For cool loading animations, see resources.

2. Add font from google font API
   - `import` or `link` font as
    ```css
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap" rel="stylesheet">
    ```

    OR

    ```css
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap');
    </style>
    ```

    and use this font as
    ```css
    p {
        font-family: 'Comfortaa', cursive;
    }
    ```

## Resources
- [HTML & CSS Fundamentals course](https://codedamn.com/learn/html-css)
- [Loading animations](https://codepen.io/AlexWarnes/pen/jXYYKL)
- [Best fonts collections from Google](https://fonts.google.com/)
- [Neomorphism](https://neumorphism.io/#e0e0e0)