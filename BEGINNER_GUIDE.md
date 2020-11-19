## Beginner's Guide

First of all, we welcome you to the open-source contribution.

This guide will help you to make your first contribution to the AnitaB.org.

Read the project's README.md file and get a basic idea of what the project is about.

Read the [Contributing guidelines](https://github.com/anitab-org/vms/blob/develop/CONTRIBUTING.md) and [Reporting guidelines](http://systers.io/reporting-guidelines). These guidelines need to be kept in mind while contributing to any project.

---

### Getting your first issue assigned
Now since you have chosen your project, follow the steps mentioned below to get your first issue assigned.

**Step 1:** Go to the **Issues**  tab of the selected project repository.

![issue_tab](https://user-images.githubusercontent.com/64194946/93016427-b36c8580-f5de-11ea-82ee-57111edad230.png)


**Step 2:** Now, from the list of the issues, search for the issue that you are comfortable working upon. 
We recommend beginners to look for issue with label "First Timers Only" and "Status: Available". You can find them [here](https://github.com/anitab-org/vms/issues?q=is%3Aopen+label%3A%22Status%3A+Available%22++label%3A%22First+Timers+Only%22)

![label](https://user-images.githubusercontent.com/64194946/93048355-4f000380-f67c-11ea-962d-6256888b06f0.png)

**Step 3:** Click on the issue and read the description properly. If you want to work on it, go to the comment section and comment that you want to work on it. One of our volunteers will assign you that issue.

---

### Working on the issue
Now since you have your first issue assigned, we will be discussing some basic steps that need to be followed while working on the issue.

*Steps 1 to 3 are for setup purposes only. You have to follow these steps only once on each project.*

*Steps 4 to 9 should be repeated for every new contribution.*


**Step 1: Forking** 

Fork the main project repository by clicking on the **Fork** button at the top-right.
Forking will create a copy of the repository in your Github account.
![fork](https://user-images.githubusercontent.com/64194946/93016931-570b6500-f5e2-11ea-98fe-f226934091e4.jpg)


**Step 2: Cloning**

*For further steps, you need to have git installed. You can download git from [here](https://git-scm.com/downloads)*

Now since you have git installed, run the following command to clone the repository: 
```
git clone https://github.com/YOUR_GITHUB_USER_NAME/vms
```
*where YOUR_GITHUB_USER_NAME is your Github user name.*


**Step 3: Remote**

First, navigate to your local repository using:
```
cd vms
``` 

The default remote name of the local repository is *origin*. This remote points to the forked repository. But you need to keep track of the main project repository. For this, we need to create a new remote named *upstream*. 

Run the following command to add new remote:
```
git remote add upstream https://github.com/anitab-org/vms
```

Use `git remote -v` to check the current remote. It should show the following output:
```
$ git remote -v
origin  https://github.com/YOUR_GITHUB_USER_NAME/vms (fetch)
origin  https://github.com/YOUR_GITHUB_USER_NAME/vms (push)
upstream        https://github.com/anitab-org/vms.git (fetch)
upstream        https://github.com/anitab-org/vms.git (push)
``` 


**Step 4: Pull latest changes from upstream**

It is pretty obvious that their might be some changes in the main project after you have forked it. Your local repository should be synchronous to the main repository.

For this, you have to pull changes from upstream master branch to your local repository.

Run the following command to pull the latest changes:
```
git pull upstream master
```


**Step 5: Creating new branch**

It is a good practice to a create separate branch for every issue so that it is isolated from the *master* branch.

Use the following command to create a new branch and switch to it:
```
git checkout -b BRANCH_NAME
```

*Try to choose appropriate BRANCH_NAME.*


**Step 6: Solving the issue**

Now you can start working on the issue. You may need to read the installation guide that is specific to every project. For [VMS](https://github.com/anitab-org/vms) project you can check it's [installation guide](https://github.com/anitab-org/vms/blob/develop/aut_docs/Installation_Setup.md).

Make the relevant changes that can fix the issue.

***Stuck?***

Don't worry! We are always here to help you. Go to the comment section of the issue and ask your doubt. Someone will help you out. You can also join our [ AnitaB.org Open Source Zulip](https://anitab-org.zulipchat.com/) channel to discuss any topic. You are recommended to join [vms stream](https://anitab-org.zulipchat.com/#streams/222539/vms) at zulip.

After approval, you must make continuous notes on your progress in the issue while working. If there is not at least one comment every 3 days, the maintainer can reassign the issue.


**Step 7: Commit changes**

*Repeating this step after every significant change in your local repository is a good practice.*

Use ` git add FILE_NAME ` to add file named *FILE_NAME*.

*Here FILE_NAME is the name of the file you made changes to*

Now run the following command to commit all the changes :
```
git commit -m "COMMIT_MESSAGE"
```

*Read [commit message style guide](https://github.com/anitab-org/mentorship-android/wiki/Commit-Message-Style-Guide) for choosing appropriate COMMIT_MESSAGE.*


**Step 8: Push changes to fork**

After making all the changes and committing them, you can push them to your fork.

```
git push origin BRANCH_NAME
```

This will push changes to BRANCH_NAME of remote *origin*.


**Step 9: Create the pull request**

You will see the option of creating a pull request at the fork on Github.

![pull_req](https://user-images.githubusercontent.com/64194946/93018289-452ebf80-f5ec-11ea-81cf-e8f696226a37.png)

Click on "Compare & pull request".

You can now create a new pull request by comparing changes across two branches.

While creating a pull request, you need to follow [pull request template](https://github.com/anitab-org/vms/blob/develop/PULL_REQUEST_TEMPLATE.md).

![createPullReq](https://user-images.githubusercontent.com/64194946/93018539-0a2d8b80-f5ee-11ea-9cbd-74a08249d06f.png)

After filling the required details and comparing the changes you made, click on "Create pull request" button.


### Congratulations! You have successfully created your first pull request.

*Now wait for the reviewers to review your pull request. Do the necessary changes requested by the reviewers. Once your pull request gets approved, it will be merged with the main repository*

### Kudos! You have successfully made your first contribution to AnitaB.org.


