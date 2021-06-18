# Creating A simple Clickable Notification

Here we will be creating a simple notification that on click will launch our kivy app.

## 1. Create the python file
  We will use pyjnius to write java code within python.

## 2. Create Notification channel
  From android 8 onwards all notification must be sent through a channel. That is what is done in the function `create_channel`. If you want the code to work below android 8 you need to check the api level and not execute this function if the api level is below that of android 8.

## 3. Create a Notification
  Call the function `create_notification` to create and display your notification. This is basic notification. Hold on to the notification id as it can be used to cancel the notification in the future

## 4. Add Intent for launching your Kivy app
  We create an intent that will launch our kivy application. It is not necessary to set the intent's `action` or `category`. We have simply set it here in order to add more info to the intent,but the code should work without it.

  **Flags:** `FLAG_ACTIVITY_SINGLE_TOP` This flag ensures that if the app is already open it will not relaunch it again.

  **Action:** `ACTION_MAIN` When an intent is set as `ACTION_MAIN` then when the intent is fired the app will be launched as if it was launched by the user from their home screen or app drawer. No intent data will be passed.

  We have also set the notification to auto dismiss itself after being pressed. If you dont wish to have this behaviour simply remove this line
  `notification.setAutoCancel(True)` as autocancel deafults to `False`.

## References:s
https://developer.android.com/reference/android/content/Intent
https://developer.android.com/reference/android/app/PendingIntent
https://stackoverflow.com/questions/21303226/what-is-the-difference-between-intent-extra-and-intent-data
