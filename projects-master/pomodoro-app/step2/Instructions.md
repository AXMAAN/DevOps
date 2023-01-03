In this step, we will start working on a simple 25 minute timer. When the start
button is clicked, a 25 minute timer should start, keep updating, and end when
it hits 0:00.

Here are some tips on how you can do it:

- Add a click event listener on the start button to run the main code.
- Store the time remaining in seconds. Start at `25 * 60 = 1500` seconds.
- Use a `setTimeout` with a `1000`ms delay to update the UI every second.
```javascript
function run() {
	  // code
	  if (time > 0) setTimeout(run, 1000);
	  else reset();
}

// ...

setTimeout(run, 1000);
```

- You can convert seconds to minutes with `Math.round(time / 60)` and get the
remaining seconds with `time % 60`
