##### We want to create a branch to work on so that our local changes will not affect the master.

##### 1. Before creating a new branch pull the changes from upstream, your master needs to be up to date.
```
git pull origin master
```

##### 2. Create new branch on your local machine
```
git branch <branch_name>
```
##### 3. Switch to new branch
```
git checkout <branch_name>
```
##### 4. Publish your new branch to github
```
git push origin <branch_name>
```
This means you push your local branch branch_name to create your remote branch origin/branch_name. Your local branch branch_name is now tracking your remote branch origin/branch_name.
So other people can see your branch.

##### 5. Remember to make sure you are in your branch before you make changes locally
```
git branch
```
Will show all branches.
##### 6. Make some changes to your new branch
```
git add files
git commit -m "changes something"
```
##### 7. Push to your branch
```
git push origin <branch_name>
```
You push your local branch branch_name to your remote branch origin/branch_name. So, your remote branch origin/branch_name is updated
##### 8. Now to merge master into your branch
```
git pull origin master
```
This merges your remote branch origin/master into your local branch you most recently checkedout (which is assumed to be branch_name). Solve conflict if there is any. After this, you have merged remote origin/master branch into your local branch_name branch. 
##### 9. After you solved conflicts push to your branch again
```
git push origin <branch_name>
```
You push your local branch_name to your remote origin/branch_name, so your remote origin/branch_name branch is updated.
##### 10. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/)
* On [GitHub](https://github.com/cse103/Webwork_AdaptiveHints), navigate to the repository from which you'd like to propose changes.

* In the "Branch" menu, choose the branch that contains your commits.

* To the left of the "Branch" menu, click the green ""Compare and Review" button.

* The Compare page will automatically select the base and compare branches.

* On the Compare page, click "Create pull request".

* Type a title and description for your pull request.

* Click Create pull request.

##### 11. Ask someone to review the pull request and to merge your branch into master.

##### 12. The following are steps for pull request on Github Desktop App
##### How to do pull request

* Sync on your own branch
* Switch to master branch
* Sync on master branch
* Switch back to your own brach
* Update from master
* Sync on your own branch
* Pull Request
* Click link to see your pull request
* Scroll down to see merge button
* If the merge button is green, merge your pull request
