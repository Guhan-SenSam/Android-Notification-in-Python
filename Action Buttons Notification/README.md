![Action Notification](https://developer.android.com/images/ui/notifications/notification-basic-action_2x.png)

# Creating A Notification With An Action Button

Here we will be creating a simple notification that on has an action button which on click will execute a certain function.
You can add a maximum of three action buttons to a notification

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
  Add these lines to it.
  ```
  {% for a in args.add_activity  %}
   <activity android:name="{{ a }}"></activity>
   {% endfor %}
  ```
Above lines should be added after the below lines.
  ```
  <receiver android:name="org.org.appname.Action1"
            android:enabled="true"
        android:exported="false">
    </receiver>
  ```

## 8. Build
  Create a copy of the edited manifest in some other directory.
  Then run `buildozer android clean` and then recompile your app. The app should compile but this would have reverted all your changes to the manifest template file. Go back to the same directory and copy the edited manifest template into it(replacing the default one). Now run a normal compile of your app and everything will work.


## Extras:

  ### Dismiss Notification on Action Button click

  By default when you click on an action button of a notification. It will not dismiss the notification. To do this you need to pass the notification id in has an extra for the intent. And in the BroadcastReceiver get that extra and use it to dismiss the notification.

  To your python code add the following lines after creating the intent object.
  ```
  intent.putExtra("NOTIFID",id)
  ```
  Remember to use the same id value for the notification id and also for the id used here.

  In your java class add the following lines inside the `onReceive` method.
  ```
  NotificationManagerCompat notificationManager = NotificationManagerCompat.from(context);
  notificationManager.cancel(intent.getExtras().getInt("NOTIFID"));
  ```
  Remember to import the necessary classes
  ```
  import androidx.core.app.NotificationManagerCompat;
  ```

  ### Launch Kivy App on Action Button Click

  Sometimes you would want to launch your kivy app on pressing an action button. It is suggested not to use this method as action buttons are meant to execute operations quickly and launching a kivy app is very slow.

  Modify the python file by removing these lines
  ```
  intent = Intent(context, action1)

    # Creating our PendingIntent
    pendingintent = PendingIntent.getBroadcast(
        context, id, intent, PendingIntent.FLAG_CANCEL_CURRENT
    )
  ```

  and instead add these lines
  ```
  from android import python_act
  intent = Intent(content,python_act)
  intent.putExtra("ACTION",1)
  pending_intent = PendingIntent.getActivity(context,id,intent,0)
  ```
  Here `ACTION` will be a key that is passed to our python activity on start. You can access this extra data from the intent inside your main.py file and thus know if the app was just launched normally or if it was launched by clicking on the notification. To do that add the following code inside you main.py file.
  ```
  from jnius import autoclass
  PythonActivity = autoclass('org.kivy.android.PythonActivity')
  mActivity = PythonActivity.mActivity

  intent = mActivity.getIntent()
  start = intent.getShortExtra("ACTION",0)
  if start == 0:
    # App launched normally from homescreen
  else:
    # App launched through notification
  ```
  Here 0 is just a default value that will be assigned to start in case an intent doesn't have the extra data.


## References:
https://developer.android.com/reference/android/content/Intent
https://developer.android.com/reference/android/app/PendingIntent
https://developer.android.com/training/notify-user/build-notification
https://groups.google.com/g/kivy-users/c/Qroi2FJcRhU
