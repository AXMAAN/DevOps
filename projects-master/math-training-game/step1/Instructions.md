In this step your goal is to design the layout of the `Math Training Game`.

It is advised that you go though the [HTML & CSS Fundamentals course](https://codedamn.com/learn/html-css) for a comprehensive and detailed understanding of these tags.

## What will you do?

In this step you are tasked to design the layout like this:

![App Screenshot](https://raw.githubusercontent.com/ritwickrajmakhal/ScreenShots-for-math-training-game/master/sc3.png)

Go to the `index.html` tab and do the following:

1. Create a `div` tag with class `box` within `<main>` tag.

    Sample code:

    ```html
    <!-- start writing your code -->
	<div class="box"></div>
    ```
Note: `div` tag used to create a container.

2. Create a `section` tag with class `sec1` within `.box` element.

    Sample code:

    ```html
    <!-- start writing your code -->
    <div class="box">
        <section class="sec1"></section>
    </div>
    ```
    Note: Previously written code should be same.

3. Create a paragraph tag with the class `instruction` within `.sec1` element and set a text.

    Sample code:
    ```html
    <section class="sec1">
        <p class="instruction">Choose the correct option</p>
    </section>
    ```

4. Create a `div` tag with id `operand1` within `.sec1` element and after `.instruction` element.
    
    Create another `div` tag with id `operator` within `.sec1` element and after `#operand1` element.

    Create another `div` tag with id `operand2` within `.sec1` element and after `#operator` element.

    Sample code:
    ```html
    <div id="operand1">45</div>
	<div id="operator">+</div>
	<div id="operand2">45</div>
    ```
5. You should create another `section` tag with the class `.sec2` within `.box` element and after `.sec1` element.

6. Create a `button` tag with id `option1` within `.sec2` element.
    
    Create another `button` tag with id `option2` within `.sec2` element and after `#option1` element.

    Create another `button` tag with id `option3` within `.sec2` element and after `#option2` element.

    Create another `button` tag with id `option4` within `.sec2` element and after `#option3` element.

    Create another `div` tag with id `msgbox` within `.sec2` element and after `#option4` element.

    Sample code:
    ```html
    <section class="sec2">
		<button id="option1">95</button>
		<button id="option2">85</button>
		<button id="option3">80</button>
		<button id="option4">75</button>
        <div id="msgbox">Result</div>
	</section>
    ```
7. Create an audio tag with id `correctBeep` within `main` tag and after `.box` element.
    
    Set the `src` attribute of `#correctBeep` element to `assets/correct.mp3`.

    Sample code:
    ```html
    <audio id="correctBeep" src="assets/correct.mp3"></audio>
    ```
    Similarly create another audio tag with id `wrongBeep` within `main` tag and after `#correctBeep` element.
    
    Set the `src` attribute of `#wrongBeep` element to `assets/wrong.mp3`.

    Note: Find all the audio files from the `assets` folder.

You have completed the step 1, make sure that everything is working fine. Mark all the steps as complete, and go ahead.