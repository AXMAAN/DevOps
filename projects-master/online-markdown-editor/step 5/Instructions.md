# Toggling theme on button click

Finally before finishing the project we will add this theme toggle. To seperate the theme changing functionality with the markdown functionalities I will suggest to write the js for this in `index.html` itself.

- So first get/select the theme button.

  ```html
  <script>
    const themeBtn = document.querySelector('.theme')
  </script>
  ```

- Then add a click event listener. When this button is clicked we will toggle (add or remove) a class from body. Then also update the theme button's emoji based on the theme.
  ```js
  themeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark')
    themeBtn.textContent = document.body.classList.contains('dark')
      ? '☀️'
      : '🌙'
    // if the body has a dark class then the theme is dark so ☀️ will be shown
    // so that user can change to light theme . Similarly  if body does not have
    // dark class then it is light theme , so show 🌙 for user to change to dark theme
    themeBtn.classList.toggle('dark')
  })
  ```
- Add some css to `.dark` & for a nice & smooth transition add some `transition` to body

  ```css
  .dark {
    background: #22272e;
    color: #eee;
  }
  body {
    /*below all existing css */
    transition: all 500ms ease;
  }
  ```

Finally the project should be working as described. Congratulations on completing this project 🥳
