## Getting Started

First thing we should do is to structure the `HTML`. The basic structure will be first the Theme Toggle Button then then main markdown section.

- Create a button (for theme changing) & create a main. The button should have ☀️ as text content.

  ```html
  <button class="theme">☀️</button>
  <main></main>
  ```

  > The `<main>` HTML element represents the dominant content of the <body> of a document.

- Now build **2 sections** inside main & have a `h1` inside each of them , first h1 will be "Text Editor" & 2nd one will be "Preview" .

  ```html
  <main>
    <section>
      <h1>Text Editor</h1>
    </section>
    <section>
      <h1>Preview</h1>
    </section>
  </main>
  ```

- Then inside the 1st section below h1 create a textarea to take markdown input.

  ```html
  <section>
    <h1>Text Editor</h1>
    <textarea name="textinput" id="textinput"></textarea>
  </section>
  ```

  > The `textarea` element represents a multiline plain text edit control for the element's raw value.

- Inside the second section below h1 create a article element. Here we will display the html formatted preview from markdown input.

  ```html
  <section>
    <h1>Preview</h1>
    <article></article>
  </section>
  ```

  > The `<article>` HTML element represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include: a forum post, a magazine or newspaper article, or a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.
