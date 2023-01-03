Let's start adding functionality to our app using very few lines of Javascript.

1. Create a constant variable called api to store or to store API endpoint to which we would be sending a request to get new quotes.

   ```js
    const api = "https://api.quotable.io/random";
   ```

        Note we will be using public Open-Source API [this](https://api.quotable.io/random) to generate new quotes.
        Please Star this [Repo](https://github.com/lukePeavey/quotable) and support the Developer for creating such a great and easy to use API


 2. Now let's grab few elements from our HTML using id's we specified while setting up boilerplate code in step 1 using `document.getElementById()`

```js
    // Grabbing Quote and Author elements
const quote = document.getElementById("quote");
const author = document.getElementById("author");
const btn = document.getElementById("btn");
```

3. Attach an Event listner on the button using variable `btn` which we grab and initialized in previous step

```js
    btn.addEventListener("click", getQuote);
```

     Note that the Event that we attached to our button is a click event. So that whenever button is clicked it would fire up getQuote function which we will be setting up in the next step.

4. Now lets implement the important and stand alone function `getQuote` within which we will make a request to generate new quote using Fecth API.

Fetch API is an in-built API built into every browser.It provides a JavaScript interface for accessing and manipulating parts of the protocol, such as requests and responses. It also provides a global fetch() method that provides an easy, logical way to fetch resources asynchronously across the network.

```js
 function getQuote() {
    fetch(api)
        .then((res) => res.json())
        .then((data) => {
            quote.innerHTML = `"${data.content}"`;
            author.innerHTML = `- ${data.author}`;
        })
        .catch((err) => {
            console.error('Error:', err);
        });
}
```
Now important characteristic about fetch() is it always returns a Promise which should be resolved using .then and .catch as shown above.

The simplest use of fetch():- takes one argument — the path to the resource we want to fetch — and does not directly return the JSON response body but instead returns a promise that resolves with a Response object.

The Response object, in turn, does not directly contain the actual JSON response body but is instead a representation of the entire HTTP response. So, to extract the JSON body content from the Response object, we use the json() method (res.json()), which returns a second promise that resolves with the result of parsing the response body text as JSON.

        If you head over [here](https://api.quotable.io/random) you can see our API endpoint response with a JSON Object which inturn contains keys `content` and `author` having values of actual quote and its author name respectively.

        Later in .then block of fetch api we replace placeholder quote and author with the value we recieved from our API using .innerHTML and javaScript template literals to update DOM Dynamically.

```js
            quote.innerHTML = `"${data.content}"`;
            author.innerHTML = `- ${data.author}`;
```

If you want to learn more about Asyncronous and advanced part of JavaScript you can take up [this](https://codedamn.com/learn/advanced-practical-javascript) course on [codedamn](www.codedamn.com) so that you can gain practical Understanding of advanced concepts like Promises and async-await , Prototypal inheritence objects and common pitfalls , Generators, iterators, DOM manipulation, and more.

0. Kudos 🎊'now you've built yourself a quote generator app.Congratulations and keeping this motivation and confidence learn and build some more stuff / apps using Javascript on any tech stack as a matter of fact over [here](https://codedamn.com/projects)

Don't miss out bonus step!
