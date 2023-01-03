In this step, we are going to add some content to the sidebar. In YouTube you might have seen that the side-bar contains some icon list, we are going to add that list here

```
<div class="side-bar">

   <div class="nav">
      <a class="nav-link active">
        <i class="material-icons">home</i>
        <span>Home</span>
      </a>
  </div>

</div>
```

Then, we need to first style the navbar, which is the wrapper for all the links:

```
.nav {
    width: 100%;
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    margin-top: 15px;
}
```

The only thing I will explain here is flex-direction. This determines whether we want the children to appear in a column (vertical) or row (horizontal). In this case we go with a horizontal display.

Then, let's style the nav-link above with CSS as shown below:

```
.nav-link {
   display: flex;
   align-items: center;
   padding: 12px 25px;
 }
 
.nav-link span {
   margin-left: 15px;
 }
 
.nav-link:hover {
   background: #e5e5e5;
   cursor: pointer;
 }

.active {
   background: #e5e5e5;
}
```

You can see, we are using the `:hover`. The styles in it will only be applied whenever we move our cursor over the home navigation link.

Wait, we have many links in the sidebar, so how are we going to create that? Well, we just do what every developer loves - copy and paste and then edit it as in below:

```
<div class="side-bar">
  <div class="nav">
    <a class="nav-link active">
      <i class="material-icons">home</i>
      <span>Home</span>
    </a>
    <a class="nav-link">
      <i class="material-icons">local_fire_department</i>
      <span>Trending</span>
    </a>
    <a class="nav-link">
      <i class="material-icons">subscriptions</i>
      <span>Subscriptions</span>
    </a>
  </div>
  <hr>
</div>
```

After pasting three links, we want to make them into separate categories by using the `<hr>` tag to create a line that separates them from the next category. Now, let’s style the hr tag.

```
hr {
   height: 1px;
   background-color: #e5e5e5;
   border: none;
}
```

Then, we will add the remaining code after the hr tag as in below:

```
    <a class="nav-link">
       <i class="material-icons">library_add_check</i>
       <span>Library</span>
    </a>
    <a class="nav-link">
       <i class="material-icons">history</i>
       <span>History</span>
    </a>
    <a class="nav-link">
       <i class="material-icons">play_arrow</i>
       <span>Your Videos</span>
    </a>
    <a class="nav-link">
       <i class="material-icons">watch_later</i>
       <span>Watch Later</span>
    </a>
    <a class="nav-link">
       <i class="material-icons">thumb_up</i>
       <span>Liked Videos</span>
    </a>
```

Wow, we are done with the sidebar of the YouTube clone!