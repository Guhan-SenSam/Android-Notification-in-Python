# Scheduling Notifications To Ring Later

Many times you would want your notification to go of later in time rather than as soon as executing the notification creation function. The way we can achieve this is using something called android alarm manager. Don't let the name fool you, the Alarm Manager isn't meant to schedule alarms but instead can be used to make a certain action occur at a certain point of time.

> Note: For this method to work the notification has to be created through Java. This would mean you would have to hard-code the notification content directly in java. If you want to make this changeable check the extra section at the bottom.

## A little about the Alarm Manager

The alarm manager basically allows you to run an android intent at a specific time. This point of time can be in the future or in the past. If it is in the past the action will be fired immediately(give or take a few seconds).

The way we tell the alarm manager to fire at a certain time is by giving it a time in the format of a long number that represent the number of milliseconds from epoch time.

The Alarm Manager can operate in two ways.
  1. **Time since Boot**: In this mode the alarm manager considers the reference time as the point the device was booted and not the actual time at your location. This mode is useful if you have a repeating notification that has to ring in short intervals.

  2. **Real Time Clock**: In this mode the alarm manager uses the real time of your locality to figure out when it has to fire your registered action. The alarm manager is also thankfully timezone aware and will adapt the time to ring a reminder based on the device's current timezone.

> Note: Any tasks that are scheduled in the alarm manager will be removed once the device resets. It is your job to reschedule these tasks on reboot of the system.

## 1. Create the python file
  We will use pyjnius to write java code within python.

## 2. Schedule the Notification to fire at a later time
  Using the alarm manager we will create an alarm object that will fire after 20 seconds. This will be caught by our BroadcastReceiver class (written in Java) and from there we will send the notification.

## 3. Java BroadcastReceiver
  Create the java file. In the first line replace `appname` with your app's name as defined in buildozer.

## 4. Edit Buildozer spec file
  You have to change
  ```
  # (list) List of Java files to add to the android project (can be java or a
  # directory containing the files)
  android.add_src = scr
  ```
  here scr is a folder within my project directory that contains the java class `Notify` that I have written.

## 5. Edit Android Manifest Template
  We need to register our broadcast receiver in our android manifest.

  Inside your project directory you will find a `.buildozer` folder. Within this folder navigate to this path `.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/sdl2/build/templates`.

  There you will find an android manifest template file.
  Add the below lines.

  ```
  <receiver android:name="org.org.appname.Notify"
        android:enabled="true"
        android:exported="false">
        <intent-filter>
           <action android:name="org.org.appname.NOTIFY"/>
       </intent-filter>
  </receiver>
  ```
  After the below lines in the manifest.
  ```
  {% for a in args.add_activity  %}
   <activity android:name="{{ a }}"></activity>
   {% endfor %}
  ```
  Here the appname should be replaced with your app's name as defined in buildozer app path.

## 6. Build
  Create a copy of the edited manifest in some other directory.
  Then run `buildozer android clean` and then recompile your app. The app should compile but this would have reverted all your changes to the manifest template file. Go back to the same directory and copy the edited manifest template into it(replacing the default one). Now run a normal compile of your app and everything will work.
