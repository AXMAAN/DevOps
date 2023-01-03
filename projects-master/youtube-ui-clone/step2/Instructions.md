So you have made the layout in HTML, but as you can see it is not looking good. So, let's style it using CSS.

In this step we are going to stylize the Header and Main section. Open up style.css, and

## Reset the HTML Default styles

```
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

The asterisk * is a CSS selector that selects all HTML tags on our page. We set their margin and padding to 0. We then set their box-sizing to border-box.

## Set the font family

```
body {
  font-family: 'Roboto', sans-serif;
}
```

This sets the font family to Roboto, which we included in the step 0. We select the body tag and set its font-family to Roboto and use sans-serif as a fall-back in case Roboto is not available.

## Style the header

```
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
    padding: 15px;
}
```

The `.header` class name is used to select (or connect to) the header section of our website so that we can add some styles to it.

We set its display property to flex to create a layout out of it, and then we can easily divide it into sections. We will divide it into sections later.

`Justify-content: space-between` means we want the contents in the header to have space between them once there are more than one.

`Align-items: centre` is used to move all the contents of the header to the centre-left of your screen. That is called vertical alignment. We finally set the `height` of the `header` to 60px and its padding to 15px.

## Style the main section

```
main {
   height: calc(100vh - 70px);
   display: flex;
   background-color: #f9f9f9;
}
```

We set the height of the main section to calc( 100vh - 70px). 100vh means the total height that is visible in a browser without scrolling. And we use calc ( 100vh - 70px) to run a calculation that subtract 70px from 100vh.

We set its display property to flex to create a layout out of it. Finally, we set its background colour to #f9f99f which is a kind of silver or ash.

## Style the side-bar

```
.side-bar {
    height: 100%;
    width: 17%;
    background-color: white;
    overflow-y: hidden;
}
```

The height of the .side-bar is set to 100% of its parent. That means it will have the same height as its parent. Its width is set to 17% of its parent and background colour set to white.

Phew! That was a lot of work! You might want to reiterate over tis step again, just to be sure ;)

In the next step, we are going to add responsiveness to our project, and add contents to the header.