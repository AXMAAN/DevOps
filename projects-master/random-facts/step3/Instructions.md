## Goal of the step

- The main aim of this step is to fetch the fact from given API
- You can also add some transitions and animations on your `div` or text.

It is advised that you go though the [JavaScript Fundamentals course](https://codedamn.com/learn/javascript-basics) for a comprehensive and detailed understanding of the fundamentals of JavaScript for this project.

## Things to do

1. Write a function named `fetchFact` to fetch the fact from given endpoint.

    ```js
    function fetchFact{
        fetch('https://api.api-ninjas.com/v1/facts?limit=1', {
        headers: {
            'X-Api-Key': 'Your API key from api-ninjas'
        },
        })
        .then(res => res.json())
        .then(data => {
            const fact = data[0]?.fact
            const para = document.querySelector('p')
            para.innerHTML = fact || "Retry..."
        })
        .catch(err => {
            console.log(err)
        })
    }
    ```
2. Use this function on each click and on loading website for the first time.

    ```js
    function fetchFact{
        // Here limit=1 is set in endpoint to get only one fact at a time, you can set more limit
        fetch('https://api.api-ninjas.com/v1/facts?limit=1', {
        headers: {
            'X-Api-Key': 'Your API key from api-ninjas'
        },
        })
        .then(res => res.json())
        .then(data => {
            const fact = data[0]?.fact

            // Show this fact to the user
            const para = document.querySelector('p')
            para.innerHTML = fact || "Retry..."
        })
        .catch(err => {
            console.log(err)
        })
    }

    // Call this function to load fact for the first time
    fetchFact()

    // Load fact on each click
    const btn = document.querySelector('button')
    btn.addEventListener('click', ()=>{
        fetchFact()
    })
    ```

## Resources
- [JavaScript Fundamentals course](https://codedamn.com/learn/javascript-basics)
- [Get API key here](https://api-ninjas.com/)