In this step, we will render the stored data on Weather App.

The data that we fetched from the API is stored in the `weather` variable. We will use this variable to render the data on the screen. The data is present in the form of object containing multiple objects with arrays of 7 days. We will use the `map` function to render the data.

Source code should look like this:

```
<div className="row">
	{[0, 1, 2, 3, 4, 5, 6].map(day => (
		<div key={day} className="col-3">
			<div className="card my-3">
				<div className="card-body">
					<h3 className="card-title text-primary">{weather?.time[day]}</h3>
					<div className="card-text">
						<h5 className="text-info">
						<i className={`wi ${weatherCodeMapping[weather?.weathercode[day]]?.icon}`}></i> {weatherCodeMapping[weather?.weathercode[day]]?.weather}
						</h5>
						<table className="table table-bordered">
							<thead>
								<tr className="table-dark">
									<th colSpan={2}>Temperature</th>
								</tr>
								<tr>
									<th className="table-success">Min</th>
									<th className="table-danger">Max</th>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td className="text-success">{weather?.temperature_2m_min[day]}°C</td>
									<td className="text-danger">{weather?.temperature_2m_max[day]}°C</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</div>
	))}
</div>
```

Let us break down the code:

-   Firstly, we need to import the `weatherCodeMapping` object from the `weatherCodeMapping.js` file. To do so, add `import { weatherCodeMapping } from "./weatherCodeMapping"` at the top of the source code
-   `[0, 1, 2, 3, 4, 5, 6].map(day => (` is to basically iterate over the array `[0, 1, 2, 3, 4, 5, 6]` that is needed since we have objects containing arrays of 7 days, as mentioned earlier.
-   The `key={day}` prop is added, since we are using the `map` function. This is to avoid the `key` warning.
-   `weather?.time[day]` is used to render the Dates. The `weather` variable is the object that we fetched from the API. The `time` is the key of the object that contains the Date. The `[day]` is used to access the array of 7 days. The `day` is the variable that we are iterating over in the `map` function. `?` is called the <i>optional chaining operator</i>. It is required, because initially, we have our `weather` variable as null. So as long as the data isn't fetched into it (and since fetch is asynchronous), we cannot use attributes inside it (since there are none), and using it will throw an error.
-   `{weatherCodeMapping[weather?.weathercode[day]]?.weather}`, `{weather?.temperature_2m_min[day]}` and `{weather?.temperature_2m_max[day]}` are similar as of above
-   Finally, incase of `` className={`wi ${weatherCodeMapping[weather?.weathercode[day]]?.icon}`} ``, we are using the `weatherCodeMapping`object that we imported from the`weatherCodeMapping.js`file. This object contains the weather code and the corresponding icon. We are using the`weathercode`key of the`weather` object to access the weather code.`weatherCodeMapping[weather?.weathercode[day]]`will return the object containing the weather code and the corresponding icon.`weatherCodeMapping[weather?.weathercode[day]]?.icon` will return the icon.

Thus, we have successfully rendered data to our Weather App.
