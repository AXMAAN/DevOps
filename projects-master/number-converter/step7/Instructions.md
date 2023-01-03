In this step you will conclude this project.

## What will you do?
Go to the `script.js` tab and do the following:

1. Add an event listener to the `CALCULATE` button using `addEventListener(event,callback function)`.

    Sample code:
    ```js
    calc_btn.addEventListener("click", function () {

    });
    ```
    Note: `calc_btn` is a variable that actually selects the `CALCULATE` button.

2. Complete this callback functions following the given steps bellow.

    - Create a variable called `input_no_system` and store which input option the user has selected.
    - Create a variable called `output_no_system` and store which output option the user has selected.
    - Declare two variable called `ans` and `input_val` which will store some output and take input from the `text-filed` latter.

    Sample code:
    ```js
    let input_no_system = input_option[input_option.selectedIndex].value;
    let output_no_system = output_option[output_option.selectedIndex].value;
    let ans, input_val;
    ```
    Note:

    The `input_option` or `output_option` actually selects the `<select>` tag, so we can access it's child element using the concept of array.

    The `input_option.selectedIndex` or `output_option.selectedIndex` gives an index of which option the user has selected.

3. Now you will be dealing with a bunch of conditional.

    - If the user has selected the same number system as `input` as well as `output`, then set the `input value` to the `output value`.

    Sample code:
    ```js
    if (input_no_system == output_no_system) {
        ans = input.value;
    }
    ```
    - If the user has selected decimal number system as an input-option then user can select

        - Binary
        - Octal
        - Hexadecimal

    as an output-option. For that you need some nested if-else conditionals.

    Something like this:

    ```js
    // Continuation of previous if statement.
    else if (input_no_system == "Decimal") {
        input_val = parseInt(input.value); // Converting String to integer because our expects an integer
        if (output_no_system == "Binary") {
            ans = dec_to_bin(input_val); // Calling proper function and storing correct output in ans variable.
        }
        else if (output_no_system == "Octal") {
            ans = dec_to_oct(input_val);
        }
        else if (output_no_system == "Hexadecimal") {
            ans = dec_to_hex(input_val);
        }
    }
    ```
    In this way you have to write down all the conditionals for the binary, octal and hexadecimal number system.

    A reference table is given that can help to write down all the conditionals.

    ![Table Image](https://raw.githubusercontent.com/ritwickrajmakhal/ScreenShots-for-number-system-using-js/master/sc6.png)

    Note: For `Decimal`, `Binary` and `Octal` to other number system conversion all the functions `needs an integer argument` for that we need a `String-Integer` typecasting before calling the functions, but for `Hexadecimal` to other number system conversion all the functions `needs a string argument` for that we don't need any `String-Integer` typecasting (Sample code given in the next instruction).
4. After that you should display the `ans` in the `output` field. For that just set `output.value` as `ans`.

    Sample code:
    ```js
        // Continuation of previous else if statement.
        else if(input_no_system == "Hexadecimal"){
            input_val = input.value; // No need of String-Integer typecasting
            if (output_no_system == "Decimal") {
                ans = hex_to_dec(input_val);
            }
            else if (output_no_system == "Binary") {
                ans = hex_to_bin(input_val);
            }
            else if (output_no_system == "Octal") {
                ans = hex_to_oct(input_val);
            }
        }
        output.value = ans; // displaying the result
    }); // End of callback function for calc button
    ```
We have completed the project, make sure that everything is working fine. Mark all the steps as complete, and submit the project!

Congratulations, you have come a long way! You have completed the project and learned a lot of new things. Take up the next <a href="https://codedamn.com/projects">project</a> and start building on your own.