In this step you have to make sure that the nav bar is dynamically fix while scolling text animation is working properly.

you have to add span tag in index.html for text typing animation.
```html
        <h1>I'm YourName<span id="type2"></span></h1>
```

The following are the code exmaple to use in index.js file for nav fix and text animation : 

```js
// nav bar position
const navBar = document.querySelector(".nav");
const navHeight = navBar.getBoundingClientRect().height;
window.addEventListener("scroll", () => {
  const scrollHeight = window.pageYOffset;
  if (scrollHeight > navHeight) {
    navBar.classList.add("fix-nav");
  } else {
    navBar.classList.remove("fix-nav");
  }
});
```


```js
// text animation  
new TypeIt("#type1", {
  speed: 120,
  loop: true,
  waitUntilVisible: true,
})
  .type("Dev", { delay: 400 })
  .pause(500)
  .delete(9)
  .go();
```
Add custom color in index.js for text

You can adjust the scroll speed and animation. 

