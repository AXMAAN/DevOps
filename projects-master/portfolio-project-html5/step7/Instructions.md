welcome in the part of making work-tab responsive.

## our break point is : 850px.

- we can remove the h1 in media query by just `display: none;`.

- we can select thw wraper and balance padding with `padding: 1em`.

- and a surprise!! we don't need to make the gallery responsive....

- why? because width of every image is `260px` and `max-width` of our wraper is `930px` so means we can put 3 photos in one line that's why we don't ha to worry about this thing when we were adding styling.

- but how exactly is this responsive is because we haven't touched it, yes html is responsive by default we make it unresponsive.

- what is happening is when the width is decreasing for example when width is `690px` the space is enough for only 2 so the third one is going in second line automatically.

- this is why sometimes we should just give some simple styling and let the things done itself and if at somepoint it's not what we want we can catch and fix.

- as i said we can catch and fix at a point i found the images so close and the space are available on sides so i catch that point and add `margin-inline: 1rem` and then its awesome.

- last thing is to put the arrow up on its correct place just set `top` and `left` accordingly.

- that's it if you followed the instructions your work page should look like this:

![Screenshot1](https://user-images.githubusercontent.com/91528741/194884338-59d81a3a-e0e6-43d2-9e82-2124e5e09f96.png)



