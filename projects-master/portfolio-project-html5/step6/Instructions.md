finally the last step and you have completed a nice portfolio project!!!

## use css to make the page responsive!

- let's start with `index.html`.

    - so first we are going to use media queries.

    - if you know what they are then you are good to go otherwise read [here](https://www.w3schools.com/css/css_rwd_mediaqueries.asp).

    - now right click on the page and open inspect then in the inspector you will see a mobile icon in left click it.

    - now you will be able to resize your page.

    - so resize your page and see where is the page breaking.

    - for me `750px` is the point where the page was looking squashed , so i choosed  `750px` you can take your point.

    - now just write this for confirmation that our media query is working:
    ```css
    @media (max-width: 750px){
        body{
            display: none;
        }
    }
    ```

    - if it works awesome otherwise look carefuly maybe a typo.

    - now let's write some valid code in media query so, as you can see in design that we have deleted the text part in mobile view, you can do it with `display: none`.

    - the text part is gone but still the image is squashed, because remember we gave the image `width: 35%` so now let's make it 100% so, `width: 100%`.

    - but now the image is streched out, and why? remember we gave the profile-card `width: 100%`, now we can do something like `width: fit-content` you can read about it later but for now it will solve our problem.

    - now we need to make it cintered in page and margin top a bit so `margin: 2em auto` and tada!

    - now just set arrow-up like `top: -28px;` and left that fits for you.

    - if you want to make everything perfect you can set the height but i think its okay for now.

    - and ya its now great!

    - if you followed the instructions it should work like this:

    ![Screenshot1](https://user-images.githubusercontent.com/91528741/194884041-41aec967-c16d-4741-a45b-8bfb71ebfe50.png)


    



