In this step, we will get familiar with React Hooks and how to use them in our application.

React Hooks are simple JavaScript functions that we can use to isolate the reusable part from a functional component. Hooks can be stateful and can manage side-effects.

We will be using the following hooks in this step:

1. `useState` - This hook is used to create a state variable and a function to update it.
2. `useEffect` - This hook is used to perform side-effects in a functional component.

### Please carry out the following steps:

1. Firstly, we need to import these _hooks_ in order to use them. Add the following right at the top of our source code: `import { useState, useEffect } from "react"`
2. We need to store 2 variables: `weather` (to store weather data from API) and `coords` (to store coordinates for fetching weather data).
3. We can create 2 state variables for storing the same: `const [weather, setWeather] = useState(null)` and `const [coords, setCoords] = useState({latitude: 0,longitude: 0})`. `useState` takes 1 argument, which is the initial value. We are setting initial value of `weather` as `null` because we are anyway going to fetch it from an API and replace it. Whereas, we are setting initial value of `coords` as a dictionary (object) with keys `latitude` and `longitude`, with both values as `0`, since we need to store _latitude_ and _longitude_ in it, and setting both to `0` gives us some default values, to begin the "fetch" operation with, which we will do later.
4. The `useEffect` hook is used to perform side-effects in a functional component. It takes 2 arguments: a function and an array of dependencies. The function is executed after every render of the component. The array of dependencies is used to specify when the function should be executed. If the array is empty, the function is executed only once, after the first render. If the array contains a variable, the function is executed after every render, and also after every change of the variable. We will use this hook to fetch weather data from an API, in the next step.

Thus, we got a basic idea of React Hooks.
