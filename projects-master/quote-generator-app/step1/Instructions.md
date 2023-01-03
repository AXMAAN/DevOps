In this step our goal is to set up the basic boilerplate code in `index.html`.We have already linked the `style.css` and `script.js` files.

Before jumping into the code of the project, make sure that you understand the basic structure of the HTML5 document and what the boilerplate code does:

-   `<!DOCTYPE html>` tag: Tells the browser that we are using HTML5 and not any previous versions of HTML.
-   `<html>` tag: Tells the browser that the content inside the `<html>` tag is, well, HTML!
-   `<head>` tag: Tells the browser that the content inside the `<head>` tag is metadata about the HTML document.
-   `<body>` tag: Tells the browser that the content inside the `<body>` tag is the content to be displayed on the browser page.
-   `<link>` tag: Tells the browser that we want to link an external file with the HTML document, and process it.

It is advised that you go though the [HTML & CSS Fundamentals course](https://codedamn.com/learn/html-css) for a comprehensive and detailed understanding of these tags.

## What will you do?

1. Add a new `<div> </div>` tag inside the `<body>` element. Give the `<div>` element class `container`, this element will act as a container and will have title of our app and also our quote and a button to generate a new quote.

2.Inside container div create a HTML 5 `<header></header>` tag.Within this header tag create a `<h1></h1>`.Within the h1 tag we wiil be adding our title i.e `Quote Generator App`

    ```html
        <div class="container">
            <header>
                <h1>Quote Generator App</h1>
            </header>
        </div>
    ```

    Here the `Header` tag is a HTML5 Tag. The <header> element represents a container for introductory content or a set of navigational links.

3. Now we are done with setting up our title let's create structure for our actual quote part.
Add a new `<div> </div>` tag within our `container` div after the header tag .Give the `<div>` element class `quote-container`. Now within this `quote-container` div add another `<div> </div>` with a class of `quote-box`.

    Note that we will be using Flexbox to lay out and style our app. Thus we have divs within container div where container div will act as Flex Parent and div within it will be treated as Flex child

It is advised that you go though the [HTML & CSS Fundamentals course](https://codedamn.com/learn/html-css) where you can learn Flex thoroughly Hands On!

4. `quote-box` div will contain two elements. First we will have a  `<p></p>` paragraph tag with `id="quote"` which will contain a place holder Quote as of now.

    ```html
         <p id="quote">"When I let go of what I am, I become what I might be."</p>
    ```

        We have hardcoded quote that will be visible on initial page load.Later we will be Dynamically grab this element using id of "quote" and we will replace it's content with Dynamilcally generated Quote from an external API using Javascript!.

    After Quote paragraph Element we will be having a `<small></small>` tag  with id of "author" which will also contain a Placeholder Author as of now.

    If you have never came across `<small></small>` tag then go through this post from [w3Schools](https://www.w3schools.com/tags/tag_small.asp)

        ```html
            <small id="author">- Laozi</small>
        ```

        Again as said Earlier these are just placeholders for initial part to visualize what we are working with it.Later we will make everything Dynamic using few lines of JavaScript that we will be coding in further steps.(Dont Worry as of now😊)

5. Now we just have to implement last piece of our Structure i.e HTML. But before that just make sure your HTML has similar code block as below (If you have followed the Instructions). However you have complete freedom to implement the project in your own way.

        ```html
    <div class="container">
        <header>
            <h1>Quote Generator App</h1>
        </header>
        <!-- Container -->
        <div class="quote-container">
            <div class="quote-box">
                <p id="quote">"When I let go of what I am, I become what I might be."</p>
                <small id="author">- Laozi</small>
            </div>
        </div>
    </div>
        ```
Now that our Structure is almost ready Let's add a `<button></button>` outside the `<div></div>` with class="quote-box" to trigger an event using which we will be making an API call to fetch new Quote from our API.

To this buuton add id of "btn" and add class (actually multiple classes) of "btn-white" and "btn-mid".We will be using these classes to Style our Button in next step.


        ```html
             <button id="btn" class="btn-white btn-mid">Generate</button>
        ```

## At the end of Step 1 HTML Template should be as follows
        ```html
    <div class="container">
        <header>
            <h1>Quote Generator App</h1>
        </header>
        <!-- Container -->
        <div class="quote-container">
            <div class="quote-box">
                <p id="quote">"When I let go of what I am, I become what I might be."</p>
                <small id="author">- Laozi</small>
            </div>
            <button id="btn" class="btn-white btn-mid">Generate</button>
        </div>
    </div>
        ```


## Congrats 🎉

Congratulation on completing first step and implementing the structure of your app.
Now in the upcoming steps let's style the app and make it fully functional using JS
