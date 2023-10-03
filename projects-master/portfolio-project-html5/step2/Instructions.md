huh! champ welcome in the styling part.

## take the color from style-guide and fonts from assets/fonts/

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

- add this code in your base css this is fonts that we will use later.

- add background image `assets/images/bg.jpg` to the body.

- make the content center, use `margin: auto;` grid or flexbox in order to achieve it.

- add an overlay from `assets/iamges/overlay.png` you can apply it on `body::after`

- make nav items horizontal aligned.
    - use flexbox for this.
    - color them `#ffffffb4`
    - space them and add a `font-size: 2rem` to them to make them big.


- make the card like structure of main part.
    - first use flexbox for align text and image horizontaly.
    - make the text in center.
    - now your `index.html` should look like this:

    ![Screenshot1](https://user-images.githubusercontent.com/91528741/194873962-29b25605-6043-42ee-9ae1-0f20c21f992f.png)



    - make the card about 850px wide.
    - text-side will be 65% and image-side will be 35% of the card.
    - add `background-color: #ffffff` to text part and the home icon.
    - give `font-family: 'bold'` to the name text and `font-family: 'light'` to the info text.
    - now your `index.html` should look like this:

    ![Screenshot2](https://user-images.githubusercontent.com/91528741/194875638-ac41b57b-f760-4025-b377-3762a3c64a39.png)



    - now your button, give it `position: absolute` and `position: relative` to the profile-card div.
    - now set it like `right: 0` and `top: 40%` then give it some styles and `backgroung-color: rgba(0, 0, 0, 0.7)` for the transparency.
    - now the page should look like this:

    ![Screenshot3](https://user-images.githubusercontent.com/91528741/194875729-c79bbee8-74a9-4b59-8740-919930b0f745.png)



- style the footer.
    - give it `color: #f4f4f4` and select the anchor tag and give the same color and make `font-size: .9rem`

- now the last thing the triangle pointing to the home icon.
    - we can make some shaped with css you can search for it later but for now take this:

    ```css
    .arrow-up {
        width: 0; 
        height: 0; 
        border-left: 25px solid transparent;
        border-right: 25px solid transparent;
    
        border-bottom: 30px solid #fff;
    }
    ```

    - now make a div with class arrow-up in you html file and make its `position: absolute` and as the card has `position: relative` so it will be relative to that and set `top: -20px` something in negative because we want to put it up and set left accordingly.
- awesome.. index.html is styled it should now look something like this:
    
    
![Screenshot4](https://user-images.githubusercontent.com/91528741/194875980-7fa16bae-cf7a-42e3-b954-92d13d0024c5.png)
