# Mecha_Test


## git clone
#get the repository on your local device

```
git clone <URL>
```

## Branch

### create new branch

```
git branch <new_branch_name>
```

### go to (branch)

```
git checkout -b <branch>
```

### create new branch within specified branch

```
git checkout -b (branch) (branch your creating)
```

### delete branch

```
git branch -d (branch)
```


## The entire process of pushing to github

### check the status of files that have been changed

```
git status
```
## git add
### add a file that has been modified to staged
```
git add (filename)
```

### add all modified files to staged

```
git add *
```

### undo

```
git reset
```

or

```
git reset [file]
```
## git commit
### commit all files that have been staged by git add

git commit -m "brief description of change"

## git push

```
git push origin <Name_of_Branch>
```

### display list of all commits on current branch

```
git log
```

#press q to close out of git log
