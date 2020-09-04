## Integrating black and flake8 as pre-commit hook

Black and flake8 are two of the most important code formatters. This ensures that every code is well formatted and organized.

### Setting up the pre-commit hook
##### What does this pre-commit hook do ?
This pre-commit hook ensures that the code is well formatted before a commit is made.

##### Steps to run this pre-commit hook
1. Update your local, cloned repository
```bash
$ git pull upstream <branch-name>
```
2. Move the file named : ```pre-push``` to ```.git``` folder.
3. Install the git hook
```bash
$ pre-commit install
```
###### NOTE: In case you do not have pre-commit,you can simply pip install it and then run step 2.
```bash
pip install pre-commit
```
4. Now stage your changes and commit them. You will see that the checks will run automatically.
5. If you check the status, you will the code related files have been modified automatically.
```bash
$ git status
```
If you go and check the files on your local machine/editor, you will see that the code has been formatted.
6. Stage the modified files and follow the normal steps for generating a pull request.
```bash
$ git add <file-name>
...
$ git commit -m "<commit message>" --no-verify
...
$ git push origin <branch-name>
```
