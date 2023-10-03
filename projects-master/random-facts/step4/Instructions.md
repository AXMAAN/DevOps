## Goal of the step

- The main aim of this step is to add some sound effect
- This step is optional, you can skip this if you want

It is advised that you go though the [JavaScript Fundamentals course](https://codedamn.com/learn/javascript-basics) for a comprehensive and detailed understanding of the fundamentals of JavaScript for this project.

## Things to do

1. Write a function named `wow` to apply sound effect but before this, download some good sound effect and add to `assets` folder. Sample sound is added in the assets folder named `sound.mp3`

    ```js
    function wow() {
        var snd = new Audio('./assets/sound.mp3')
        snd.play();
    }
    ```
2. Use this function after fetching data.

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

            // Applying sound
            wow()
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

## Congratulations
Congratulations, you have successfully applied your HTML, CSS and JavaScript fundamentals to this project. Hope you learnt some new concepts and enjoyed the project.

## Resources
- [JavaScript Fundamentals course](https://codedamn.com/learn/javascript-basics)