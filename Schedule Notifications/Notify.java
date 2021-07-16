package org.org.appname;
//The package name of your android app

import android.content.BroadcastReceiver;
import android.content.Intent;
import android.content.Context;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;
import android.app.Notification;
import android.os.Build;
import android.media.RingtoneManager;
import android.net.Uri;
import android.media.AudioAttributes;
import org.org.appname.R;
import java.lang.Math;

public class Notify extends BroadcastReceiver{

  // This function is run when the BroadcastReceiver is fired
  @Override
  public void onReceive(Context context, Intent intent) {
    // function to create notification channel
    this.createNotificationChannel(context);
    // function to create the notification
    this.sendNotification(context, intent);
  }

  private void createNotificationChannel(Context context) {

        //checks if android version is equal to or above nougat else doesnt do anything
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            Uri sound = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);

            AudioAttributes att = new AudioAttributes.Builder()
                    .setUsage(AudioAttributes.USAGE_NOTIFICATION)
                    .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
                    .build();
            // Sets the name of the notification channel
            CharSequence name = "New Notification";
            // sets the description of the notification channel
            String description = "New Notification";
            int importance = NotificationManager.IMPORTANCE_HIGH;
            NotificationChannel channel = new NotificationChannel("NOTIFICATION", name, importance);
            channel.setDescription(description);
            channel.setSound(sound, att);
            channel.enableLights(true);
            channel.enableVibration(true);
            NotificationManager notificationManager = context.getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }

    private void sendNotification(Context context, Intent intent) {
         Uri uri= RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
         //create an unique notification id. Here it is done using random numbers
         int notification_id = (int)(Math.random()*(8000-1+1)+1);

         NotificationCompat.Builder builder = new NotificationCompat.Builder(context, "NOTIFICATION")
                 .setSmallIcon(R.drawable.ic_launcher)
                 .setContentTitle("Your notification title here")
                 .setContentText("Your notification description here")
                 .setTicker("New Notification")
                 .setSound(uri)
                 .setAutoCancel(true)
                 .setOnlyAlertOnce(false)

         NotificationManagerCompat notificationManager = NotificationManagerCompat.from(context);
         notificationManager.notify(notification_id,builder.build());
     }


}
