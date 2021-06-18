# Creating A simple Clickable Notification

Here we will be creating a simple notification that on click will launch our kivy app.

## 1. Create the python file
  We will use pyjnius to write java code within python.

## 2. Create Notification channel
  From android 8 onwards all notification must be sent through a channel. That is what is done in the function `create_channel`. If you want the code to work below android 8 you need to check the api level and not execute this function if the api level is below that of android 8.

## 3. Create a Notification
  Call the function `create_notification` to create and display your notification. This is basic notification. Hold on to the notification id as it can be used to cancel the notification in the future

## 4. Add Intent to run when user clicks on action button in notification
  Create an action that on click will trigger our own java broadcast receiver which will then execute whatever code we need to run within java. The limitation of this method is that we have to write our code in java. I will be attaching some alternatives below allowing you to write code in python, but they aren't elegant solutions.

  In line 23 we autoclass our own java class. This java file has to be inside your project folder(It can be anywhere as Java will search all sub directories of your project folder). replace `appname` with the name of your app.

  > Note: This is assuming that in your buildozer file you have the following package domain.
    ```
    # (str) Package domain (needed for android/ios packaging)
    package.domain = org.appname
    ```

## 5. Java BroadcastReceiver
  Create the java file. In the first line replace `appname` with your app's name as defined in buildozer.

  Any java code within the `onReceive` method will be executed when the user presses the action button.

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
  Add these lines to it. These lines should be added After
  ```
  {% for a in args.add_activity  %}
   <activity android:name="{{ a }}"></activity>
   {% endfor %}
  ```

  ```
  <receiver android:name="org.org.appname.Action1"
            android:enabled="true"
        android:exported="false">
    </receiver>
  ```



## References:
https://developer.android.com/reference/android/content/Intent
https://developer.android.com/reference/android/app/PendingIntent
https://developer.android.com/training/notify-user/build-notification
https://groups.google.com/g/kivy-users/c/Qroi2FJcRhU
