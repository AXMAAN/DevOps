In this step you have to add changes in app.js file

- first of all import methods that's created in githubSlices.js
  
- use your github username for default useState method
  
- Get the data from the store by useSelector  
for example: 
const store = useSelector((state) => state?.repos);
 const { loading, reposList, profile, error } = store;
