In this step you need to connect mongodb to your app and then make models for storing user data and meetup data

## What will you do?

1. Create MongoDB Cluster. You can do this locally or can go for cloud mongoDB Atlas

2. Get the credentials(client id and client sceret) from there and store them in .env file.
   Next.js has built-in support for loading environment variables from .env.local into process.env.
   An example .env.local:

   ```env
    DB_HOST=localhost
    DB_USER=myuser
    DB_PASS=mypassword
   ```

3. Connect the MongoDB to your app. Make a folder dbConnnect.js so that you can always import it whenever needed

   ```javascript
   import mongoose from "mongoose";

   const connection = {};

   async function dbConnect() {
     if (connection.isConnected) return;
     const db = await mongoose.connect(process.env.DB_URL, {
       useNewUrlParser: true,
       useUnifiedTopology: true,
     });
     connection.isConnected = db.connections[0].readyState;
   }

   export default dbConnect;
   ```

4. Make a folder for models and put this model in it. Make a model(schema) for user. So you need to include the following in user schema:-

   ```javascript
   name: string;
   email: string;
   image: string;
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
