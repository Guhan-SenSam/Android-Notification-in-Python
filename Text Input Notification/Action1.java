package org.org.appname;
//The package name of your android app

import android.content.BroadcastReceiver;

public class Action1 extends BroadcastReceiver{



  @Override
  public void onReceive(Context context, Intent intent) {
    Bundle remoteInput = RemoteInput.getResultsFromIntent(intent);
    if (remoteInput != null) {
        return remoteInput.getCharSequence(NOTIFICATION_TEXT);
        // This will return the text typed in the notification
    }
      // Code to execute once the button has been pressed
    }
}
