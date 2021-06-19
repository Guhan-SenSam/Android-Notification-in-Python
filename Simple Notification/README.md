![Simple Notification](https://developer.android.com/images/ui/notifications/notification-basic_2x.png)

# Creating A simple Notification

Here we will create simple Notification that has a title a description and displays the icon of the app that fired it.

**This is not runnable code. You need to pass the proper variables mentioned in the comments and figure out where to fit these lines into your program**

## 1. Create the python file
  We will use pyjnius to write java code within python.

## 2. Create Notification channel
  From android 8 onwards all notification must be sent through a channel. That is what is done in the function `create_channel`. If you want the code to work below android 8 you need to check the api level and not execute this function if the api level is below that of android 8.

## 3. Create a Notification
  Call the function `create_notification` to create and display your notification. This is basic notification. Hold on to the notification id as it can be used to cancel the notification in the future

## References
https://developer.android.com/training/notify-user/build-notification
https://developer.android.com/training/notify-user/channels
https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder
