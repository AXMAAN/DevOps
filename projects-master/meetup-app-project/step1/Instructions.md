In this step the main goal is to build the frontend for how to show the list of meetups. Onwards we can divide the step according to the backend and frontend so next 3-4 will be for frontend and after that for backend.

## What will you do?

1. Create a dummy javascript array of object of meetup and object should contains following (name : value pairs):

   ```
   {
       title: 'Title for the meetup',
       description: 'Long description of the place',
       image: "image location(url)",
       address: "Address of the place"
   }
   ```

2. Make a Component which will show the above objects.That is loop over the object for each objects in the landing page.Like this

   ```javascript
   dummy.map((object)=> return <Card meetup={object}>)
   ```

3. This component should only show title, image, address and some button like update, delete, show details(it will be covered in step2).
4. For UI you can use materialUI or TailwindCSS or framework you like.

Check the challenges tabs to know what all you should be implementing. All the best!
