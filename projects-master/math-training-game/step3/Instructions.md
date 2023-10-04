Welcome to `step 3`, in this step your goal is to make this game interactive.

## What will you do?
Go to the `script.js` tab and do the following:

Note: We have already linked the `script.js` file with `index.html` file for you.

1. Create a variable called `operand1`, this variable should select the `operand1` id which is present in the `index.html` file.

    Sample code:
    ```js
    const operand1 = document.querySelector("#operand1");
    ```
    - `document.querySelector()` is used to select any element from the document (`index.html`).

    Note: `#` is used because you are selecting the ids. If it is a class then you will use `.` operator.

    Likewise create all the variables following the table given bellow (Don't delete the previously created variable).

    |Variable Name |Id Name       |
    | :--------    | :-------     |
    | `operand2`   | `operand2`   |
    | `operator`   | `operator`   |
    | `option1`    | `option1`    |
    | `option2`    | `option2`    |
    | `option3`    | `option3`    |
    | `option4`    | `option4`    |
    | `msgbox`     | `msgbox`     |
    | `correctBeep`| `correctBeep`|
    | `wrongBeep`  | `wrongBeep`  |
    
    After that declare two variable called `indexOfAns`, `interval`.
    ```js
    let indexOfAns;
    let interval;
    ```

2. Create an array called `options` which you should put all the option variables. i.e, `option1`, `option2`, `option3`, `option4`.
    
    Sample code:
    ```js
    const options = [option1, option2, option3, option4];
    ```

3. Complete the given function called `generateNumber(upper, lower)` which returns a random number in a given range

    - generateNumber(10, 50) should return a number between 11-50 (inclusive)
    - generateNumber(100, 200) should return a number between 101-200 (inclusive)

    Solution:
    ```js
    const generateNumber = (lower, upper) => {
        // Generates a random number which is present in between lower bound and upper bound
        const randomNumber = Math.ceil(Math.random() * (upper - lower)) + lower;
        return randomNumber;
    }
    ```
4. Complete the given function called `generateOperator()` to generate a random arithmetic operator between `'+', '-', '*', '/'`.

    In this function  
    
    - Create an array of arithmetic operators.
    ```js
    const arrayOfOperator = ['+', '-', '*', '/'];
    ```
    - Since we can access an element from an array using indices so, generate a random index number between `-1` to `length of  arrayOfOperator - 1`.
    
    ```js
    let randomNumber = generateNumber(-1, arrayOfOperator.length-1);
    ```
    Note: It will generate random number from `0 to 3` as of now. 
    - Return the random arithmetic operator.
    ```js
    return arrayOfOperator[randomNumber];
    ```
5. Complete the given function called `generateQuestion()` to generate questions in your game following:
    
    - set the `innerHTML` of `operand1` to `generateNumber(-50,50)`.
    - set the `innerHTML` of `operand2` to `generateNumber(-50,50)`.
    - set the `innerHTML` of `operator` to `generateOperator()`.
    ```js
    operand1.innerHTML = generateNumber(-50, 50);
    operand2.innerHTML = generateNumber(-50, 50);
    operator.innerHTML = generateOperator();
    ```
    - Change the background color of all the options buttons to `rgb(77, 62, 71)`.
    - Remove the attribute called `disabled` from all the option buttons.
    ```js
    for(let i=0;i<options.length;i++){
        options[i].setAttribute("style","background-color:rgb(77, 62, 71);");
        options[i].removeAttribute("disabled");
    }
    ```
    Note: `setAttribute()` method adds an attribute to any `html` element and `removeAttribute()` method removes an attribute from any `html` element.

    - set the `innerHTML` of `msgbox` to `Result`.
    ```js
    msgbox.innerHTML = "Result";
    ```
You have completed the step 3, make sure that everything is working fine. Mark all the steps as complete, and go ahead.