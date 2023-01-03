# Get Length of the Playlist (2)

Now, You have figured out the way to get the length. In this Step just code your logic.

If you were unable to make a logic. Let's do it together:

* Store all the video IDs in an array.
* Now, make a http request to the API using axios (This time request will be on other url just keep this in mind).
    * Come up with the url and header.
    * Make a get request.
    * Get the duration of each video from the response.
    * Store the duration of each video in an array.
* Now, you have the duration of each video.

## Hint
For the url, you can get a very good idea from this [documentation](https://developers.google.com/youtube/v3/docs/videos/list) of the API. Just play around in the **"Try this method"** section of the documentation.

## Next Step
Figure out the way to get total duration of the playlist as the duration format is not the common one. **Hint:** You can use `moment.js` for this. See Documentation [here](https://momentjs.com/docs/)


