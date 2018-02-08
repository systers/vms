# Contribution Guide

The VMS project is always looking for more contributors like you! Before you begin however, you should install and get the project running. Click [here](https://github.com/systers/vms/blob/master/docs/Installation%20Guide.md#installation-guide) for the installation guide. Always make sure that you are working with the latest version of the project, as your concerns may have already been addressed. Remember that coding is not the only method of contributing. You can help with documentation, QA, user interface, and much more!

## Reporting bugs

In order to report bugs, you should create a [new issue](https://github.com/systers/vms/issues/new) on GitHub, and include as many of the following as you can:

* Detailed description of bug

* Expected results versus actual results

* Reproduction steps

* Screenshots

* Any other information that you see fit



## Reporting issues

In order to report issues, you should create a [new issue](https://github.com/systers/vms/issues/new) on GitHub, and include as many of the following as you can:

* Detailed description of issue

* Suggestions to fix issue

* Location of issue

* Screenshots

* Any other information that you see fit



## Suggesting features

In order to suggest a feature, you should create a [new issue](https://github.com/systers/vms/issues/new) on GitHub. It may seem strange that feature suggestions go there, but that is just how GitHub is organized! Try to include as many of the following as you can:

* Detailed description of features you want implemented

* How you want the features to be implemented

* Why you feel these changes are worthwhile

* If applicable, sample examples or designs to help visualize

* Any other information that you see fit.



##Creating pull requests

If you find there is a bug/issue/feature in the [issue list](https://github.com/systers/vms/issues) that you want to tackle, just clone the VMS repository and make the necessary changes. If you have a working solution, push your changes to your forked VMS repository, and then make a [pull request](https://github.com/systers/vms/compare). Please try to push ONLY the relevant changes, which also means you will only need to add one new commit. Please create a separate branch for each issue you solve and follow the commit guidelines below for creating pull requests.



## Writing good commits

A good commit is atomic. It should describe one change and not more.
A good commit message consits of 3 parts:

* shortlog - This should describe the change - the action being done in the commit in not more than 50 characters and in imperative present tense.

* commit message - This should describe the reasoning for your changes. This is especially important for complex changes that are not self explanatory and can be ignored otherwise. Limit the subject line to 72 characters. 

* issue reference - This should use `Fixes` keyword if your commit fixes a bug or typo, or `Closes` if it adds a feature/enhancement and a full URL to the issue.

Example of a good commit:

	Example 1 (Add feature)
	shifts_views.py: Log shift hours

	This allows the volunteers to log shift hours
	only after the shift date has expired and displays
	proper message otherwise.

	Closes #502

	Example 2 (Fix typo)
	Getting_Help.md: Fix docstring typo

	wether --> whether.

	Fixes #101

## Editing commit messages

If you have previously made a commit and update it on a later date, it is advisable to also update the commit message accordingly.

If you need to modify your code, you can simply edit it again, add it and commit it using:

`$ git commit -a --amend`

This will edit your last commit message.


For more information on push and pull requests [click here](http://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/)

For more information on how to write a good commit [click here](http://chris.beams.io/posts/git-commit/).


**Note:** You should only focus on ONE thing in your bug/issue/feature/pull request submission. If you have more things to contribute, fantastic! Just make a new submission for each.
