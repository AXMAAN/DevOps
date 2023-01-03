In this step the main goal is to build the HTML structure for the gallery project, the structure is a simple nested structure of `article > img + span` tags. It is okay if you are not able to understand this notation.

Here the `>` means the child of the parent, the `+` means the sibling of the previous element:

-   `article` is the parent
-   `img` & `span` are the siblings

## What will you do?

1. Create the `<article>` tag inside the `div#gallery-container` element:

    ```html
    <article></article>
    ```

2. Add `<image>` and `<span>` tags to `<article>` element:

    ```html
    <article class="img-container">
    	<img class="galley-image" src="" />
    	<span class="title"></span>
    </article>
    ```

    This represents the HTML structure for 1 image. Do this for 11 other images as well.

3. Set the `src` attribute of each individual `<img>`:

    ```html
    <img src="assets/01.jpg" />
    ```

    Make sure to set the `src` attribute refers to all the images in the assets folder.

4. Adding `lorem` text to the span tag. `lorem` refers to random placeholder text. You can add custom text if you want.

    The text we are adding to the span tag represents the title of the image. So we'll restrict the word length to three.

    `Emmet` is available on Codedamn Playgrounds, you can directly write `lorem3` and hit space to generate three words inside the `<span>` tag. Or you can choose to write any three words of your choice for all the span tags.

## For Geeks

It can seem daunting to write the HTML structure for the gallery project, well it is not. You can always make use of `emmet` to create a complex HTML structure with a single line of code.

```
article.img-container*12>img.gallery-image[src=assets/$.jpg]+span.title>lorem3
```

You can use this structure to create the same HTML Structure that we have written manually. You can learn more about `emmet` [here](https://docs.emmet.io/abbreviations/syntax/).
