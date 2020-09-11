<h1>Steps to test a PR</h1>

1. Follow instructions in
[README](https://github.com/anitab-org/vms/blob/develop/README.md) to setup the system running locally.

2. Check on Zulip chat if any of the PR's 
[here](https://github.com/anitab-org/vms/labels/Needs%20Testing) are high-priority if the priority is not set already.

3. If the PRs are not prioritized then pick any 1 PR from the list from the link in step 2 to test locally.

4. Go to the Issue that PR is fixing and follow the steps to reproduce that issue while you are under the develop branch.

5. Run the following commands to get to the PR branch, where `<contributor>` is the GitHub username of the contributor that submitted the PR:

```
git clone https://github.com/<contributor>/vms/
git checkout <branch-name>
```

6. Verify the code addition/deletions in the PR.

7. Reproduce the issue and test the fix.

8. Get screenshots/gifs of before and after the fix and attach them to the PR comment.

9. If the testing is unsuccessful and fixes are needed change then remove the label `Status: Needs Testing` and add `Status: Needs Review`.

10. If the testing is successful and no improvements needed then remove the label `Status: Needs Testing` and add `Status: Ready to Merge`.

<h2>Template to report PR testing results</h2>
This template can be used to add a review comment to a PR after testing is done. It can be used irrespective of the success or failure of testing.

```
The changes made in this PR were tested locally. Following are the results:

1. Code review - Done or Not Done

2. All possible responses (positive and negative tests) were tested as below:

  * _Test1 Description_  
    _Screenshot/gif_:  
    _Expected Result_:  
    _Actual Result_:
  * _Test2 Description_  
    _Screenshot/gif_:  
    _Expected Result_:  
    _Actual Result_:  
    ...  
    
3. Additional testcases covered:

  * _Test1 Description_  
    _Screenshot/gif_:  
    _Expected Result_:  
    _Actual Result_:
    
4. Additional Comments:

5. Status of PR Changed to: Needs Review or Ready to Merge.
```
