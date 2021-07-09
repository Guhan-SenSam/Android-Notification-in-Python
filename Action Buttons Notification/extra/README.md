## Method Without Java
 This method allows you to run some code when you press on the notification action button without requiring any java code. But I would highly suggest against this for the following reasons.

 1. This method requires you to launch your entire kivy application which is slow. Action buttons in notifications are meant to be instant background processes they are not meant to take time to happen

 2. It results in your kivy app being displayed on your screen. Fox example a notification action button would be used to snooze an event reminder for 10 minutes. This operation should not launch your app and should just be completed in the background.If the app is launched it completely defeats the purpose of these quick action buttons. Thus I highly don't suggest this method.

 ## Steps

 1. Use the code in the two files to incorporate this method in your app. Remember you have to check for the intent extra data in order for your kivy app to be able to distinguish if it has been normally launched or has been launched from a notification.

> Note: This method doesn't require you to edit the android manifest template.
