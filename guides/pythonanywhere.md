# Pythonanywhere

## Back up and restore mysql database

1. Find help on pythonanywhere [here](https://help.pythonanywhere.com/pages/MySQLBackupRestore/) and [here](https://www.pythonanywhere.com/forums/topic/119/)
1. Assuming a pythonanywhere account with username parousia
1. Backup from a bash console

   `$ mysqldump -u parousia -h parousia.mysql.pythonanywhere-services.com 'parousia$choral' > db-backup-choral.sql`

   `$ mysqldump -u parousia -h parousia.mysql.pythonanywhere-services.com 'parousia$funn' > db-backup-funn.sql`

1. Restore from a bash console

   `$ mysql -u parousia -h parousia.mysql.pythonanywhere-services.com 'parousia$choral' < db-backup-choral.sql`

   `$ mysql -u parousia -h parousia.mysql.pythonanywhere-services.com 'parousia$funn' < db-backup-funn.sql`
