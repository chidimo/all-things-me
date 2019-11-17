# MongoDB

1. `show dbs`
1. `use <db name>`
1. `show collections`
1. `quit()`
1. `db.<collection name>.insertOne({})`
1. `db.<collection name>.insertMany({})`
1. `{$and: [{fieldname: {$exists: true}}, {fieldname: null}]}` filter for items where fieldname key exists AND its value is null

1. `mongorestore --drop --gzip --uri mongodb+srv://m220student:m220password@mflix-gyvwn.mongodb.net data` This should be run in normal command shell, NOT the mongo shell.
