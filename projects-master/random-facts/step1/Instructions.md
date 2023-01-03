## Goal of the step

- The main aim of this step is to add a button named `Next Fact Please` for fetching new fact.
- You can also add your social media links.

It is advised that you go though the [HTML & CSS Fundamentals course](https://codedamn.com/learn/html-css) for a comprehensive and detailed understanding of the fundamentals of HTML and CSS for this project.

## Things to do

1. Add the button named `Next Fact Please`
    - Remove everything from `body` tag of `index.html` file.
    - Add buttons as

    ```html
    <div class="buttons">
        <button>Next Fact Please</button>
        <div class="social">
            <a href="Your social media link goes here..." target="_blank">add svg of your social media link</a>
        </div>
    </div>
    ```

    - For adding social media image of your choice, use the link in `resources` below and download it and save it to `assets` folder.

2. Apply CSS to `buttons` div in `style.css` file and make it flexbox. Here is the sample you can use

    ```css
    .buttons {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    ```
    - Make your buttons cool by using some of the styles given in `resources`.

## Resources
- [HTML & CSS Fundamentals course](https://codedamn.com/learn/html-css)
- [Social media icons](https://freeicons.io/search/icons?q=social&iuc=1776348805)
- [Button designs](https://codepen.io/collection/GZnZWD)