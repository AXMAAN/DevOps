In this step, we will construct a form component for adding top and bottom meme text and change the meme image template by clicking the 'Get New Meme' Button.

## Pointers to note

### This is how state variable is declared in React:

```javascript
const [data, setData] = React.useState(/*default state*/)
```
Here default state is the value by which the sate variable data is initialized. The default value can be any data type depending on the use case. It can be an object, a number or a boolean value like true or false.

For Example: Consider a form having two input fields for First Name and Last Name

```javascript
<input 
	type="text"
	placeholder="First Name"
	name="firstname"
	value={meme.firstname}
	onChange={onChange}
/>
<input 
	type="text"
	placeholder="Last Name"
	name="lastname"
	value={meme.lastname}
	onChange={onChange}
/>
```
So the state variable for storing the values inputted in the above fields can be declared as:

```javascript
const [name, setName] = React.useState({
	firstname: "",
	lastname: ""
})
```

### Syntax for declaring a function to update the changes in First Name or Last Name in the name state variable

```javascript
const onChange = (event) => {
	const {name, value} = event.target
	setMeme(prevName => ({
		...prevName,
		[name]: value
	}))
}
```



***Note1: Every input element of any type within the form component need to have a name and a value property assigned using the conventions mentioned above for using the ability of react-controlled form inputs using react states.***

***Note2: For now, we will create a button named "Get New Meme" and add functionality to that button in later steps.***