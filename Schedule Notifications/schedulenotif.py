from jnius import autoclass, cast

# Gets the current running instance of the app so as to speak
mActivity = autoclass("org.kivy.android.PythonActivity").mActivity

context = mActivity.getApplicationContext()
Context = autoclass("android.content.Context")
Intent = autoclass("android.content.Intent")
PendingIntent = autoclass("android.app.PendingIntent")
String = autoclass("java.lang.String")
Int = autoclass("java.lang.Integer")


intent = Intent()
intent.setClass(context, Notify)
# Here change the "org.org.test" to whatever package domain you have set.
# Here my buildozer file has the package domain of "org.test".
# After that "NOTIFY" is the custom action we have set. This custom action is
# also defined in the manifest file(check README file). You can use any name here
# just make sure you use the same name while registering the action event
intent.setAction("org.org.test.NOTIFY")
# Create a pending intent to be fired later in time by the alarm Manager
# Here the intent_id is a variable holding a numeric value that uniquely identifies the
# pending intent. Keep this id so that you can cancel scheduled alarms later on.

# There are various types of pending intent flags that can be set based on what you want.
# Here the `FLAG_CANCEL_CURRENT` will cancel any other pending intent with the same id before
# setting itself.
pending_intent = PendingIntent.getBroadcast(
    context, intent_id, intent, PendingIntent.FLAG_CANCEL_CURRENT
)

# This gets the current system time since epoch in milliseconds(works only in python 3.7+)
ring_time = time.time_ns() // 1_000_000
# We now create the alarm and assign it to the system alarm manager. Some methods assign
# an alarm manager instance to a variable and then scheduling a task. But if you need to
# later cancel this alarm from another python file or from another launch of your app(as
# every time you relaunch a kivy the app ,the code is rerun thus creating a new instance of
# the alarm manager rather than the one we used before to schedule the alarm). THIS IS IMPORTANT
# AS WE NEED TO USE THE SAME ALARM MANAGER INSTANCE TO CANCEL AN ALARM

cast(
    AlarmManager, context.getSystemService(Context.ALARM_SERVICE)
).setExactAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, ring_time, pending_intent)

# Here we use RTC_WAKEUP which uses the real time of the device to figure out when to fire the alarm
