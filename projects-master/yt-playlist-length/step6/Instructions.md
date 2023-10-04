# Get Length of the Playlist (3)

Now, you have the duration of each video.

You can use `moment.js` to convert the duration format to the common one and to get total duration or length of the playlist.

Steps:
* Our duration format is `PT1H2M3S`. To Convert it we have to use `moment.duration` method.
* You have to figure out how you can get total length by using moment.js.
* Also figure out how to get length of the playlist over custom range and do the required changes in the function declaration and other code.

## Hint
For total length, you will find an function in the [documentation](https://momentjs.com/docs/#/durations/).

## Final Code Requirements (Backend)

**In the end, you should have 2 functions `getData(ID)` and   `getLength(videoID, start, end)` where start and end are for custom range. The getLength function should return the length of the playlist.**