In this step, we will use the Browser Geo-location API, to get coordinates.

Source code should look like this:

```
<button className="btn btn-warning" onClick={
	() => {
		navigator.geolocation.getCurrentPosition(function(position) {
			setCoords({
				latitude: position.coords.latitude,
				longitude: position.coords.longitude,
			})
		})
	}
}>Auto-Detect</button>
```

Let us break down the code:

-   We are using the `navigator.geolocation.getCurrentPosition()` method to get the current position of the user. This method takes a callback function as an argument, which is called when the position is successfully retrieved. This callback function takes a `position` object as an argument, which contains the coordinates of the browser.
-   We are using the `setCoords()` method to update the state variable `coords` with the coordinates of the browser.

Thus, we have successfully used Browser Geolocation API for getting coordinates in our Weather App.
