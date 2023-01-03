welcome in the part of styling the contact page!

## take the color from style-guide and fonts from assets/fonts/

- same as i said in last instructions, you can write the basic css for layout and background stuff or you if you've created you can use base-css instead.

- in this case we have created base-css so lets link it!

- now the contact-tab should look like this:

![Screenshot1](https://user-images.githubusercontent.com/91528741/194883008-19f76e21-9081-42e1-a673-bdb957104e61.png)


- style name, email, subject and message field.

    - add `background-color: #f4f4f4` and and `font-family: 'light'` if you've folowed all the instructions til now it should work.(note: this font-family is custom that we've setted in base-css if you have'nt you can here is the code and make sure to set the path accordingly.)

    ```css
    @font-face {
        font-family: 'bold';
        src: url(./assets/fonts/6xK3dSBYKcSV-LCoeQqfX1RYOo3qOK7lujVj9w.woff2);
    }

    @font-face{
        font-family: 'light';
        src: url(./assets/fonts/6xKydSBYKcSV-LCoeQqfX1RYOo3ik4zwlxdu3cOWxw.woff2);
    }   

    ```

    - we can wrap name and email in a div with class user-info.

    - now, we can set its `display: flex` and set `width: 48%` of its child ie. the name and email inputs, and `jusitify-content: space-between` this should give us the desired result.

    - after this we can set input, textarea's `display: block` and `width: 100%` so that subject and message field take up the ful width (note: a catch here, if we try to strech out the message field this would result in overflow so to fix this we can add `max-width: 100%` with this the message field will be strech in its place only.)

- styling button.

    - add `background-color: #222` and `color: #f4f4f4`.

    - now if you did the above things your button will be of full width and this is something we don't want so what we can do is set its `width: auto` and this will fix it.

- make the form centered.

    - as we have linked the base-css its already done and if you haven't you can just do `margin: auto` in the wraper.

- making the arrow pointing to the contact or mail icon.
    - again coming from base-css just need to add a div with class arrow-up inside wraper and set left and otherwise here is the code for arrow-up:

    ```css
    .arrow-up {
        position: absolute;
        width: 0; 
        height: 0; 
        border-left: 25px solid transparent;
        border-right: 25px solid transparent;
    
        border-bottom: 30px solid #fff;
    }
    ``` 
- make the page look like the design that is given.
   
    - if you've followed the instructions above it should be looking like the given design.

- inputs not working!!

    - problem: we used `body::after` for the overlay remember?
        - what it does is it come in top of body and adding the overlay that we want, but the problem is that we can't click anything or anything is not working now because when we clicking something we're clicking on the overlay image.

    - fix: now that we know the problem now so we need to fix it.
        - we can either select the elements or give a class to all the inputs or field which we want to be on top.

        - in this case we have gave the class on-top to all the elements we want to be in front but code is same just add a postion and a bigger `z-index`.

        ```css
        .on-top{
            position: relative;
            z-index: 1;
        }
        ```

- now everything is done your contact-tab should look like this (this is not border i have clicked on it):

![Screenshot2](https://user-images.githubusercontent.com/91528741/194883336-f9c62a7b-a10a-4345-bdc0-f95e7b76a8cc.png)

