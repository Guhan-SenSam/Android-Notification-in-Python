![Notification](https://developer.android.com/images/ui/notifications/reply-button_2x.png)

# Creating A Notification with a TextField

Here we will be creating a notification that will enable you to type message responses

# 1. Create the python file
  We will use pyjnius to write java code within python.

## 2. Create Notification channel
  From android 8 onwards all notification must be sent through a channel. That is what is done in the function `create_channel`. If you want the code to work below android 8 you need to check the api level and not execute this function if the api level is below that of android 8.

## 3. Create a Notification
  Call the function `create_notification` to create and display your notification. This is basic notification. Hold on to the notification id as it can be used to cancel the notification in the future

## 4. Add Intent to run when user clicks on action button in notification
  Create an action that on click will trigger our own java broadcast receiver which will then execute whatever code we need to run within java. The limitation of this method is that we have to write our code in java. View Notification with Action button for some alternatives that you can use.

  In line 20 we autoclass our own java class. This java file has to be inside your project folder(It can be anywhere as Java will search all sub directories of your project folder). replace `appname` with the name of your app.

  > Note: This is assuming that in your buildozer file you have the following package domain.
    ```
    # (str) Package domain (needed for android/ios packaging)
    package.domain = org.appname
    ```

## 5. Java BroadcastReceiver
  Create the java file. In the first line replace `appname` with your app's name as defined in buildozer.

  Any java code within the `onReceive` method will be executed when the user presses the action button.

  Here I have added some code that will return the text that was input through the notification. In case no text was input it will just return

## 6. Edit Buildozer spec file
  You have to change
  ```
  # (list) List of Java files to add to the android project (can be java or a
  # directory containing the files)
  android.add_src = scr
  ```
  here scr is a folder within my project directory that contains the java class `action1` that I have written.

## 7. Edit Android Manifest Template
  We need to register our broadcast receiver in our android manifest.

  Inside your project directory you will find a `.buildozer` folder. Within this folder navigate to this path `.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/sdl2/build/templates`.

  There you will find an android manifest template file.
  Add the below lines.

  ```
  <receiver android:name="org.org.appname.Action1"
            android:enabled="true"
        android:exported="false">
  </receiver>
  ```
  After the below lines in the manifest.
  ```
  {% for a in args.add_activity  %}
   <activity android:name="{{ a }}"></activity>
   {% endfor %}
  ```

## 8. Build
  Create a copy of the edited manifest in some other directory.
  Then run `buildozer android clean` and then recompile your app. The app should compile but this would have reverted all your changes to the manifest template file. Go back to the same directory and copy the edited manifest template into it(replacing the default one). Now run a normal compile of your app and everything will work.

## Notes:
  Remember to use differenet id's for each pending intent or you may end up overwriting already existing pending intents. You can also add extra info to the intent such as to whom the message is meant to be sent. This can be done by using `putExtra()` when creating the notification intent and then gettting this info in the java code with `getExtra()`.

## References:
https://developer.android.com/reference/android/content/Intent
https://developer.android.com/reference/android/app/PendingIntent
https://stackoverflow.com/questions/21303226/what-is-the-difference-between-intent-extra-and-intent-data
