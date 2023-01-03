In this step, we will use fetch() API and async-await to fetch memes data from the Imgflip API and select a random image URL from the fetched data for the meme image template.


## API Endpoint and Imgflip API

It gets an array of popular memes that may be captioned with this API. It returns 100 memes ordered by how many times they were captioned in the last 30 days.
- URL/Endpoint: https://api.imgflip.com/get_memes
- Method: GET

## Pointers to note

### How to fetch the data from API. For the data, we have used the API endpoint from:

[Read Here](https://codedamn.com/news/reactjs/reactjs-fetch-api-example) to know more about the syntax and usage of fetch API

### This is how state variable is declared in React:

```javascript
const [data, setData] = React.useState(/*default state*/)
```
Here default state is the value by which the sate variable data is initialized. The default value can be any data type depending on the use case. It can be an object, a number or a boolean value like true or false.

### Generating a given value from a range of values

```javascript
Math.floor(Math.random() * (max - min + 1)) + min
```
In the above code snippet, the max value represents the maximum value of the expected range, and the minimum value represents the minimum value of the expected range