In this step we will add a user interactivity, where the user will be able to add notes. User can enter Note Title and Note Content and use the Add button to add the Note.

1. Create an object with "title" and "content" as key. We will use this object to store our data, let's call it `note`.
2. This is the perfect time to make use of useState Hook, create a useState for individual note to be added.
3. For simplicity, all user interactivity is handled in our `App.jsx` component. To support this, we need to pass data and functions as props.
4. Create an array of the `note` object, we can use this array to render all the `note` objects in `App.jsx`. Implement this array using useState Hook.
5. When user clicks `add`, use the passed prop functions from `App.jsx` to handle adding the `note` in `createArea.jsx` to `notes` array in `App.jsx`.

Try to implement the form fields in form a contolled component. Since, we are using form for `CreateArea.jsx`, make sure to prevent default reloading when user clicks on `submit`.

Now that we have added the `add` functionality with our components, let's move on to the next step and add delete functionality.
