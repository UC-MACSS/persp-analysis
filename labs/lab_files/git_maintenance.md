# Basic Git Maintenance

In working on your homework and files, you may accidentally modify files you should not have or create files you would like to erase. Here are some recommended strategies for dealing with this.

## Check Status

Be sure to check what you are staging to commit with the command `git status`

```bash 
git status #shows changes
```

After you add files to commit run git status again
```bash
git status
```

Are all the files listed what you really want to commit. If you have files changed outside your student folder, reset the HEAD and try adding again:

```bash
git reset HEAD
git add SOMETHING
git status
```

## Remove Files

To for example remove files in your folder (such as test files or drafts) use `git rm`:

```bash
git rm NAME_OF_FILE(S)
git commit -m "removing unwanted file"
git push origin master
```

## Restore Original File You Modified and Should Not Have

This process is most helpful if you have only modified the files but not committed/pushed the changes.

```bash
#In terminal remove the local file
rm NAME_OF_FILE #permanently erases file
git checkout NAME_OF_FILE
```

## Rename Files (not case sensitive)

To rename files or folders (not case sensitive) use `git mv`:

```bash
git mv OLD_FILE_NAME NEW_FILE_NAME
git commit -m "renamed file"
git push origin master
```

## Rename Files (case sensitive).

Git cannot directly rename a file to a case sensitive version of the same filename. Thus `git mv FILENAME filename` will fail. You must rename it a temporary name, and rename to the new name to make this change:

```bash
git mv FILENAME tmp
git mv tmp filename
git commit -m "renamed file"
git push origin master
```

If you have committed changes to files to your fork that cannot be easily undone or modified, such as modifying folders or removing directories outside the student folder that you should not have done, you may want to instead force sync your fork to the master. 

**FORCE SYNCING WILL OVERWRITE YOUR FORK AND COMMITS** 
**YOU MUST BACK UP THE FILES YOU WANT TO KEEP FIRST BEFORE PROCEEDING**

I would recommend the following:

1. Renaming your local fork `mv repo corrupted_repo`. 
2. `git clone your_fork`
3. Double check the files you want to keep are in `corrupted_repo`. (i.e. `ls corrupted_repo/students/lastname_firstname/`)
4. cd `your_fork`
5. [Follow the steps to force-sync the fresh clone of `your_fork`](https://github.com/UC-MACSS/persp-analysis/tree/master/students):

```bash
#WARNING, ONLY DO AFTER FOLLOWING THE ABOVE STEPS AND READING THE DIRECTIONS
#YOUR FORK ON GITHUB AND WORK WILL BE DELETED AND SYNCED TO MASTER

git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force 
```

6. Now that your fork is freshly synced to the master, copy the desired files to the new and correct location:
```
mkdir students/lastname_firstname
cp ../corrupted_repo/students/lastname_firstname/* students/lastname_firstname/
```

7. Commit and Push
```bash
git status #check what you are adding
git commit -m "adding homework"
git push origin master
```
