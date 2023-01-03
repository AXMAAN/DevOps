In this step the main goal to add some content and build the HTML structure for the Number Converter project.

As of now you have already builded the layout structure for the `Number Converter` project.

## What will you do?

In this step you are tasked to design the layout like this:

![App Screenshot](https://raw.githubusercontent.com/ritwickrajmakhal/ScreenShots-for-number-system-using-js/master/sc2.png)

Go to the `index.html` tab and do the following:

1. Create a `<p>From:</p>` element within `sec1` class, like this:
	```html
	<section class="sec1">
		<p>From:</p>
	</section>
	```
	Likewise create another `<p>To:</p>` element within `sec2` class.

2. Create a `<input type="text" id="input">` element within `sec1` class and after `<p>From:</p>` element.

    Likewise create another `<input type="text" id="output" disabled>` element within `sec2` class and after `<p>To:</p>` element.

   Note: You should `disable` the input filed of `sec2` class.

3. Create a dropdown list using `<select>` tag within `sec1` class and after `<input type="text" id="input">` element.

	Sample code:

	```html
	<select id="input-options">
		<option value="Decimal" selected>Decimal</option>
		<option value="Binary">Binary</option>
		<option value="Octal">Octal</option>
		<option value="Hexadecimal">Hexadecimal</option>
	</select>
	```
	Note: You should set the first `<option>` of each `<select>` tag as `selected`.

	Likewise create another dropdown list within `sec2` class and after `<input type="text" id="output" disabled>` element.

	Note: You should give an `id="id="output-options"` of the `<select>` tag present in `sec2` class.

4. Create three `<button>` tag within `sec3` class with an id called:
	- `id="reset"`
	- `id="calc"`
	- `id="swap"`

	and give appropriate value to each button.
	Like this:

	```html
	<button id="reset">RESET</button>
	<button id="calc">CALCULATE</button>
	<button id="swap">SWAP</button>
	```

See you in the next step if you followed all the instructions correctly.