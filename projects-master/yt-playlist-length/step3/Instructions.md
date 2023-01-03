# Get data from the API (2)

In the previous step, we got the data of the playlist having videos less than or equal to 50. Now, we will get the data of the playlist having videos more than 50.

Again, if you have gone through the [documentation](https://developers.google.com/youtube/v3/docs/playlistItems/list), there you must have seen something known as `pageToken`. This is the key to get the data of the playlist having videos more than 50. Do read about this if you haven't already.

Now we are all set for the next step. Follow the steps below:

* Find a playlist having videos more than 50.
* Extract the playlist ID from the link. This time try to extract the playlist ID from the link using slicing and indexing.
* Now, create a function named `getData` which will take the playlist ID as an argument.
* In this function, make a http request to the API using axios. 
    * Come up with the url and header.
    * Make a get request.
    * Get the data from the response.

Now, you have the data of playlist with 50+ videos. You can use it to get the length of the playlist.

## Hint

Make sure to add `pageToken` in the header of the request. It's up to you what pageToken you want to use `nextPageToken` or `prevPageToken`.

## Next Step

Play around with the data and figure out how to get the length of the playlist.

