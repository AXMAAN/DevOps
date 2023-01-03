## Adding styles

Now we add some `CSS` to our `style.css` to make our site look nicer to work with it.

- Add the below css to `body` to make it take the entire screen. We are using flexbox so that theme changing button can be positioned to the right without using `position`

  ```css
  display: flex;
  flex-direction: column;
  width: 100%;
  ```

- Add the `theme` class to the button in html. Now in css give it some padding , background , font-size & a pointer cursor. Remove the ugly border & align it to the right side of the screen (actually it will be the extreme right of the parent container & here the parent container i.e body is full screen wide, so the button will be shown at the right side of screen).

  ```css
  .theme {
    align-self: flex-end;
    padding: 0.25em;
    /* whitespace around the emoji 
    will make it look nicer*/
    background: #22272e;
    border: none;
    cursor: pointer;
    font-size: 18px;
  }
  ```

- Now we stylize the `main`. We want the page to not scroll but only the text editor & preview to be scrollable. Since this main is the parent to the `textarea` & `article` so hiding the overflow for main makes the page unscrollable. It will have flex display to show the editor & preview side by side. Give some gap to it as well. Height will be fixed but less than 100vh( full height of viewport/screen) because we want the everything to fit in the screen without scrolling.

  ```css
  main {
    overflow: hidden;
    display: flex;
    height: 90vh;
    gap: 20px;
  }
  ```

- I have already added some base styles for textarea & article in boilerplate so that they are scrollable. Now write some more css specific for textarea. So remove the border & outline. Later on we will add dark & light theme so we want the textarea to change the text & background color accordingly. That is why give `inherit` to both of them so that textarea can inherit the computed value of the property from its parent element.

  ```css
  textarea {
    border: none;
    outline: none;
    background: inherit;
    color: inherit;
  }
  ```

Now lets add some specific styles for our markdown previewed as html. So when we start write JS for markdown preview we can instantly see it working & can focus more on JS.

```css
h1 {
  font-size: 1.5em;
}
h2 {
  font-size: 1.25em;
}
.highlight {
  background: rgb(255, 255, 0);
  color: black;
  padding: 0 0.25em;
  /* 0 for top-bottom , 0.25em for left-right*/
}
ul,
ol {
  padding: 0 1.2em;
  /* this padding for left-right is very important
    otherwise list marks wont be visible */
}
a {
  color: #1988ff;
}
```
