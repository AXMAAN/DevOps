Let's make our clone responsive now, so that it can be viewed on mobile devices as well as big screens comfortably. How do we do it? Well, we will use CSS media queries. Now, let get started!

So, we will add the CSS code below to the CSS file of the YouTube Clone.


```
@media (max-width: 768px) {
    .side-bar {
      display: none;
    }
    .search {
      display: none;
    }
}
```

`@media (max-width: 768px) { }` is used to set the device screen sizes that the code in the media query will apply to.

In this, `max-width: 768px` means that the styles in the media query will be applied to any screen size that is equal to or less than 768px.

So, whenever the screen size in use is 768px or less, we will hide the sidebar and the search input by setting their display property to none.

```
@media (max-width: 900px) {
   .search input {
    width: 25rem;
  }
}
```

Finally, we make the the search input a bit smaller whenever the screen size of the device in use is less or equal to 900px.

That is it.

Hurraaaay...we're done in making the YouTube clone! Thanks for all you hard work!