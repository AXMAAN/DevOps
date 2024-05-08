### **Steps**

- **Add trigger**

  ```yml
  on:
  issues:
    types: [opened]
  ```

- **Add Condition**

  ```yml
  if: github.event.issue.title == 'Add My Name' || github.event.issue.title == 'add my name'
  ```

- **Update data.json**

  ```bash
  node update-data.js --add-username="${{ github.event.issue.user.login }}"
  ```

- **Render new README.md**

  ```bash
  node render-readme.js
  ```

- **Close the issue**

  ```yml
  - name: "Close this issue"
    if: ${{ always() }}
    run: gh issue close $ISSUE --comment "Updated your name on this repo's README.md file!! 🥳🥳"
    env:
      GITHUBTOKEN: ${{ secrets.GITHUBTOKEN }} # This secret is generated by github itself (no need to add in repo's secret again).
      ISSUE: ${{ github.event.issue.htmlurl }}
  ```

- **Note:** you can also create a function which does both the jobs `a. updating data.json`, and also `rendering README.md`