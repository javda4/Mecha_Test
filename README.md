# Mecha_Test

#THIS IS IF USING GIT BASH

#get the repository on your local device

git clone [URL]

######### BRANCH ############
#create new branch

git branch <new_branch_name>

#go to (branch)

git checkout -b (branch)

#create new branch within specified branch

git checkout -b (branch) (branch your creating)

#delete branch

git branch -d (branch)



########PUSHING FILE TO BRANCH
#check the status of files that have been changed

git status

#add files that were worked on 

git add (filename)

#undo commits

git reset

or

git reset [file]

#commit file to local git

git commit -m "brief description of change"

#push your changes for people to see

git push origin [Name_of_Branch] or head

#display list of all commits on current branch

git log

#press q to close out of git log
