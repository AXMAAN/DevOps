In this step, we would work on making a functionality for generating a random invite code on starting a new game.

Here are a few pointers on how you can do it:

-   From frontend, send a POST request to backend on `/api/generate-code` with the structure like:

```json
{
	"requestingUser": "<username>"
}
```

-   On the backend, it could generate a random string that is the roomID as well as the joining code.
-   Backend could create a mapping of roomID as the object key and the joined users as a `string[]` value:

```js
const mapping = {
	'some-random-room-id': ['user1', 'user2']
}
```

-   Whenever someone "joins game" using the same random ID, all you have to is:

```js
mapping[roomID]?.push(userID)
```

-   Finally, once both people join, the endpoint `GET /api/room/:roomid` should return usernames of both the members. You may optionally poll this endpoint every few seconds on game page. (or use websocket to deliver the information)
