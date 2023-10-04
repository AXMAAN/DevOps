The dashboard should load feed from all the users. This feed should be also stored in localStorage as feed as the localStorage key, and the following structure as the value (feel free to change it to add more features):

```json
[
	{
		"postID": "", // a unique post ID
		"contents": "", // contents of the post
		"postAuthor": "", // username of the author of the post
		"createdOn": 0, // a unix timestamp (stored in seconds) of the time it was created
		"updatedOn": 0 // a unix timestamp (stored in seconds) of time it was updated
	}
]
```

-   Whenever a user creates a new post, it is added into the `localStorage` key feed as an individual post.
-   All posts inside feed `localStorage` should be visible to everyone in random order who create an account and visits `/dashboard`
-   Only the post author should see the option to edit or delete the post.
-   Only the post author can edit and delete the post. Put proper checks in place.
-   Take design inspiration from assets folder, but you have to build the design + logic on your own.
