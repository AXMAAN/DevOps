In this step, we will take user input for coordinates.

Adding user input for coordinates will dynamically fetch weather data for the coordinates entered by the user.

#### Please carry out the following steps:

1. `input` tags expect a `value` attribute to be passed to them. This value is the default value that is displayed in the input box. Let us set the default value to be `coords.latitude` and `coords.longitude` that we already have in our state variable `coords` for latitude and longitude, respectively.
2. We can set them so, by adding `value={coords.latitude}` and `value={coords.longitude}` to the `input` tags, having `placeholder="Latitude"` and `placeholder="Longitude"`, respectively.
3. We also need to add `onChange` handlers for both of the tags, so the values can be updated in the state variable `coords` when the user enters a new value. We can do this by adding `onChange={e => setCoords({ ...coords, latitude: e.target.value })}` and `onChange={e => setCoords({ ...coords, longitude: e.target.value })}` to the `input` tags, having `placeholder="Latitude"` and `placeholder="Longitude"`, respectively.

Thus, we have successfully taken user input for getting coordinates in our Weather App.
