from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
if platform == 'android':
    from jnius import autoclass
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    mActivity = PythonActivity.mActivity

kv_string = '''
Screen:





'''


class MainApp(App):
    def build(self):
        kv = Builder.load_string(kv_string)
        return kv

    # This function is autorun at start of a kivy app
    def on_start(self):
        # We make sure that the rest of this function only executes if on android
        if platform != "android":
            return
        # Get the intent that is passed to our kivy app on on start
        # This intent could have come from the user normally starting the application
        # or also come from the notification, we need to figure out from where it came
        intent = mActivity.getIntent()
        # Checks to see if the intent has extra data. If not it will just add 0
        # If intent has extra data we have launched from the notification so execute based on that
        # If value is 0 we have launched the app normally and we continue normal execution
        start = intent.getShortExtra("LAUNCHED_FROM_NOTIF", 0)
        if start == 0: # Normal app launch
            return
        else:  # APp launched from notification
            print("I Have been launched from a notification")


if __name__ == '__main__':
    MainApp().run()
