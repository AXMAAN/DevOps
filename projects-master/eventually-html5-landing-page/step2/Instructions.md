In this step you'll be adding the styles to make the landing page look better. 

1. import the fonts from the assets and write the `@font-face` properties for both of the font assets. 

    ```css
    @font-face {
        font-family: 'Roboto';
        src: local('Roboto'), local('Roboto-Regular'),
            url('assets/fonts/Roboto-Regular.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
        font-display: swap;
    }
    ```

    Make sure to write similar @font-face rule for the Roboto Bold (font-weight: 700)

2. Make sure to align the content by setting top and bottom margins 

3. Set the background-color of the Sign up button to `#1cb495` 

    Set the border-radius property for both input and the submit button to `6px`

4. Make the form a flex container and set the `align-items` property to center and `justify-content` to space-between. 

5. Make a flex container for all the social icons, make sure to set the size for the svg icons to 18px. 

6. Add the font styles to the heading and the description and set the font-family to Roboto-700 and Roboto-400 respectively for Heading and description. 

    Set the color of the description and the footer text to `rgba(255,255,255,0.5)`



