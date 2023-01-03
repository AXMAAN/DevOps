In this step you will work with `script.js` file.

## What will you do?
Go to the `script.js` tab and do the following:

1. Create a variable called `input`, this variable should select the `input` id which is present in `index.html`.

    Sample code:
    ```js
    const input = document.querySelector("#input");
    ```
    - `document.querySelector()` is used to select any element from the document (`index.html`).

    Note: `#` is used because you are selecting the ids. If it is a class then you will use `.` operator.

    Likewise create another variable called `output`, this variable should select the `output` id which is present in `index.html`.

    Sample code:
    ```js
    const output = document.querySelector("#output");
    ```
    Likewise create all the variables following the table given bellow (Don't delete the previously created two variables).

    |Variable Name      |Id Name          |
    | :--------         | :-------        |
    | `input_option`    | `input-options` |
    | `output_option`   | `output-options`|
    | `reset_btn`       | `reset`         |
    | `calc_btn`        | `calc`          |
    | `swap_btn`        | `swap`          |

    Note: You should follow this table to create all the variables.

2. Add an event listener to the `RESET` button using `addEventListener(event,callback function)`.

    Sample code:
    ```js
    reset_btn.addEventListener("click", function () {
        
    });
    ```
    `reset_btn` is a variable that actually selects the `RESET` button.

    Within this function set the `input.value` and `output.value` as an empty string (`""`).
    This will help you to clear the input-output screen.

    Also set the `input_option.selectedIndex` and `output_option.selectedIndex` as 0.

    Note: `selectedIndex` refers to the index (starts from 0) of the `<option>` tag present in the `index.html`.

3. Add an event listener to the `SWAP` button using `addEventListener(event,callback function)`.

    Sample code:
    ```js
    swap_btn.addEventListener("click", function () {
        
    });
    ```
    `swap_btn` is a variable that actually selects the `SWAP` button.

    Within this function

    - Create a variable called `temp` store the index of the `<option>` element which user has selected.
    - Set the `input_option.selectedIndex` as `output_option.selectedIndex`.
    - Set the `output_option.selectedIndex` as `temp`.

    Sample code:
    ```js
    let temp = input_option.selectedIndex;
    input_option.selectedIndex = output_option.selectedIndex;
    output_option.selectedIndex = temp;
    ```
    - Likewise you should swap the value present in input field and output field.

    Sample code:
    ```js
    temp = input.value
    input.value = output.value
    output.value = temp
    ```

See you in the next step if you followed all the instruction properly.