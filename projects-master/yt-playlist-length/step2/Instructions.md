# Get data from the API (1)

Now, You have your API key and you have enabled the YouTube Data API. We will get the data from the API.

Before coming to getting the data, let's create a new file named `.env` in the root directory of the project. In this file, we will store our API key and other sensitive data. 

```
API_KEY=<YOUR_API_KEY>
```
> Make sure to put your API key in place of `<YOUR_API_KEY>` within the quotes (don't forget the quotes).


If you have seen the documentation of the API, then you know that API provide data of only 50 videos at max in a single request. So, In this Step we will only focus on getting the data of playlist having videos less than or equal to 50. 

For that follow the steps below:

* First of all, make sure your server is running and up.
* Then make sure you have axios installed. If not, install it using `npm install axios`.
* Keep the link of the playlist you want to get the data of handy.
* Extract the playlist ID from the link. 
* Now, create a http request to the API using axios. 
    * Come up with the url and the header (Figure this on your own).
    * Make a get request to the url.
    * Get the data from the response.

Now, you have the data. You can use it to get the length of the playlist.

## Hint

For the url, you can get a very good idea from this [documentation](https://developers.google.com/youtube/v3/docs/playlistItems/list) of the API. Just play around in the **"Try this method"** section of the documentation.

## Next Step

Play around with the data and figure out how to get the length of the playlist.