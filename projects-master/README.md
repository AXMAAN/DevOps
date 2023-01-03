# Welcome To Hacktoberfest - Contribute a project and win prizes

This initiative is part of [Codedamn's Hacktoberfest](https://codedamn.com/hacktoberfest)

During Hacktoberfest, submit an interactive project to this repository and get a change to win a Codedamn's T-shirt.

## How to participate? (read carefully)

If you want to watch a step-by-step video on how to contribute, check out this video: [https://www.youtube.com/watch?v=a65Qaycbb0k](https://www.youtube.com/watch?v=a65Qaycbb0k)

In order to participate and win prizes, you have to submit a **guided project**. A guided project is a breakdown of a project into multiple steps for a beginner/intermediate developer to build. These guided projects can be attempted for free from codedamn IDE. Check out this [example guided project](https://codedamn.com/project/multiverse-html5-photo-gallery). Steps on how to do that is below.

### 1. Getting your boilerplate code ready

1. Choose the project that you want to contribute to, it has to be a new project that you have built yourself, and now want to help others.

2. Create a fresh folder structure for your project and keep the **required boilerplate code only**. Make sure to add all the assets related to the project. It is recommended to put all your assets in the `/assets` folder itself.

3. Add a `.cdmrc` file on the top level of your Project. Go through this [documentation](https://teach.codedamn.com/docs/concepts/cdmrc) to setup the `.cdmrc` file.

4. Create a new GitHub repository for the Project and keep the link with you, you'll use it in the next step.

### 2. Creating your Project on Codedamn

1. Fork this repository and clone it into your computer. Open the repository in any text editor.

2. Create a new folder in the project. The name of the folder will be the project slug that will be displayed in the URL. The folder name should not contain any spaces, and should have URL safe characters.

    For Example: `eventually-html5-landing-page` will be hosted at [https://codedamn.com/project/eventually-html5-landing-page](https://codedamn.com/project/eventually-html5-landing-page)

3. Create a `spec.yml` file inside the folder. This is the specification file that contains the metadata regarding the project. This data will be shown in the project landing page.

Here is an example of how the `spec.yml` file should look like, you can use this as a template for creating your own `spec.yml` file.

```yaml
name: Eventually - Stunning HTML5 Landing Page
tags: ['HTML/CSS', 'JavaScript']
starter-files: https://github.com/codedamn-projects/eventually-stunning-html5-landing-page
type: frontend
level: easy
cover-image: https://raw.githubusercontent.com/codedamn-projects/eventually-stunning-html5-landing-page/master/designs/Landing%20Page%20%5BDesktop%5D.jpg
short-description: A simple and minimal landing page built in HTML5 for a pre-launch to collect email addresses. You will learn about background images and building a deployable landing page in this project.
long-description: |
    Your challenge is to build out this landing page and get it looking as close to the design as possible.

    This project focuses mostly on HTML, CSS and layouts with CSS. There's a tiny bit of JS included for the mobile navigation toggle. But you could also choose to do this without JS!

    You can use any tools you like to help you complete this project. So if you've got something you'd like to practice, feel free to give it a go.

    Your users should be able to

    - View the optimal layout for the site depending on their device's screen size

    - See hover states for all interactive elements on the page

    - Download the starter code and go through the README.md file.

    The `README.md` file will provide further details about the project. The `style-guide.html` file is where you'll find colors, fonts, etc.

    Don't forget to share your submissions with the community to get feedback. All the best.

# https://codedamn.com/projects specific section
codedamn:
    helper-learning-path: frontend
    show-community-banner: true
    playground-layout: terminal-editor-browser
    playground-image: html
    guided: true
```

Each field is explained in detail below.

#### Spec.yml file fields

-   **`name`**: The name of the project. This will be displayed in the project landing page.

-   **`tags`**: The tags share the technologies that are used in developing the project.

-   **`starter-files`**: The GitHub repository URL of the starter files. The repository will be forked to a Codedamn Playground, so that the user can start working on the project directly.

-   **`type`** : The type of the project. This will be used to categorize the project. The possible values are `frontend`, `backend`, `fullstack`, `web3`

-   **`level`** : The level of the project determines the difficulty of the project. Possible values are `easy`, `medium`, `hard`

-   `cover-image` : The URL of the cover image of the project, this project will be displayed on the Project Card and on the project landing page.

    Make sure that this image exists in the GitHub Repository of your Project, and only paste the static link generated by GitHub. This link would be similar to `rawgithubusercontent.com/...`. You can refer to the GIF below.

    ![get image raw URL](https://raw.githubusercontent.com/codedamn/projects/hacktoberfest-readme/schemas/assets/Static%20URL%20for%20Image.gif)

-   `short-description` : The short description of the project is a one-liner description that will be displayed in the project card and in the open graph image.

-   `long-description` : The long description of the project will be displayed in the project landing page. This should explain the outcome of the project in brief.

#### Codedamn Object fields in `spec.yml` file

-   `helper-learning-path` : The helper learning path will display the relevant learning path in the project landing page. So if any user is unaware of the technologies used in the project, they can refer to the learning path to learn the technologies.

    Currently only four learning paths are available. `frontend`, `backend`, `fullstack`, `web3`.

    You can find all the details about the learning path [here](https://codedamn.com/learning-paths/)

-   `show-community-banner` : This field is used to show the community banner in the project landing page. This is used to encourage the user to share their project with the community and get help from the community on our [forum](https://codedamn.com/forum/) or our [discord server](https://discord.gg/codedamn)

-   `playground-layout` : This field is used to determine the layout of the playground. The possible values are `terminal-editor-browser`,`terminal-browser`, `terminal-editor`, `terminal`,

    ![playground layouts](https://raw.githubusercontent.com/codedamn/projects/hacktoberfest-readme/schemas/assets/playground-layout.png)

-   `playground-image` : This field is used to determine the docker image that is required to the boot the playground in. The possible values are

    -   `html` - HTML / CSS / JavaScript / React / Next.js / Vue

    -   `ethereum-v1` - Ethereum / Solidity / Web3.js / Truffle

-   `guided` : This boolean field is used to determine if the project is guided-mode or not. If the project is guided, the project should have steps in the project. Possible values are `true` or `false`

### 3. Creating the steps for the project

1. Before getting into the details of implementing the steps, we suggest you to mentally break down the project into small steps and make a note of what each step of the project will look like. This helps you to understand the project better and also helps you to implement the steps in a better way.

2. There is no limit for the number of steps that can be created. For each step will have a separate folder for itself. The name of the folder should be the `step` followed by a number. The step names should go like `step0` , `step1`, `step2` and so on...

3. Each step folder will contain two files inside it. `Instructions.md` (Capital `I` please **do not use small** `i`) and `challenges.yml`. (Small `c`)

    ![guided project playground](https://raw.githubusercontent.com/codedamn/projects/hacktoberfest-readme/schemas/assets/steps%20.jpeg)

4. The `Instructions.md` file will contain the instructions for the step. You can convey the details of what the user is supposed to implement in this step and guide them along with the way the specific details that the user should be aware of.

    Make sure not to include any heading in the `Instructions.md` file as the Step name is already displayed at the top of the Instructions tab.

5. The `challenges.yml` file will contain the challenges for the step. There are the clear cut deliverables that the user should implement in this step. The challenges are used to determine if the user has completed the step or not.

    Here is the example of the `challenges.yml` file.

    ```yaml
    name: 'Make the page responsive'
    stepId: step3
    stepBreakDown:
        - text: 'The landing is responsive on mobile screens'
        - text: 'The landing page is responsive on small to medium sized screens'
        - text: 'The landing is responsive on large screens'
    ```

Each field is explained in detail below.

-   `name` : The name fields is used to determine the name of the step. This will be displayed in the Steps section on the Playground.

-   `stepId`: is used to map the step to the step folder and determine the order of the step folder. Make sure that the `stepId` value matches the folder name that the file is in.

-   `stepBreakDown` : This field contains the list of all the challenges that this step holds. This is an Array of Objects in YAML.

    Each object should have a `text` field that contains the challenge text, this challenge text is visible in the challenges tab in the playground.

The users are supposed to self-assess the challenges themselves before moving to the next steps of the project.So, make sure that the challenges text is clear and concise.

We have covered all the instructions that you need to be aware of as a creator to create your first guided project. You can now start working on the project and get it ready for review.

### 4. Creating a pull request

Now that you have created and work on the guided-project, please create a Pull Request to the **master** branch of the Repository.

## What are my prizes?

If you're based in India:

-   Codedamn Merch Kit (Exclusive codedamn t-shirt + coding stickers)
-   Get a chance to share your story on [codedamn YouTube channel](https://youtube.com/codedamn)

If you're based outside India:

-   Codedamn Pro account for free for 3 months
-   Get a chance to share your story on [codedamn YouTube channel](https://youtube.com/codedamn)

## Reviewing of Project

Once you have created a pull request, the project will be reviewed by the codedamn team. If there are any details that need to be fixed, we'll let you know in the Pull Request messages itself. Make sure to keep an eye on them.

Once your Pull Request gets merged we'll send you a form to fill out the necessary details to ship your swags.
