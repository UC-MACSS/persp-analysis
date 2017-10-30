# Student submissions

All submissions for course assignments should be stored in this folder. Create a subfolder following the syntax `lastname_firstname/` in this directory (e.g. `soltoff_benjamin` or `mausolf_joshua`).

## Submitting your assignment

All assignments for this course should be submitted via [GitHub pull request](https://help.github.com/articles/about-pull-requests/). The basic workflow for homework should be:

1. [Fork](https://guides.github.com/activities/forking/) the [course repository](https://github.com/UC-MACSS/persp-analysis)
1. [Clone](https://help.github.com/articles/cloning-a-repository/) the repository to your computer
1. Modify the files and [commit changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) to complete your paper/problem set.
1. [Push](https://help.github.com/articles/pushing-to-a-remote/) the changes up to your forked repository on GitHub.
1. [Create a pull request](https://help.github.com/articles/creating-a-pull-request) on the original repository to turn in the assignment. *Make sure to include your name in the pull request.*

> Once you have forked the repository the first time, you do not need to make a new fork for each assignment. Rather, [sync your fork with the upstream repository](https://help.github.com/articles/syncing-a-fork/). This will merge updates to the assignment repository with your fork.

> **Additional Resources from Lab**:
* [Intro Git Tutorial](http://jmausolf.github.io/code/intro_git/)
* [Intermediate Git Tutorial](http://jmausolf.github.io/code/intermediate_git/)


### NOTE:

Please **DO NOT REMOVE** the folders for other students or change their files. We will not accept pull requests that make these changes. If you accidentally remove these folders and commit those changes, you will need to force-sync your fork with the upstream master.

**BEFORE** force-syncing, **you will need to save a backup of your student folder (students/lastname_firstname) and all files**. 

#### A force-sync will remove any changes not already on the upstream master from YOUR LOCAL FORK, and that work will be lost.

**Once you backup your student/lastname_firstname folder**, proceed to force sync to the master:

```
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force 
```

Then restore your personal folder to the students folder. Proceed with adding/committing/pushing the changes to your folder. Create a new pull request as needed.

## Format

Homework submissions must be in a reproducible, text-based format such as `.md`, `.Rmd` or `.tex`, with `.md` being preferred. If submitting, `.tex`, you must also submit the corresponding `.pdf` file. Any `.pdf` files without a corresponding reproducible source file (`.md`, `.Rmd`, `.tex`) will be rejected. Other formats such as `.docx` or `.rtf ` are not allowed and will be refused.
