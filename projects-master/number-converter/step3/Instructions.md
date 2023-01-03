Welcome to the last step of styling part of the `Number Converter` project. In this step you will conclude the styling part.

## What will you do?

In this step you are tasked to design the layout like this:
![App Screenshot](https://raw.githubusercontent.com/ritwickrajmakhal/ScreenShots-for-number-system-using-js/master/sc3.jpg)

Go to the `style.css` tab and do the following:

1. Select the `sec2` class and add `border-left` of `1px solid black`.

2. Select the `<p>` tag and increase the `font-size` by `3rem`.

3. Select the `<input>` and `<select>` tag and give the `padding` of `5px`. Also increase the `font-size` by `1.5rem.`

4. Select the `<button>` tag, give the `padding at top-bottom` of `10px` and at `left-right` of `20px`. Make the `cursor` to be `pointer`.

	Note: You should use the shorthand way to add the padding.

	Sample code:
	```css
	.sec3 button {
		padding: 10px 20px;
		cursor: pointer;
	}
	```
5. Select all the buttons present in `sec3` class and set the `border radius` to be `5px` like this:
	```css
	.box .sec3 * {
		border-radius: 5px;
	}
	```
	Note: Here `*` operator selects all the elements present in `sec3` class.

6. Set the `background-color` of the all the buttons following the id-color reference:
	### Color Reference

	| id name             | Hex                                                                |
	| ----------------- | ------------------------------------------------------------------ |
	| reset | ![#ff3333](https://via.placeholder.com/10/ff3333?text=+) #ff3333 |
	| calc | ![#00cc66](https://via.placeholder.com/10/00cc66?text=+) #00cc66 |
	| swap | ![#cccc00](https://via.placeholder.com/10/cccc00?text=+) #cccc00 |

