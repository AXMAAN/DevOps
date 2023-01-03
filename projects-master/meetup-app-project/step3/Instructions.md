In this step you need to build a form for submitting request for adding new meetups and updating them.

## What will you do?

1. Make a component for form so we can reuse it both new meetups and for updating them.

2. Add proper styling and validation. You can Regular Expressions for Validation.

3. There should be proper error messages on error inside UI.You should some popup for it.

4. Form should contains atleast the following field.

   ```
   Meetup Title
   Meetup image
   address
   description
   ```

5. Should store the value of the inputs tag in a variable. In nextjs to do so we uses uesState();

   ```javascript
   import { useRef, useState } from "react";
   const [title, setTitle] = useState(""); // in the function component
   ```

   Check the challenges tabs to know what all you should be implementing. All the best!
