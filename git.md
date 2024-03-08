## Git Useful Commands

### Initialization

* **git init** - Initializes a new Git repository.
* **git clone <url>** - Clones an existing Git repository.

### Staging and Committing

* **git add <file>** - Adds a file to the staging area.
* **git add -A** - Adds all files in the current directory to the staging area.
* **git commit -m "<message>"** - Commits the changes in the staging area with a message.

### Branching and Merging

* **git checkout -b <branch-name>** - Creates and switches to a new branch.
* **git checkout <branch-name>** - Switches to an existing branch.
* **git merge <branch-name>** - Merges the specified branch into the current branch.

### Viewing Changes

* **git status** - Shows the status of the working directory and staging area.
* **git diff** - Shows the difference between the working directory and the staging area, or between two commits.
* **git log** - Shows the commit history.

### Undoing Changes

* **git reset HEAD <file>** - Unstages a file from the staging area.
* **git reset HEAD~1** - Undoes the last commit.
* **git revert <commit-hash>** - Reverts a commit.

### Pushing and Pulling

* **git push origin <branch-name>** - Pushes the specified branch to the remote repository.
* **git pull origin <branch-name>** - Pulls the specified branch from the remote repository and merges it into the current branch.

### Tagging

* **git tag <tag-name>** - Creates a tag.
* **git tag -a <tag-name> -m "<message>"** - Creates a tag with a message.
* **git show <tag-name>** - Shows the information about the specified tag.

### Other Useful Commands

* **git stash** - Stashes the changes in the working directory and staging area.
* **git stash pop** - Restores the changes that were stashed.
* **git clean -f <file>** - Deletes the specified file from the working directory.
* **git bisect <good-commit> <bad-commit>** - Finds the commit that introduced a bug.
* **git remote add origin <url>** - Adds a remote repository.
* **git fetch origin** - Downloads the latest changes from the remote repository.
* **git remote -v** - Lists all remote repositories.
* **git config --global user.name "<name>"** - Sets the user name.
* **git config --global user.email "<email>"** - Sets the user email.
* **git config --list** - Lists all Git configuration settings.
* **git help** - Shows help for Git commands.