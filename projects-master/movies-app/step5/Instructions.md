1. The purpose of "use strict" is to indicate that the code should be executed in "strict mode".
   With strict mode, you can not, for example, use undeclared variables.

```js
'use strict';
```

2. Use your API Key instead of which is written here which we got in step4.

```js
const API_URL =
  'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=4f6690e5920a43000b65b9bf0b5869bf&page=1';
const IMG_PATH = 'https://image.tmdb.org/t/p/w1280';
const SEARCH_URL =
  'https://api.themoviedb.org/3/search/movie?api_key=4f6690e5920a431c7b65b9bf0b5869bf&query="';
```

3. These variables are for dom. to insert and for search input.

- The getElementById() method is one of the most common methods in the HTML DOM. It is used almost every time you want to read or edit an HTML element.
- The querySelector() method returns the first element that matches a CSS selector.

```js
const main = document.getElementById('main');
const form = document.getElementById('search_form');
const search = document.getElementById('search');
const logo = document.querySelector('.logo');
```

4. Here getMovies Function is use for fetching the movies data.

- Here we also have to do error handling for not getting search movie.

```js
// Get initial Movies
getMovies(API_URL);

async function getMovies(url) {
  const res = await fetch(url);
  const data = await res.json();

  if (data.results.length === 0) {
    main.innerHTML = '';

    const createErrorEL = document.createElement('div');
    createErrorEL.classList.add('errorHandle');

    createErrorEL.innerHTML = `<h1>Oh no 🙅🏻 ! There is no such movie exists </h1>`;

    main.appendChild(createErrorEL);
  } else {
    showMovies(data.results);
  }
}
```

5. The showMovies Function will show the movie detail in the page content which user will see in our website.

- We are using createElement is basically a string that specifies the type of element to be created.

```js
function showMovies(movies) {
  main.innerHTML = '';

  movies.forEach((movie) => {
    const { title, poster_path, vote_average, overview } = movie;

    const createEL = document.createElement('div');
    createEL.classList.add('movie');

    createEL.innerHTML = `
    <img src="${IMG_PATH + poster_path}" alt="movie image" class="movie-img" />
        <div class="movie-info">
          <h3>${title}</h3>
          <span class="${getOverviewRating(
            vote_average
          )}">${vote_average}</span>
        </div>
        <div class="overview">
          <h3 class="overview">
            ${overview}
          </h3>
        </div>
    `;

    main.appendChild(createEL);
  });
}
```

6. The getOverviewRating Function will return the color string as per movie rating.

```js
function getOverviewRating(rating) {
  if (rating >= 8) {
    return 'green';
  } else if (rating >= 5) {
    return 'orange';
  } else {
    return 'red';
  }
}
```
