1. Using `<main></main>` element we will inject a div element into the html as movie detail card.

```html
<main id="main"></main>
```

2. This `main` section will display the movie detail. So for that there will be many movie so here will be display the movie detail card with using `flex-box`.

```css
#main {
  display: flex;
  flex-wrap: wrap;
}
```

3. The main section contains the movie div that will be display the movie detail card.

```html
<main id="main">
  <div class="movie"></div>
</main>
```

4. Here src will be getting from API. we will give it in step5

```html
<img src="" alt="movie image" class="movie-img" />
```

5. Here we will show the movie detail in movie-info class div.

```html
<div class="movie-info"></div>
```

6. After getting Data from API we will manipulate span class as per rating in different color.

```html
<div class="movie-info">
  <h3>Movie Title</h3>
  <span class=".green">7.9</span>
</div>
```

7. The overview section is for information of the movies.

```html
<div class="overview">
</div
```

8. Lorem(a number) "20" or some other number will generate random text as per written length here Lorem20 will generate some text like = Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vitae aliquam ipsa in. Ducimus voluptatum, adipisci voluptate velit voluptatibus quasi eligendi!

```html
<div class="overview">
  <h3 class="overview">Lorem20</h3>
</div
```

- after Enter the written Lorem20

```html
<div class="overview">
  <h3 class="overview">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vitae aliquam ipsa in. Ducimus voluptatum, adipisci voluptate velit voluptatibus quasi eligendi!</h3>
</div
```
