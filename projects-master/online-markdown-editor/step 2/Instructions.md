## Preview the text user inputs unformatted

- First we will select the html elements in javascript. Head over to `script.js` & get the textarea & article.

  ```js
  const textinput = document.querySelector('#textinput')
  const markdown_preview = document.querySelector('article')
  ```

- So we will take the input from textinput & display it to the preview side as the user types in. In order to do that we will add a event listener to the text input & the event we will listen to is **input**.

  ```js
  textinput.addEventListener('input', (e) => {})
  ```

The **input** event fires when the value of an `<input>`, `<select>`, or `<textarea>` element has been changed.

This `e` is the Event interface that represents the actual input event taking place in DOM. We can get the text (or value) of the event from `e.target.value`. The read-only target property of the Event interface is a reference to the object onto which the event was dispatched. Here the target is the text input itself.

- Inside the arrow function we will assign this text input's value to the innerHTML gets or sets the HTML contained within the article element. We are modifying the inner html because later on we will wrap the headings (`# h1` or `## h2`) , lists (`- item1` or `1. item1`) & other stuff into html elements.

  ```js
  let content = e.target.value
  markdown_preview.innerHTML = content
  ```
