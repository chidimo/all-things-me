# Postgres

## Install postgres on mac

1. Install with `brew install postgres`
1. Check version with `postgres --version`
1. Initialize with `initdb /usr/local/var/postgres`. If the db cluster already exists you will get an error message.
1. Create role/user with `createuser --pwprompt <username>`

## `psql` commands

`\l`
`\?`

1. `'psql -h localhost -d testdb -U postgres -f test/testdb.sql';`
1. `'psql -h localhost -d testdb -U postgres -c "delete from loans;delete from repayments"';`

```cmd
# These work inside a MySQL shell

show databases; # see all my dbs. I deleted a few
drop database <db-name>; # if needed
use <db-name>; # the database name for your django project
show tables; # see all tables in the database
DESCRIBE <table-name>; # shows columns in the database
SHOW COLUMNS FROM <db-name>; # same thing as above
ALTER TABLE <table-name> CHANGE <old-column-name> <new-column-name> <col-type>; # now I manually updated my column name
```

<https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb>

```cmd
brew services start postgresql
psql postgres
# steps
psql -U postgres
CREATE DATABASE <db-name>
\list
```
