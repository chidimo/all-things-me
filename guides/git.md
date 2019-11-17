# Git

## Configure `git` for [visualstudiocode](https://stackoverflow.com/questions/30024353/how-to-use-visual-studio-code-as-default-editor-for-git)

```bash
git config --global core.editor "code --wait"
git config --global -e

# To use vscode as diff tool
[diff]
    tool = default-difftool
[difftool "default-difftool"]
    cmd = code --wait --diff $LOCAL $REMOTE
```

## Fixes

1. Prevent merge conflicts due to `CRLF` characters on windows, set `git config --global core.autocrlf true`
1. Revert a commit https://stackoverflow.com/a/36177806/2689562

## Commands

1. `git shortlog -sne --all`
1. `git config --global user.name "Chidi Orji"`
1. `git config --global user.email "orjichidi95@gmail.com"`
1. `git add --all` or `git add .`
1. `git commit -m "Initial commit"`
1. `git push -u origin master`
1. `git push --set-upstream origin master`
1. `git rm -r --cached path_to_your_folder/`
1. `git rm -r --cached .` `git add .` `git commit -m "fixing .gitignore"`
1. `git reset HEAD~`
1. `git reset HEAD@{1}`
1. `git push --delete <remote_name> <branch_name>`
1. `git shortlog -s -n`
1. `git log --oneline --graph`
1. `git log --pretty=oneline`
1. `git branch -D branch_name`
1. `git mv oldname newname`
1. `git rebase -i HEAD~n`
1. `git tag <number or name>`
1. `git push --tags origin <whichever branch you want to add the tag to>`
1. `git tag -d <number or name> # -d for delete`
1. `git push origin :refs/tags/<number or name>`
1. `git push --tags`
1. `git commit --amend`
1. `git commit --amend --no-edit`
1. `git branch --unset-upstream`

## ssh with private repo

Open a `~/.ssh/config` file and put the following

```
Host github.com
HostName github.com
IdentityFile "path-to-private-ssh-key"
User <github username>
```

Now you can use git commands as usual, but in `git bash`

## Gitflow workflow

Its all about branches and how to name them.

Uses two branches: `master` and `develop`

Each new feature should have its own branch

### Branch naming prefixes

Feature branches? [feature/]
Release branches? [release/]
Hotfix branches? [hotfix/]
Support branches? [support/]
Version tag prefix? []

### When its time for a release

1. Fork a `release` branch off of the latest `develop` branch (This branch must not receive any new feature(s)). Only tidying up tasks can be added.
1. When ready merged into `master`, then `tag`.
1. Merge back into `develop` before continuing development.
1. Delete the feature branch

### Hotfixes

1. Fork off `master`
1. When done, merge back into `master` and `develop` (or current `release` branch)
1. `tag` master with an updated version number
1. Delete the branch
Iburu onye igbo, [pia ebe a](igbo/oti.md)

git filter-branch --env-filter '
OLD_EMAIL="chidi.o@softcom.ng"
CORRECT_NAME="Orji Chidi"
CORRECT_EMAIL="orjichidi95@gmail.com"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
