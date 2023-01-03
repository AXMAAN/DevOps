Hello everyone! Welcome to the first step of building a collborative code editor.
We will start by building the UI first and then switch between backend and frontend.

## Instructions for this step:
This page will be your landing page, shown on the '/' route. You can start by breaking down the project structure into two parts, client and server (This has already been implemented in the starter files to get you started easily).
Work only on the client folder in this step.

You can build homepage UI as shown

## Few pointers to let you headstart:
- clicking on create your “own room” link will create a random room code. We will be working on this in the next step.
- one person creates a room.
- others (more than 1) can join the room.
- Add one field for room id.
- Add another field for username.
- Clicking on join button would take the user to the compiler page that we will be designing and implementing in the later steps
- Make sure that you do not allow the user to route to the compiler page without either the room id or the username. This implies that the room id and username fields are NECESSARY for routing to the compiler page.
- you can show the errors as a notification, alert, or using react toast. P.S: You can use react-hot-toast package for showing notifications

![](https://raw.githubusercontent.com/oneknucklehead/collaborative-editor/main/designs/Landing%20homepage%20%5BDesktop%5D.jpg)
