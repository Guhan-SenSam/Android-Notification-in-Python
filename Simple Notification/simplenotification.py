from jnius import autoclass, cast

# Gets the current running instance of the app so as to speak
mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
context = mActivity.getApplicationContext()

# Autoclass necessary java classes so they can be used in python
RingtoneManager = autoclass("android.media.RingtoneManager")
Uri = autoclass("android.net.Uri")
AudioAttributesBuilder = autoclass("android.media.AudioAttributes$Builder")
AudioAttributes = autoclass("android.media.AudioAttributes")
AndroidString = autoclass("java.lang.String")
NotificationManager = autoclass("android.app.NotificationManager")
NotificationChannel = autoclass("android.app.NotificationChannel")
NotificationCompat = autoclass("androidx.core.app.NotificationCompat")
NotificationManagerCompat = autoclass("androidx.core.app.NotificationManagerCompat")
func_from = getattr(NotificationManagerCompat, "from")


def create_channel():
    # create an object that represents the sound type of the notification
    sound = cast(Uri, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION))
    att = AudioAttributesBuilder()
    att.setUsage(AudioAttributes.USAGE_NOTIFICATION)
    att.setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
    att = cast(AudioAttributes, att.build())

    # Name of the notification channel
    name = cast("java.lang.CharSequence", AndroidString("Name of channel"))
    # Description for the notification channel
    description = AndroidString("Description of channel")
    # Unique id for a notification channel. Is used to send notification through
    # this channel
    channel_id = AndroidString("Channel id string")

    # Importance level of the channel
    importance = NotificationManager.IMPORTANCE_HIGH
    # Create Notification Channel
    channel = NotificationChannel(channel_id, name, importance)
    channel.setDescription(description)
    channel.enableLights(True)
    channel.enableVibration(True)
    channel.setSound(sound, att)
    # Get android's notification manager
    notificationManager = context.getSystemService(NotificationManager)
    # Register the notification channel
    notificationManager.createNotificationChannel(channel)


def create_notification():
    # Set notification sound
    sound = cast(Uri, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION))
    # Create the notification builder object
    builder = NotificationCompat.builder(context, channel_id)
    # Sets the small icon of the notification
    builder.setSmallIcon(context.getApplicationInfo().icon)
    # Sets the title of the notification
    builder.setContentTitle(
        cast("java.lang.CharSequence", AndroidString("Notification Title"))
    )
    # Set text of notification
    builder.setContentText(
        cast("java.lang.CharSequence", AndroidString("Notification text"))
    )
    # Set sound
    builder.setSound(sound)
    # Set priority level of notification
    builder.setPriority(NotificationCompat.PRIORITY_HIGH)
    # If notification is visble to all users on lockscreen
    builder.setVisibility(NotificationCompat.VISIBILITY_PUBLIC)

    # Create a notificationcompat manager object to add the new notification
    compatmanager = NotificationManagerCompat.func_from(context)
    # Pass an unique notification_id. This can be used to access the notification
    compatmanager.notify("notification_id", builder.build())
