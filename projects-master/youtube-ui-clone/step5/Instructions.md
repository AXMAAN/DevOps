In this part of the Project, we will add videos to the content area. You need to duplicate video (not videos) into many places to make it look like Youtube and you can edit them with unique Youtube video information if it's available.

```
<div class="videos">
  <!-- a video starts -->
    <div class="video">
       <div class="thumbnail">
          <img src="https://avatars.githubusercontent.com/u/75475819?v=4" alt="" />
        </div>

          <div class="details">
             <div class="author">
                <img src="https://github.com/harshit-sharma-gits/youtube-clone-starter-files/blob/main/THUMB.png" alt="" />
             </div>
             <div class="title">
                <h3>
                    Introverts & Content Creation | Sumudu Siriwardana
                 </h3>
                 <a href="">
                        Francesco Ciulla
                  </a>
                  <span> 2M Views • 3 Months Ago </span>
             </div>
           </div>

         </div>
   <!-- a video Ends -->
 </div>
```

Now, let apply CSS to it.

```
.content {
  background-color: #f9f9f9;
  width: 100%;
  height: 100%;
  padding: 15px 15px;
  border-top: 1px solid #ddd;
  overflow-y: scroll;
}

.videos {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
}

.video {
  width: 270px;
  margin-bottom: 30px;
}
```

If you check the style for `.videos`, you will see `flex-wrap`. When the screen can only take four items, for example, other items will be moved to another row. That is what `flex-wrap` does.

```
.thumbnail {
  width: 100%;
  height: 170px;
}

.thumbnail img {
  object-fit: cover;
  height: 94%;
  width: 100%;
}
.author img {
  object-fit: cover;
  border-radius: 50%;
  height: 40px;
  width: 40px;
  margin-right: 10px;
}
```

`object-fit` in this case is used to clip the image to its container so as to remove overflow (areas where the image is bigger than its container) in height and width:

```
.details {
  display: flex;
}
 
.title {
  display: flex;
  flex-direction: column;
}
 
.title h3 {
  color: rgb(3, 3, 3);
  line-height: 18px;
  font-size: 14px;
  margin-bottom: 6px;
}
 
.title a,
span {
  text-decoration: none;
  color: rgb(96, 96, 96);
  font-size: 12px;
}
```

In this case, we make a layout out of `.details` and because we don’t set its flex-direction to property, it will be set to row – which is its default value. You see that a layout is also made out of the title and set its children to appear in a column by setting flex-direction to column.

We select the h3 tag that is inside `.title` and we set its color to somewhat black.

`line-height` is used to set the height of a line of text and in this case, we set it to 18px.

Finally we use `.title a, span` to select the anchor tag in `.title`. We also select all span tags on the page and set their text-decoration to none.

So what is text decoration? It has a design such as an underline that an anchor tag has, and we hide it in this case by setting it to none.

Wow, we have videos to the YouTube Clone! So what's remaining now?

See the next step >>