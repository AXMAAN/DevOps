In this step, we will fetch and store Weather data using an API.

The `useEffect` hook comes into picture in this step. We will be using `open-metro` API to fetch Weather data.

We will be using the `fetch` function to make a request to the API and get the data.

Source code should look like this:

```
const [coords, setCoords] = useState({latitude: 0,longitude: 0})

useEffect(() => {
		fetch(`https://api.open-meteo.com/v1/forecast?latitude=${coords.latitude}&longitude=${coords.longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=auto`)
		.then(res => res.json())
		.then(data => {
			setWeather(data.daily)
		})
	}, [ coords ])

return (
```

Let us break down the code:

-   `useEffect` takes in a function as an argument. This function is called when the component is mounted. The second argument is an array of dependencies. The function is called only when the dependencies change.
-   In this case, the **dependencies** are `coords`. The function is called only when the `coords` change. Which means, the API is called everytime there is a change in the **coordinates**.
-   Then, inside the function, we make a call to the `Open-metro API`. The API returns a JSON object. We use the `then` function to get the data from the API. The `then` function takes in a function as an argument. This function is called when the API returns the data. The data is passed as an argument to the function. We use the `setWeather` function to set the state of the `weather` variable. The `weather` variable is set to the data returned by the API.

Thus, we have successfully fetched data from an API to our Weather App.
