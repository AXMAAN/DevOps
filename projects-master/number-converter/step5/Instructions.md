In this step you will define some more functions for the `Number Converter` project.

If you studied about `Number System` then you possibly know that we can convert from any number system to any number system (except `decimal` number system) using two steps.

These are:

- Convert your number to the corresponding decimal number.
- Now from decimal number you can convert it to any number system in one step.

## What will you do?

Go to the `number_system_module.js` tab and do the following:

1. Complete the function called `bin_to_oct(N)` to convert a binary number to the corresponding octal number using `bin_to_dec(N)` and `dec_to_oct(N)` function which you have already defined in the previous step.

    Sample code:
    ```js
    N = bin_to_dec(N);
    return dec_to_oct(N);
    ```
2. Likewise Complete the function called `bin_to_hex(N)` to convert a binary number to the corresponding hexadecimal number using `bin_to_dec(N)` and `dec_to_hex(N)` function which you have already defined in the previous step.

3. Complete the function called `oct_to_bin(N)` to convert a octal number to the corresponding binary number using `oct_to_dec(N)` and `dec_to_bin(N)` function which you have already defined in the previous step.

4. Complete the function called `oct_to_hex(N)` to convert a octal number to the corresponding hexadecimal number using `oct_to_dec(N)` and `dec_to_hex(N)` function which you have already defined in the previous step.

5. Complete the function called `hex_to_bin(N)` to convert a hexadecimal number to the corresponding binary number using `hex_to_dec(N)` and `dec_to_bin(N)` function which you have already defined in the previous step.

6. Complete the function called `hex_to_oct(N)` to convert a hexadecimal number to the corresponding octal number using `hex_to_dec(N)` and `dec_to_oct(N)` function which you have already defined in the previous step.

If you've done it properly then you will be able to see some message in you console like this.

![App Screenshot](https://raw.githubusercontent.com/ritwickrajmakhal/ScreenShots-for-number-system-using-js/master/sc5.png)

Else you will get some `error message`.