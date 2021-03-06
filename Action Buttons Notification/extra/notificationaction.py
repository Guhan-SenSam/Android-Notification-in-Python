from jnius import autoclass, cast
from android import python_act

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
Intent = autoclass("android.content.Intent")
PendingIntent = autoclass("android.app.PendingIntent")

# Autoclass our own java class
action1 = autoclass("org.org.appname.Action1")


def create_channel():
    # create an object that represents the sound type of the notification
    sound = cast(Uri, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION))
    att = AudioAttributesBuilder()
    att.setUsage(AudioAttributes.USAGE_NOTIFICATION)
    att.setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
    att = cast(AudioAttributes, att.build())

    # Name of the notification channel
    name = cast("java.lang.CharSequence", AndroidString("Channel Name"))
    # Description for the notification channel
    description = AndroidString("Channel Description")
    # Unique id for a notification channel. Is used to send notification through
    # this channel
    channel_id = AndroidString("channel_id")

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

    # code to add an action button
    # Creating intent that will launch our kivy app
    intent = Intent(context, python_act)
    # Set some more data for the intent
    intent.setFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP)
    # Sets intent action type
    intent.setAction(Intent.ACTION_MAIN)
    # Set intent category type
    intent.addCategory(Intent.CATEGORY_LAUNCHER)
    # We add extra data to the intent so that we can detect from python if the app
    # was launched through the notification or normally
    # In our main.py we will check for this "LAUNCHED_FROM_NOTIF" extra. If it is present
    # the app was launched from a notification
    intent.putExtra("LAUNCHED_FROM_NOTIF", 1)

    # Create a pending Intent using your own unique id (int) value
    pending_intent = PendingIntent.getActivity(context, id, intent, 0)
    # Create the action object
    # Give it an id and a string to represent the text to be shown on the notification
    action1_button = NotificationCompat.Action.Builder(
        id, "action1", pendingintent
    ).build()
    # Add the action to the notification
    builder.addAction(action1_button)

    # Create a notificationcompat manager object to add the new notification
    compatmanager = NotificationManagerCompat.func_from(context)
    # Pass an unique notification_id. This can be used to access the notification
    compatmanager.notify(notification_id, builder.build())
