# Meteor

## Starting a new `Meteor + React` app

  meteor npm install --save react react-dom
  meteor add static-html
  meteor remove blaze-html-templates
  meteor add accounts-ui accounts-password
  meteor npm install --save bcrypt
  meteor add react-meteor-data
  npm install react-meta-tags --save
  meteor remove insecure, autopublish
  meteor npm install --save classnames react-router history
  meteor add meteortesting:mocha
  meteor npm install --save-dev chai

## Setting up meteor for android

1. `meteor install-sdk android` command does nothing. It just prints out a web address. This is the default behaviour.
1. Download and install Android studio. This is mainly needed for package management.
1. Install java 8 from command line: `sudo apt install openjdk-8-jdk` or download it from the oracle website and install

## Manually installing `gradle`

1. Remove any existing `gradle` installation. See [here](https://www.thelinuxfaq.com/ubuntu/ubuntu-17-04-zesty-zapus/gradle?type=uninstall) for guide.
1. Download [gradle](https://gradle.org/install/>)
1. Unzip and place in any directory of your choosing
1. Create environment variable `GRADLE_HOME`
1. Add `GRADLE_HOME/bin` to `PATH`

## Set up java, android `sdk`, and `gradle` environment variables

1. Open up `/home/<account_name>/.bashrc` file.

1. Add the following lines. This creates some environment variables and modifies the path.

  export GRADLE_HOME="/home/<device_name>/gradle-5.0"
  export PATH=$PATH:$GRADLE_HOME/bin
  export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/bin/java"
  export ANDROID_HOME="/home/<device_name>/Android/Sdk"
  export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

## Common errors and resolution

### `/dev/kvm device: permission denied`

1. `sudo apt install qemu-kvm`
1. `sudo adduser ubuntu kvm`
1. `sudo chown <Replace with username> /dev/kvm`

### `Android target: android: Command failed with exit code ENOENT`

This error seems to indicate that there is no Sdk platform installed

1. In android studio, navigate to `File -> Settings -> System Settings -> Android SDK`.
1. In `SDK Platforms`, select `Android 8.0 (Oreo), API Level 26` and deselect all others.
1. Click apply. Wait for the download and installation to complete.
1. In `SDK Tools`, select `Android SDK Build-Tools`, `Android Emulator`, `Android SDK Platform-Tools`, `Android SDK Tools`.
1. Click apply to complete the download and installation.

### `Android target: avdmanager: Command failed with exit code 1`

This error indicates that no virtual device was found.

1. Remove the `/../Android/Sdk/tools` folder and replacing it with the `tools` folder inside the the downloaded `tools_r25.2.5-linux.zip`. I downloaded from this [link](http://mirrors.neusoft.edu.cn/android/repository/tools_r25.2.5-linux.zip)

## Adding android system images manually

1. Copied the link to the zip file from AVD Manager.
1. Extracted the archived `x86` folder to `/../Android/Sdk/system-images/android-26/google_apis_playstore/`. It turned out I didnt really need this. I installed `Android SDK Platform 26, API Level 26, Revision 2` straight from within android studio

## Helpers

### Locating java install directory

1. `whereis java` returns `java: /usr/bin/java /etc/java /usr/share/java /usr/share/man/man1/java`. This shows everywhere java is found. But they're often symbolic links. Now we dig deeper.
1. `ls -l /usr/bin/java` returns `/usr/bin/java -> /etc/alternatives/java`
1. `ls -l /etc/alternatives/java` returns `/etc/alternatives/java -> usr/lib/jvm/java-11-openjdk-amd64/bin/java`
1. `ls -l /etc/alternatives/java -> usr/lib/jvm/java-11-openjdk-amd64/bin/java` returns same thing. We've reached the end of the tunnel.
1. `readlink -f $(which java)` returns same location as above.

### Version checks

1. `javac -version`
1. `java -version`
1. `gradle -version`

### Fix Login failure after editing `.profile`

I edited `.profile` and I couldn't login to my Ubuntu. I then corrected it with the steps below. I actually meant to edit `bash_rc` file.

1. Log into recovery mode (steps here <https://askubuntu.com/a/842232>)
1. `nano /home/<account_name>/.profile`. Now remove the edits and save the file with `Ctrl + X`

### Enable USB Debugging on Huawei P10 Lite

1. See here: <https://www.syncios.com/android/how-to-debug-huawei-p10.html>

## Resources

1. Sdk manager: <https://developer.android.com/studio/command-line/sdkmanager>
1. To completely purge linux system of java: <https://askubuntu.com/a/185250>

## Setup `meteor` for android on windows 10: [guide](https://github.com/meteor/simple-todos-react/issues/72)

1. Add `C:\Users\<account_name>\AppData\Local\Android\Sdk\platform-tools` to system path
1. Create `ANDROID_HOME=C:\Users\<account_name>\AppData\Local\Android\Sdk`
1. Create `JAVA_HOME=C:\Program Files\Java\jdk1.8.0_191`
1. Find and open `emulator.js` from `<project_root>\.meteor\local\cordova-build\platforms\android\cordova\lib`
1. Find the line `avd.target = 'Android ' + level.semver + ' (API level ' + api_level + ')';` and replace it with `avd.target = 'Android ' + (level ? level.semver : '') + ' (API level ' + api_level + ')';`
1. In android studio SDK manager, under `Android 8.0 (Oreo)`, select `Android SDK Platform 26` and `Sources for Android 26`
1. Now fire up android studio, start your virtual android device and power it on, then issue the command `meteor run android`.

It is also possible to run the app on an android phone connected to your PC. For this you have to specify a `mobile-server` for meteor to use and the phone and PC needs to be on the same WIFI network

1. `meteor run android-device --mobile-server http://localhost:3000/`

Each instance of a meteor app needs a server from which to load stuff. For development, `http://localhost:3000/` is sufficient. But for a connected phone to see the resources on the PC, the port `3000` has to be open. These ports are protected by a firewall. To open up a port in the firewall, do the following. [Source](http://www.tomshardware.com/faq/id-3114787/open-firewall-ports-windows.html)

### To open up a port in windows firewall

1. Navigate to `Control Panel, System and Security and Windows Firewall`.
1. Select `Advanced settings` and highlight `Inbound Rules` in the left pane.
1. Right click `Inbound Rules` and select `New Rule`.
1. Check `Port` radio button in `Rule Type` window and click `Next`.
1. Check `TCP`, check `Specify local ports`, Enter `3000` and click `Next`.
1. Select `Allow the connection` in the next window and hit Next.
1. Name the rule something meaningful and click Finish. I named mine `Port 3000 for meteor development`.

## Utilities

### Keep screen awake

1. Installation `meteor add cordova:cordova-plugin-insomnia@4.3.0`
1. <https://www.npmjs.com/package/cordova-plugin-insomnia>, <https://github.com/yauh/sleepwalker>

```javascript
// Keep screen awake https://www.npmjs.com/package/cordova-plugin-insomnia
// in app component, do
componentDidMount() { // Set keep screen alive on mount
    if (Meteor.isCordova) {
        window.plugins.insomnia.keepAwake()
    }
}

```

### Persist data with [nativestorage](https://github.com/TheCocoaProject/cordova-plugin-nativestorage)

Installation `meteor add cordova:cordova-plugin-nativestorage@2.3.2`

### Add status bar

1. Installation `meteor add cordova:cordova-plugin-statusbar@2.4.2`
1. Modify `mobile-config.js` and add

```javascript
// open external urls
// Setting {type: 'intent'} asks the user which app to use for opening the link while {type: 'navigation'} opens the link in-app
App.accessRule("http://*", { type: "intent" });
App.accessRule("https://*", { type: "intent" });
App.accessRule("skype:*", { type: "intent" });

// statusbar https://www.npmjs.com/package/cordova-plugin-statusbar
App.appendToConfig(`
    <preference name="StatusBarStyle" value="lightcontent" />
`);
```

## Build and upload to playstore

1. <https://github.com/ickyrr/HOWTOs/blob/master/Running-Meteor-App-on-Android/How%20to%20Submit%20Meteor%20App%20to%20Google%20Play.md>
1. Build app `meteor build <output_folder> --server="https://currency-analyzer.herokuapp.com/"`
1. Copy the generated `android-release-unsigned.apk` from `<output_folder>\android\project\build\outputs\apk\release` to `<output_folder>\android`
1. Activate `keytool` by adding `C:\Program Files\Java\jdk1.8.0_191\bin` to PATH environment variable or use the full path `<path-to\keytool.exe`
1. `cd` into `..\<project name>\android`
1. Generate key `C:\Program Files\Android\Android Studio\jre\bin\keytool -genkey -alias your-app-name -keyalg RSA -keysize 2048 -validity 10000` (Default `keystore` password is `changeit`. It will be requested twice)
1. Answer the follow up questions and press enter
1. You may ignore following two steps
1. When process is done you may get the following message

  Warning:
  The JKS keystore uses a proprietary format. It is recommended to migrate to PKCS12 which is an industry standard format using "keytool -importkeystore -srckeystore <path-to-keystore-file>\.keystore -destkeystore <path-to-keystore-file>\.keystore -deststoretype pkcs12".

    Where `-srckeystore` is the source keystore, `-destkeystore` is the destination keystore, and `-deststoretype` is the destination keystore format. This action **Replaces** the old .keystore file.

1. Run `keytool -importkeystore -srckeystore C:\Users\Chidimma\.keystore -destkeystore C:\Users\Chidimma\.keystore -deststoretype pkcs12` with the same password `changeit` to make the conversion. After it runs the following message is displayed.

        Warning:
        Migrated "<path-to-keystore-file>\.keystore" to Non JKS/JCEKS. The JKS keystore is backed up as "<path-to-keystore-file>\.keystore.old".

1. `.keystore` is located at `C:\Users\<administrator account name>` since I'm running my command line as administrator.
1. Create a secure backup of the `.keystore` file.
1. Now sign the app by running `jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 android-release-unsigned.apk your-app-name`. Each time you update your app you must sign it with the same key for you to upload it to google playstore.
1. Next step is to run `zipalign`. Add the location of `zipalign.exe` to `PATH` or run the command with the full path to `zipalign` specified.
1. `<path-to-zip-align.exe> <alignment-in-bytes_usually-4> android-release-unsigned.apk your-app-name.apk`
1. You should see the generated `your-app-name.apk` in the current working directory

## Conflicting jquery versions issue

### Problem: Installed `jquery` (1.11.1) from `atmospherejs` conflicts with a version (3.3.1) that is a `Bootstrap` dependency (`Uncaught Error: Bootstrap's JavaScript requires jQuery version 1.9.1 or higher, but lower than version 3`)

1. Run `npm shrinkwrap`
1. Edit `package.json` and `npm-shrinkwrap.json` and replace jquery version with 2.2.4
1. Delete `node_modules/` and re-install the following packages

  meteor npm install
  meteor remove twbs:boostrap jquery
  meteor npm install --save bootstrap jquery
