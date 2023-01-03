Let's start adding styles to our page.

Flexbox layout is the best way to arrange elements in a flexible way. It is a great way to organize your page and make it responsive across all viewports. The breakdown is as follows:

1. Make the `#gallery-container` a flex container.

   Our agenda is to make the images responsive and occupy the whole width of the page. To do that, we need to make the `#gallery-container` a `flex` container.

   ```css
   #gallery-container {
     display: flex;
     flex-wrap: wrap;
   }
   ```

2. Set the `width`, `height` and `object-fit` of the images, so that they maintain the aspect ratio and occupy the whole width of the article.

   ```css
   .gallery-image {
     width: 100%;
     height: 100%;
     object-fit: cover;
   }
   ```

3. Set the position of the article with `.img-container` to `relative` and set the `flex` property to `1 0 100%`. The `flex` property is a shorthand for `flex-grow`, `flex-shrink` & `flex-basis` properties combined.

   ```css
   .img-container {
     position: relative;
     flex: 1 0 100%;
   }
   ```

   With this, the `flex-container` will occupy the complete width of the page.

4. Make sure that `.title` is visible properly.

   ```css
   .title {
     position: absolute;
     bottom: 0.5em;
     left: 0.5em;
     font-family: "Source Sans Pro", sans-serif;
     color: white;
   }
   ```

5. Add the media queries so that the images are responsive across all viewports.

   ```css
   @media (min-width: 768px) {
     .img-container {
       flex: 1 0 50%;
     }
   }

   @media (min-width: 1280px) {
     .img-container {
       flex: 1 0 33.333%;
     }
   }
   ```

We have finally complete the gallery and made it responsive. Next up, adding the footer!
