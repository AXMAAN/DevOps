In this step our goal is to design the layout of the converter.

It is advised that you go though the [HTML & CSS Fundamentals course](https://codedamn.com/learn/html-css) for a comprehensive and detailed understanding of these tags.

## What will you do?

In this step you are tasked to design the layout like this:

![App Screenshot](https://raw.githubusercontent.com/ritwickrajmakhal/ScreenShots-for-number-system-using-js/master/sc1.png)

Go to the `index.html` tab and do the following:

1. Add a new `<div> </div>` tag inside the `<main>` and after `<h1>` element. Give the `<div>` element a class `box`, this element will act as a container.

	Sample code:
	```html
	<!-- start writing your code -->
	<div class="box"></div>
	```
2. Now add some style on `.box` class.
You should use the external style sheet for styling, there you will get all the Boilerplate code. Don't worry we have already linked the stylesheet with the html file.

	Here is the sample code for you (you can customize it):
	```css
	.box {
		width: auto;
		height: 55vh;
		background-color: #e6e6e6;
		border-radius: 2rem;
		padding: 3rem;
		text-align: center;
		display: flex;
		flex-wrap: wrap;
		box-shadow: 0 1.2rem 3rem 0.5rem rgba(0, 0, 0, 0.2);
	}
	```
3. Create three `<section></section>` tag with class `sec1`, `sec2`, `sec3` within `.box` element like this:

	Note: You should create all the `<section></section>` tag within `<div class="box"></div>`.
	```html
	<section class="sec1"></section>
	<section class="sec2"></section>
	<section class="sec3"></section>
	```
	4. Now add some style on `sec1` and `sec2` class. As you can see from the screenshot that `.sec1` and `.sec2` both are looking same. So we will add same styling for both the classes like this:
	```css
	.box .sec1, .sec2{
		width: 50%;
		height: 30rem;
		display: flex;
		justify-content: space-around;
		align-items: center;
		flex-direction: column;
	}
	```
5. After that add some style to `sec3` class. All things should be same like `instruction 4`, just change these thing:
	```css
	width: 100%;
	height: 10rem;
	flex-direction: row;
	```
Worrying about the output? Don't worry we will set this in the next step. Go ahead if you followed all the instruction correctly.