In this step we will be working on how to make a random room code on clicking the create your “own room” link

## Here are a few pointers on how you can do it to:
- In the frontend, you can make use of any node package like uuid to randomly generate a long string.
- Make sure that this string i.e. room id gets generated once the user clicks on the “own room” link. For better UX, once the user generates a room id, show “success” as a notification, alert or a toast.
- Once the user clicks join the room after entering the room id and username, route them to '/compiler/random-room-code'

The create room part is now complete, but what happens when someone tries to join this room? We’ll handle this in the backend part later on.
