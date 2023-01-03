So you have included the required font family and icons in step0, awesome! Now let's break down our project into units, so that it is easy to tackle along.

Our project will be having mainly two sections:
* Header section, and
* Main body

The Header contains three sections (left, center and right). The left section contains the logo and menu, the center contains the search box and an icon, and the right contains navigation icons.

The Main body contains two sections (sidebar and content). The navigation links in the sidebar are also similar, so they are just one thing. The same thing happens to the videos in the content section.

So, our YouTube clone has a header, main, sidebar, content, video-card, navigation link and navigation icon as the major units. This was the breakdown of the units of the web page we want to create.

In this step let's create the layout of the YouTube clone in HTML. Start off by adding a `<header>` inside body, and give it a class `header`.

Then add a `<main>` after the `<header>`, with two divs (`<div>`) inside. Give the divs these classes: `side-bar` and `content`.

For the content of these tags, put a single `.` inside them.

Now your body should look like this:

```
<header class="header">.</header>
<main>
    <div class="side-bar">.</div>
    <div class="content">.</div>
</main>
```

We have a header tag to create the header section of the YouTube clone. We'll add the YouTube logo, search box, and other navigation icons to the header later.

There is also the main section that contains the side-bar and content. The side-bar will contain some navigation links while the content will contain videos.

Wait! Our code doesn't look too beautiful after running. Well, we'll fix that with CSS in the next step!

