In this step our goal is to create the `Quote` component to fetch and show quote data using Quotable API.

Before jumping into the code of the project, make sure that you understand the [react hooks](https://reactjs.org/docs/hooks-intro.html) and data fetching in functional components.

## What will you do?

In this step you are tasked to create a new `Quote` component in components folder and import it and use inside `App` component.

1. Add a `useEffect` hook to make fetch call to [Quotable API](https://api.quotable.io/random). It will return a JSON response something like this

   ```json
   {
     "_id": "io0NDLSyHH4Q",
     "content": "The truth you believe and cling to makes you unavailable to hear anything new.",
     "author": "Pema Chödrön",
     "tags": ["famous-quotes"],
     "authorSlug": "pema-chodron",
     "length": 78,
     "dateAdded": "2020-09-09",
     "dateModified": "2020-09-09"
   }
   ```

2. Use the react [useState](https://reactjs.org/docs/hooks-state.html) to store the response in State. Show the quote content and author name by using the state variable.

3. Add a refresh button to refetch the data on click. You can use the `refresh.svg` image from assets to show as label.

4. Add some styling to the component. You can either add it directly to `index.css` or create a separate css file and import that in component.

Now we should be able to see a random quote on screen on load and also fetch a new quote on click of refresh button.
