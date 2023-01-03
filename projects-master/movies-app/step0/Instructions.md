

#### Your users should be able to:

- See New Movies which is sorted by rating and newest.

- User can also search the movie by there names.

API Documentation is available at https://developers.themoviedb.org/3/getting-started/introduction

To link the `style.css` ans `style.js` file with the `index.html` file. Add the following line of code inside the `<head>` tag of the `index.html` file, using the `<link>` tag for `style.css` and for the `style.js` file use `<script>` tag.

```html
<link rel="stylesheet" href="style.css" />
<body>
  <!-- At the end of the body tag -->
  <script src="style.js"></script>
</body>
```

- Here the `rel` attribute specifies the relationship between the HTML document and the linked file. The `href` attribute specifies the path to the linked file.

#### To add google font to our project.

1. First we have to import that font from [Google fonts website](https://fonts.google.com/).
2. Copy that import link and paste it into the project folder in the `style.css` file.

```css
@import url('https://fonts.googleapis.com/css2?family=Freehand&family=Kaushan+Script&family=Poppins:ital,wght@1,200&family=Roboto:wght@400;700&family=Smooch&display=swap');
```

#### Make some default styling for the project.

- These are the color which we will using on website so we are created as var.

```css
:root {
  --primary_color: #64748b;
  --secondary_color: #9ca3af;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: var(--primary_color);
  font-family: 'Poppins', sans-serif;
  margin: 0;
}
```
