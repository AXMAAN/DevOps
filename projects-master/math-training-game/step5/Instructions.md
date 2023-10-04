You have just completed the `generateAnswer()` function definition.
In this step you're going to conclude this `Math Training Game` project.

## What will you do?
Go to the `script.js` tab and do the following:

1. Create a loop which will traverse all the option buttons and adds an event listener with the event name `click`.
    ```js
    for(let i=0;i<options.length;i++){ // outer for loop
        options[i].addEventListener("click",function(){ // callback function

        });
    }
    ```
2. Create another loop within the callback function that you have recently created.
    ```js
    for(let j=0;j<options.length;j++){

    }
    ```
    - Within the for loop check whether `j` is equal to `indexOfAns` or not.

        If `j is equal` to the `indexOfAns` means the jth option contains the correct answer. So set the `background color` of the `jth option button` as `green`.
    ```js
    if(j==indexOfAns){
        options[j].setAttribute("style","background-color:green;");
    }
    ```
    Else jth option will contain the wrong answer. So set the `background color` of the `jth option button` as `red`.
    ```js
    else{
        options[j].setAttribute("style","background-color:red;");
    }
    ```
3. Within the callback function disable all the option buttons.
    ```js
    options[j].setAttribute("disabled","true");
    ```
4. Now get out of the `inner for loop` and within the `callback function` check whether `i is equal` to `indexOfAns` or not.
    
    - If `i is equal to indexOfAns` means user has pressed `ith option button` and it contains the `correct answer`. So set the text of `msgbox` as `Correct answer` and play the `correctBeep`.
    ```js
    if(i==indexOfAns){
        msgbox.innerHTML = "Correct Answer";
        correctBeep.play();
    }
    ```
    - Else `i is not equal to indexOfAns` means user pressed `ith option button` and it contains the `wrong answer`. So set the text of `msgbox` as `Wrong answer` and play the `wrongBeep`.
    ```js
    else{
        msgbox.innerHTML = "Wrong Answer";
        wrongBeep.play();
    }
5. Now create an interval which will call the `generateAnswer()` function with time interval of 5sec (5000 millisecond).
    ```js
            interval = setInterval(generateAnswer,5000);
        }); // End of call back function.
    } // End of outer for loop
    ```
6. After that get out of the `callback function` and the `outer for loop`.
    
    - Call the function called `generateAnswer()`.

We have completed the project, make sure that everything is working fine. Mark all the steps as complete, and submit the project!

Congratulations, you have come a long way! You have completed the project and learned a lot of new things. Take up the next <a href="https://codedamn.com/projects">project</a> and start building on your own.