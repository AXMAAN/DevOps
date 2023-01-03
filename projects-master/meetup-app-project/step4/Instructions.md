In this step you need to build a sigupu google and facebook oauth

## What will you do?

1. Creating Project in Google Developer Console by going to https://console.cloud.google/

2. Get the credentials(client id and client sceret) from there and store them in .env file.
   Next.js has built-in support for loading environment variables from .env.local into process.env.
   An example .env.local:

   ```env
    DB_HOST=localhost
    DB_USER=myuser
    DB_PASS=mypassword
   ```

3. Do same for facebaook also

4. Implement the config.js.This will contains the code for oauth.

5. If you are using NextAuth for implementing oauth then create a file /pages/auth/[...nextauth].js

   ```javascript
   import NextAuth from "next-auth";
   import GoogleProvider from "next-auth/providers/google";

   export default NextAuth({
     providers: [
       GoogleProvider({
         clientId: process.env.GOOGLE_ID,
         clientSecret: process.env.GOOGLE_SECRET,
       }),
     ],
   });
   ```

6. You need to store the data of the user in database which will see in next step

Check the challenges tabs to know what all you should be implementing. All the best!
