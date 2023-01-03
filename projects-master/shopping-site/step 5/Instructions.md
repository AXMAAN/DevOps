Follow these steps for the fifth and final milestone that is to add js methods for showing/hiding sidebar onn mobile view :

- open the `sidebar.js` file in `js` folder
  
- the file already is connected to components and all you need to do is to fill in the methods

- for `displayModal` method you need to set the display property of modal to block 
    ```javascript
        modal.style.display = 'block'
    ```
    and set the transform property of sidebar to translate it on x-axis to 0%  (previously translated to 100% through css on `sidebar` class)

- for `hideModal` method ypu need to set the display property of modal to none and translate the sidebar on x-axis back to 100% so that the sidebar is hidden.

### Viola! 🥳 🎉   the website's completed Congratulations!!!! 