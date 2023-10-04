In this step you have to fetch repos and profile

 -Use createAsyncThunk function to fetch Repos

Api for the following :

```text

"https://api.github.com/users/${user}/repos?per_page=30&sort=asc"

```

 -Use createAsyncThunk function to fetch Profile

```text

"https://api.github.com/users/${user}"

```

- In last use the createSlice function to create reducer which state mentions :
      - pending
      - fulfilled
      - rejected
