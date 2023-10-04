In this step we will add the delete function, when user clicks on `delete` button, the respective note is deleted.

1. We need to modify our add function in our `App.jsx` to pass an `id` to every note created.
2. This passed `id` can be used as unique identifier to delete particular `note`.
3. When user clicks on `delete` button on the particular `note` we can pass the `id` of the `note` element.\
4. We can use the `id` to call a delete function in `App.jsx` which filters the main `notes` array to remove `note` with passed `id`. We can use the inbuilt `filter` function for arrays.

Now, we have successfully built a functioning clone of Google Keep Notes with add and delete note functionality.
