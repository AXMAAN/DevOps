This is last step of the project and you need to connect backend and frontend of your application and also need to add authorization to every backend and frontend end-points.

## What will you do?

1. Make API calls using axios/fetch. So need to done whenever your making a API call for updating, storing and deleting the data from mongoDB. It can de like

   ```javascript
   async function updateMeetupHandler(enteredMeetupData) {
     await fetch("/api/update-meetup", {
       method: "PUT",
       body: JSON.stringify(enteredMeetupData),
       headers: {
         "Content-Type": "application/json",
       },
     });
     router.push("/");
   }
   ```

2. Make API calls using getStaticProps.So it can used in place where you need to retire data and that data doesn't changes often. So this app you can it in showing detailed page for every single meetups

   ```javascript
   export async function getStaticProps(context) {
     // fetch data for a single meetup
     const meetupId = context.params.meetupId;
     dbConnect();

     const selectedMeetup = await meetupModel.findById(meetupId);
     const creatorUser = await userModel.findById(selectedMeetup.createdBy);

     if (!selectedMeetup && !creatorUser)
       return {
         redirect: {
           //Error page
           destination: `/blog/dfds`,
         },
       };

     return {
       props: {
         meetupData: {
           id: selectedMeetup._id.toString(),
           title: selectedMeetup.title,
           address: selectedMeetup.address,
           image: selectedMeetup.image,
           description: selectedMeetup.description,
           createdBy: creatorUser ? creatorUser.name : "unknown",
         },
       },
     };
   }
   ```

3. Make API calls using getServerSideProps. So it can used in place where you need to retire data and that data changes. It can done as above

4. Add authorization to every backend and frontend end-points. It can be done by using seesion or token's. So I will give the example of session.
   For Frontend pages it can be like this:-

   ```javascript
   import { getSession, useSession } from "next-auth/react";
   //Inside function Component
   const { data: session } = useSession();

   if (!session)
     return (
       <div>
         <h2>You are not authorised to this </h2>
         <p>To see this </p>
         <Link href="/api/auth/signin">
           <a
             onClick={(e) => {
               e.preventDefault();
               signIn();
             }}
           >
             Signin
           </a>
         </Link>
       </div>
     );
   ```

   For backend in getStaticProprs or getServerSideProps

   ```javascript
   const session = await getSession(context); //api folder use getSession({req});
   if (session === undefined || !session)
     return {
       redirect: {
         destination: `/`,
       },
     };
   ```

5. Make a model(schema) for user. So you need to include the following in user schema:-
   ```javascript
   title: string;
   address: string;
   description: string;
   image: string;
   createdBy: Schema.Types.ObjectId;
   createAt: Time;
   ```

Check the challenges tabs to know what all you should be implementing. All the best!

We have completed the project, make sure that everything is working fine. Mark all the steps as complete, and submit the project!

Congratulations, you have come a long way! You have completed the project and learned a lot of new things. Take up the next [project](https://codedamn.com/projects) and start building on your own.
