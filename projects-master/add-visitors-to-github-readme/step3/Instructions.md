#### **Steps**

- **Create a Github token to push your code**
  1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
  2. Click `Generate new token.`
  3. Set a name `Codedamn's playground.`
  4. Give the `repo` scope (that will be sufficient).

- **Create a remote repository**
  
    - Visit [Github](https://github.com)
    - Click on `+` icon on top right corner and click on `New repository` in the drop down menu.
    - Set a repository name and click on `Create repository` button.
    - Copy the repository URL and paste it in the `git remote add origin <repo-url>` command.

- **Initialize Git**

  ```bash
  git init
  ```

- **Set Global Git Configuration**

  ```bash
  git config --global user.name "Your name" # Not username
  git config --global user.email "your-email@example.com"
  ```

- **Add all the files (what you want to push)**

  ```bash
  git add .
  ```

- **Commit files**

  ```bash
  git commit -m "My cool project is ready..!!"
  ```

- **Make a default branch (main)**

  ```bash
  git branch -M main
  ```

- **Add repo's origin**

  ```bash
  git remote add origin https://github.com/your-user-name/your-repo-name.git
  ```

- **Push the code.**

  ```bash
  git push -u origin main
  ```

  - Then you'll be promoted to give `username` and `password`.
  - for `password` you've to give `token` that you generated.



## **Congratulations 🥳🥳**
