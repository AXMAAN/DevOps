Hey, welcome to the step 4 of Number converter project.

In this step you will define some elementary functions which will help you to convert a `decimal number system` to `any number system` and as well as `any number system` to `decimal number system`.

Note: If you don't know about `Number system conversion` just google it and check out.

## What will you do?

Go to the `number_system_module.js` tab and do the following:

1. Convert a decimal number to binary number using `toString(Radix)` method.

    - Radix => Base of the number (Here 2, Since we are converting from `decimal to binary`)

    Sample code: 
    ```js
    let ans = N.toString(2);
    ```
    Note: Don't forget to `return` the `ans`.

2. Now do the reverse thing (`binary to decimal`) but! but! but! using `parseInt(Number,Radix)` method.
Here `radix = 2` and `Number = N`.

    - `Home Task` => Why we can't use the `toString` method to convert binary to decimal?

    Note: Don't forget to `return` the `ans`.

3. Convert the `decimal number to octal number` following the procedure given below:

    - Take the number `N`.
    - Divide `N` by `8`.
    - Store the remainder.
    - Repeat the last two steps until the number can be divided.
    - reverse the sequence of remainder.
    - return the reversed sequence.

    Getting stuck? Here is the sample code for you:
    ```js
    let oct = 0;
    let i = 0;
    while (N != 0) {
        oct += (N % 8) * Math.pow(10, i); // storing and reversing the remainder sequence
        N = parseInt(N / 8);
        i++;
    }
    return oct;
    ```
4. Now do the reverse thing (`octal to decimal`) by using `parseInt(Number,Radix)` method.

    Note: Here `Number = N` and `Radix = 8` (Since we are dealing with octal number).

    5. Convert the `decimal number to hexadecimal number`following the procedure given below.

    - Take the number `N`.
    - Divide `N` by `16`.
    - Store the remainder.
    - If remainder is in between 10-15 (both inclusive) then store remainder following the table:

    | Remainder | in hex   |
    | :-------- | :------- |
    | `10`      | `A`      |
    | `11`      | `B`      |
    | `12`      | `C`      |
    | `13`      | `D`      |
    | `14`      | `E`      |
    | `15`      | `F`      |
    
    - Repeat the last two steps until the number can be divided.
    - reverse the sequence of remainder.
    - return the reversed sequence.

    Getting stuck? Here is the sample code for you:

    ```js
    let hex = "";
    while (N != 0) {
        let rem = N % 16
        switch (rem) {
            case 10:
                hex += "A";
                break;
            case 11:
                hex += "B";
                break;
            case 12:
                hex += "C";
                break;
            case 13:
                hex += "D";
                break;
            case 14:
                hex += "E";
                break;
            case 15:
                hex += "F";
                break;
            default:
                hex += rem.toString();
                break;
        }
        N = parseInt(N / 16);
    }
    return hex.split("").reverse().join(""); // reversing the remainder sequence and return
    ```
6. Now do the reverse thing (`hexadecimal to decimal`) by using `parseInt(Number,Radix)` method.

    Note: Here `Number = N` and `Radix = 16` (Since we are dealing with hexadecimal number).

    If you followed all the instruction properly then you will be able see some output in your console like this:

    ![App Screenshot](https://raw.githubusercontent.com/ritwickrajmakhal/ScreenShots-for-number-system-using-js/master/sc4.png)

    Don't worry about this error you will fix it in the next step.