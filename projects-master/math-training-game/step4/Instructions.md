In this step you're going to define the `generateAnswer()` function.

## What will you do?
Go to the `script.js` tab and do the following:

1. You should complete the `generateAnswer()` function following the steps bellow:
    
    - Call the `generateQuestion()` function in side `generateAnswer()` function to generate the question first.
    ```js
    const generateAnswer = () => {
        generateQuestion();
    }
    ```
2. Create some local variables within this `generateAnswer()` function.
    - Create a local variable called `a` which will hold the integer value of `operand1`.
    ```js
    let a = parseInt(operand1.innerHTML);
    ```
    - Create a local variable called `b` which will hold the integer value of `operand2`.
    ```js
    let b = parseInt(operand2.innerHTML);
    ```
    - Create a local variable called `op` which will hold the `operator`.
    ```js
    let op = operator.innerHTML;
    ```
    - Declare a variable called `ans` which will hold the answer of the arithmetic expression.
    ```js
    let ans = eval(a+op+b);
    ```
    Note: `eval` function takes a javascript expression as a string and evaluates it.
3. Since we are working with the array of options we can randomly select that in which `option button` the actual answer will store.
    
    Like this:

    ![App Screenshot](https://raw.githubusercontent.com/ritwickrajmakhal/ScreenShots-for-math-training-game/master/sc5.png)
    
    For that generate a random number between `0-3` and store it to `indexOfAns` that we have already declared.
    ```js
    indexOfAns = generateNumber(0,options.length)-1;
    ```
    - Create a loop which will visit all the `option` and set all the answers.
    ```js
    for(let i=0;i<options.length;i++){
        // Sets all the correct and wrong options.
    }
    ```
    - Within this for loop just check whether `i` `is not equal to` `indexOfAns` means the index of wrong options.
    ```js
    if(i!=indexOfAns){ // Outer if
        // Sets all the wrong options
    ```
    - Within this `if condition` add one more if condition to check whether the `operator` is `/` or not. If yes then generate a random number between `ans` to `ans+50` and take up to `2nd precision`.
    ```js
        if(op == '/'){ // nested if
            options[i].innerHTML = generateNumber(ans,ans+50).toFixed(2); // It generates floating point numbers as a wrong option.
        }
    ```
    - If the operator is not `/` then generate a random number between `ans` to `ans+50`.
    ```js
        else{ // nested else
            options[i].innerHTML = generateNumber(ans,ans+50); // It generates integer numbers as a wrong option.
        }
    } // Outer if ends here
    ```
    - Similarly within the outer else block set the correct option.
    ```js
    else{
        // Sets the correct option.
        if(op == '/'){
            options[i].innerHTML = ans.toFixed(2);
        }
        else{
            options[i].innerHTML = ans;
        }
    }
    ``` 
    Note: You should write all the given conditionals within the `for loop`.  
4. After writing for loop, you should clear an interval called `interval` using `clearInterval()` function. 
    ```js
    clearInterval(interval);
    ```
    Note: You will define this `interval` latter in the next step.

This completes the `generateAnswer()` function definition.

You have completed the step 4, make sure that everything is working fine. Mark all the steps as complete, and go ahead.