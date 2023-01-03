1. `.movie` class is for movie detail.

```css
.movie {
  width: 28rem;
  margin: 1.9rem;
  background-color: var(--secondary_color);
  box-shadow: 0.2rem 0.2rem 3rem 0 rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem;
  overflow: hidden;
  position: relative;
}
```

2. We want full width of the img so: `width:100%`

```css
.movie-img {
  width: 100%;
}
```

3. These class with add the details which have a H1 and the span of content rating which will we center and in display position with flex layout.

```css
.movie-info {
  display: flex;
  justify-content: space-between;
  padding: 0.8rem;
  letter-spacing: 0.1rem;
  font-size: 1.6rem;
}
```

4. The span tag class will change as per rating which will come form the APIs

```css
.movie-info h3 {
  color: #eee;
}

.movie-info span {
  background-color: var(--primary_color);
  padding: 0.5rem 0.5rem 0.5rem;
  border-radius: 0.5rem;
  font-weight: bold;
}
```

5. Rating have range of 1 - 10 as per rating we will change the content/ text color of rating so here we are creating 3 class modifier = .red(>=3), .orange(>=5), .green(>=8) represents.

```css
.movie-info span.green {
  color: lightgreen;
}

.movie-info span.red {
  color: crimson;
}

.movie-info span.orange {
  color: orange;
}
```

6.The Overview section styles.

- The we want the section as hidden but we want the section visible when we hover the movie div.
- For hiding we can set there left and right bottom as 0 and transform: translateY(101% by which it will be hidden which we cover entire width of the movie section.

```css
.overview {
  background-color: white;
  padding: 0.8em 0.8em;
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  max-width: 100%;
  transform: translateY(101%);
  font-size: 1.8rem;
  color: #a8a29e;
  transition: all 0.2s ease;
  box-shadow: 0.2rem 0.2rem 1rem rgba(0, 0, 0, 0.2);
}
```

7. The transform: translateY(0) will make the overview section visible because the section goes more then a 100 per which basically taking more then a space which hidden down to section.

```css
transform: translateY(0);
```
