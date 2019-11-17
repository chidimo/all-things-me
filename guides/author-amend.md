# Author amend

```cmd
git filter-branch --env-filter '
OLD_EMAIL="orjichidi95@gmail.com"
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
' --tag-name-filter cat -f -- --branches --tags
```

The `-f` is to override any previous backup
