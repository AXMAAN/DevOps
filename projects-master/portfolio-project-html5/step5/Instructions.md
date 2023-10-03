finally welcome in the javascript part!

## though the js is just a bit, just taking you to the other pages.

- just make all icons working.

    - there are thousand ways of doing a task but here i can't give you all so guiding you how i acheive this task.

- we have to do some changes in styles.

    - first of all we can't click on any icons in our navbar and why we know because of the overlay so, first we have to take our navbar in front.

    - and remember that we have to do it in all files.

    - but if you have done like me created a base-css just do there, that's why its imp and handy to maintain a base-css so do it there or if you created different files which is a bad approach because now you have to change in all files.

    - so we can do this with just adding `position: relative` and `z-index: 1`.

    - now if you want you can add some hover effects on icons like `cursor: pointer` and `color: #fff` etc.


- now there is a global object named `window`, it gives us a lottt, you can search about it later but for now we will only talk about an object that window gives us is `location` and in this object we have some props and funcs.

- and you can search it further if you are interested, for now it has a property named `pathname`.

- `pathname` can give and set the path like "/" means the home page or "/public/work-tab.html" or "/public/contact-tab.html" and that's it this is what we need to do.

- first we will have to addEventListner we can either add this in all icons or we can use event delegation and add this on the navbar only.

- so we will use the easy approach and use event deligation smartly and add eventListener n the navbar.

- then we can use some if else condition for checking that click event is triggered by which icon.

- hint: you may find out it with `e.target.classList.contains("")`.

- then we can just do like `window.location.pathname = "/";` or `window.location.pathname = "/public/work-tab.html";` and `window.location.pathname = "/public/contact-tab.html";`.

- now if you followed the instructions honestly your page should work like this:

https://user-images.githubusercontent.com/91528741/194886708-3eed9150-4068-4efe-b989-b3346a70f243.mp4


