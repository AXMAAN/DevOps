In this step, we will aim to build a register page on /register path. You will have to work with `localStorage` API to add the registered user to `localStorage` once they register successfully.

## Pointers to note

-   This is how the schema for localStorage could look like:

```json
[
	{
		"username": "admin",
		"password": "123"
	},
	{
		"username": "john",
		"password": "456"
	}
]
```

-   Add basic validation to the registration: Usernames should be unique, alphanumeric only. Passwords should be strong.
