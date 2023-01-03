# Configure EJS

For Configuring EJS, do the following steps:

* Create a folder named `views` in the root directory.
* Create a file named `index.ejs` in the `views` folder.
* In EJS file, add required code for below given tasks:
    * Add a form. Below are the components of the form: 
        * Input Field for Playlist Link (required).
        * 2 Input field for Range (Start and End Video) (optional).
        * Submit Button
    * Add a div with id `result`.
        * Length of the Playlist will be displayed in this div.
* In EJS File Form, add `action` attribute and set it to `/` and `method` attribute and set it to `POST`.
* Add Styling to the EJS file using CSS to make your page look good or look similar to the `cover-image`. 
* Add required code to the `index.js` file in the root directory.
    * Set the view engine to EJS.
    * Add a route for `/` with `GET` method for rendering the ejs file.
    * Add a route for `/` with `POST` method for getting the data from the form.


### Optional Steps:

* You can add URL Validator.
* You can add error message div for any error that may occur.
* You can add a loader for the time when the request is being made.
* You can add meta tags for SEO.
* You can add a favicon in the EJS File.

