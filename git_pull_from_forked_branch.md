```git remote -v
git remote add upstream {url-of-repository-from-where-you-forked}
git remote -v
git fetch upstream -v
git branch -a
git checkout origin/{working-branch-name}
git branch -a
git merge upstream/{working-branch-name}
```
