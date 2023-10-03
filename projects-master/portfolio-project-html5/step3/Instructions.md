welcome! now you're gonna style the work page.

## take the color from style-guide and fonts from assets/fonts/

- you can follow any approach from below:
    - either you can create a nav exactly same that we builded in `index.html` and style it again and add bg again so on and so forth..

    - or as i did you can create a base-css as all pages are sharing the almost same layout and colors and fonts.

    - so yeah we can create a base-css and in that file we can write stylings for navbar as its in all pages, the background color of the body, the wraper div inside the body that we are doing in center with margin, the arrow-up etc. 

- now do any one from above and after that your work-tab should look like this: 


![Screenshot1](https://user-images.githubusercontent.com/91528741/194878937-c1e69773-e441-4cc5-82a4-01c46f54b7ca.png)



- make a gallery like structure of photos section.
    - its already looking like a gallery.
    - add a `background-color: #fff`.

- make the container center in the page.
    - its already centered we just need to do the images in center and we can do it easily with `text-align: center`.

    - this will now give up expected results.

- make the container points to the folder like icon.
    - you can copy-paste the code with which we created that arrow and adjust it or if you created base-css then you just need to add a div with class arrow-up and set the left property.
    
    ```css
    .arrow-up {
        width: 0; 
        height: 0; 
        border-left: 25px solid transparent;
        border-right: 25px solid transparent;
    
        border-bottom: 30px solid #fff;
    }
    ```


- make the page look like the design that is given.
    - if you followed the above steps it should look like the given design.

- now your work-tab should look like this:

![Screenshot2](https://user-images.githubusercontent.com/91528741/194879127-e0a9a389-9e71-49f7-bf73-d174dabc0a4d.png)

