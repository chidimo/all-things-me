# Building meteor apps

1. `meteor build D:\apk-builds --server="https://auditioner.herokuapp.com"`
1. `meteor build D:\apk-builds --server="http://localhost:3000"`
1. `meteor build D:\apk-builds --server="http://localhost:12016"`
1. `meteor run android-device --mobile-server="https://auditioner.herokuapp.com"`
1. `meteor run android-device --mobile-server="http://localhost:12016"`
1. `"C:\Program Files\Android\Android Studio\jre\bin\keytool.exe" --genkey -alias auditioner -keyalg RSA -keysize 2048 -validity 10000`
1. `"C:\Program Files\Android\Android Studio\jre\bin\keytool.exe" -importkeystore -srckeystore C:\Users\Chidimma\.keystore -destkeystore C:\Users\Chidimma\.keystore -deststoretype pkcs12`
1. `"C:\Program Files\Android\Android Studio\jre\bin\jarsigner.exe" -verbose -sigalg SHA1withRSA -digestalg SHA1 android-release-unsigned.apk auditioner`
1. `"C:\Users\Chidimmo\AppData\Local\Android\Sdk\build-tools\28.0.3\zipalign.exe" 4 android-release-unsigned.apk auditioner.apk`

1. `heroku config:set MAIL_URL=smtps://atest4067%40gmail.com:zqV7tnfYU4WU@smtp.gmail.com:465`
1. `heroku config:set MONGO_URL=mongodb+srv://auditioner-user:gDPGlskbpNobI1il@auditionerdb-slgse.mongodb.net/auditionerDB?retryWrites=true`
1. `heroku config:set ROOT_URL=https://auditioner.herokuapp.com/`
1. `heroku config:set S3={"s3":{"key": "", "secret": "", "bucket": "auditioner-mobile-deployment-2019-02", "region": "eu-west-2"}}`

1. `meteor build D:\apk-builds --server="http://currency-analyzer.herokuapp.com"`
1. `"C:\Program Files\Android\Android Studio\jre\bin\jarsigner.exe" -verbose -sigalg SHA1withRSA -digestalg SHA1 android-release-unsigned.apk currency-analyzer`
1. `"C:\Users\Chidimmo\AppData\Local\Android\Sdk\build-tools\28.0.3\zipalign.exe" 4 android-release-unsigned.apk currency-analyzer.apk`
