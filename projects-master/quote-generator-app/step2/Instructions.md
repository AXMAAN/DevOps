In this step the main goal is to Style our HTML structure for the Quote API project, the structure is a simple nested structure of `<div>` tags and Containers. By the end of this step ypu will have a clear Understanding of why we structured our app using containers so that we can style our app using Flexbox in this step.

    Note that if you check `style.css` file,you can see that the starter file has some pre written CSS Reset.The goal of a reset stylesheet is to reduce browser inconsistencies in things like default line heights, margins and font sizes of headings, and so on.Now the Reset has been applied let's Style this App.

## What will you do?

1. Grab body by using body tag selector. Add `width` & `height` of 100%. Then we will specify font for our app using `font-family ` attribute. We will be Using the following fonts:-

   ```css
    font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
   ```

   Then set Black color `#000000` (HexaDecimal value for Black) as `background-color` for our entire app. Also we will set the color for our text content as `white`

   ```css
   body {
    width: 100%;
    height: 100%;
    line-height: 1.5;
    font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
    background-color: #000000;
    color: white;
    overflow: hidden;
   }
   ```

2. Flexbox layout is the best way to arrange elements in a flexible way. It is a great way to organize your page and make it responsive across all viewports. The breakdown is as follows:

Make the `.container` a flex container.We will be using `flex-direction` of `column` as we want our flex children to appear one below the other . Also we will center our flex items  using `justify-content` and `align-items` properties.We will set the value of both these properties to `center`. We will also provide spacing between flex childern using `gap` property.

  ```css
.container {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
    align-items: center;

}
   ```


3. Now if have gone through the `./design` folder and checkout out the design you can see that our title has a linear gradient effect.We can achieve this using

  ```css
  h1{
    background-image: -webkit-linear-gradient(92deg, #f35626, #feab3a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    }
   ```
Here you use a linear gradient as Background image and clip it to text i.e our title.

    You can also notice that colors in linear gradient is constantly changing. This can be achieved using CSS Animations.Add the below property to add a animation.

    ```css
    h1{
    -webkit-animation: hue 10s infinite linear;
    }
    ```

 Up next we define Keyframes for our Animation using following code block

 ```css
    @-webkit-keyframes hue {
    from {
        -webkit-filter: hue-rotate(0deg);
    }

    to {
        -webkit-filter: hue-rotate(-360deg);
    }
}
 ```

 CSS Animations is a Advanced topic and requires practise to master. However if you are interested in learning about Animations you can go through [Learn Advanced HTML and CSS Concepts](https://codedamn.com/learn/advanced-html-css)




4. We also make our `.quote-container` as flexbox where `.quote-box` div and `button` acts as Flex Children.

```css
.quote-container {
    width: 400px;
    display: flex;
    flex-direction: column;
}
```

Now as of `.quote-box` is considered we will add a unusual border styling i.e linear gradient to it.

```css
    .quote-box {
    border: 5px solid;
    border-image: linear-gradient(45deg, purple, orange) 1;
    padding: 30px 20px;
    margin-bottom: 20px;
}
```

Now we can actually style the actal `#quote` and `#author` as follows

```css
#quote {
    color: whitesmoke;
    text-align: center;
}
```

```css
#author {
    float: right;
    color: gray;
    font-weight: bold;
    font-style: italic;
    margin-top: 10px;
}
```


5. In this last step we will be focusing on styling our `Generate` button and will be giving it a minimal black and white look. For starters we will set `font-size` and `line-height` properties to be 16 and 25px respectively. Then we will add `letter-spacing` of 3px. Finally as this button triggers an event we will give this a property of `cursor: pointer;` by grabbing button using class `.btn-mid` selector.

```css
.btn-mid {
    text-decoration: none;
    padding: 5px;
    cursor: pointer;
    font-size: 16px;
    line-height: 25px;
    text-transform: uppercase;
    letter-spacing: 3px;
    -webkit-transition: all .4s ease-in-out;
    -moz-transition: all .4s ease-in-out;
    -ms-transition: all .4s ease-in-out;
    -o-transition: all .4s ease-in-out;
    transition: all .4s ease-in-out;
}
```
    Note that apart from adding basic style guides to a button we've also added few transition properties in the above code block so that whenever we hover our button we get a smooth ease-in and ease-out effect for a short duration of .4seconds.

Now as a last part of styling our app we will setup hover state for  our button so that we can leverage on and visualize all the transitions we applied in the previous step.

```css
.btn-white {
    border: solid 2px #fff;
    background: transparent;
    color: #fff !important;
}
```

```css
.btn-white:hover {
    border: solid 2px #fff;
    background: #fff;
    color: #1f1f1f !important;
}
```

## Congrats 🎉

Congratulation on completing second step and implementing the styling of your app.
Now in the upcoming final step let's impliment Javascript functionality of our app so that we can actually make this as a fully working app.
