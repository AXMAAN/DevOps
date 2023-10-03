1. For making a header element in website there is a semantic tag as `<header></header>`

```html
<header></header>
```

2. For making responsive elements we are using `flex` flex-box.

```css
header {
  background-color: var(--secondary_color);
  display: flex;
  justify-content: space-between;
  padding: 1.6rem;
}
```

3. The `<a>` tag defines a hyperlink, which is used to link from one page to another and The `<form>` tag is used to create an HTML form for user input which we will use for searching the movies.

```html
<a href="#" class="logo">Watch New Movie</a>
<form id="search_form"></form>
```

4. The `<input>` tag specifies an input field where the user can enter data.

```html
<a href="#" class="logo">Watch New Movie</a>
<form id="search_form">
  <input type="text" id="search" class="search" />
</form>
```

5. <input type="text"> (default value). type define which type of value will enter as input and The placeholder attribute specifies a short hint that describes the expected value of an input field (e.g. a sample value or a short description of the expected format).

```html
<input type="text" id="search" class="search" placeholder="Search" />
```

6. Here we are using some different color properties you can use simple color also.

```css
.logo {
  font-size: 2rem;
  background: -webkit-linear-gradient(#374151, #94b2e0);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
}
```

7. In this search we will use this for searching movie by there name.

```css
.search {
  background-color: transparent;
  border: 0.2rem solid #64748b;
  border-radius: 5rem;
  font-family: inherit;
  padding: 0.5rem 1rem;
}
```

8. A CSS pseudo-element is used to style specified parts of an element.

For example, it can be used to:

    Style the first letter, or line, of an element
    Insert content before, or after, the content of an element

```css
.search::placeholder {
  color: #78716c;
}

.search:focus {
  outline: none;
  background-color: var(--primary_color);
  color: #fff;
}
```
