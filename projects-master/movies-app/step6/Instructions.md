1. When we/user submitting the movie name in search bar for the `addEventListener`(The addEventListener() method attaches an event handler to a document.) added that text of search to our path.

```js
form.addEventListener('submit', (e) => {
  e.preventDefault();

  const searchTerm = search.value;

  if (searchTerm && searchTerm !== '') {
    getMovies(SEARCH_URL + searchTerm);
    search.value = '';
  } else {
    window.location.reload();
  }
});
```

2.  To go back to that previous page which we are previewing from sorting the famous movies. writing addEventListener for load same page.

```js
logo.addEventListener('click', () => {
  main.innerHTML = '';
  getMovies(API_URL);
});
```

3.  Add media query for making responsive to ever screen. Use a media query to add a breakpoint

```css
@media only screen and (max-width: 700px) {
  header {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
  }

  .movie {
    width: 40%;
    background-color: var(--secondary_color);
    box-shadow: 0.2rem 0.2rem 3rem 0 rgba(0, 0, 0, 0.2);
    border-radius: 0.3rem;
    overflow: hidden;
    position: relative;
  }
}

@media only screen and (max-width: 500px) {
  header {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
  }

  .movie {
    width: 100%;
    background-color: var(--secondary_color);
    box-shadow: 0.2rem 0.2rem 3rem 0 rgba(0, 0, 0, 0.2);
    border-radius: 0.3rem;
    overflow: hidden;
    position: relative;
  }
}
```
