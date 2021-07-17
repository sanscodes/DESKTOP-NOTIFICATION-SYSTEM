import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Hey!! It's time to drink water now and chill for a bit",
            message = "Health experts commonly recommend eight 8-ounce glasses,which equals about 2 liters, or half a gallon a day. This is called the 8×8 rule and is very easy to remember.",
            app_icon = "icon.ico",
            timeout = 60
        )
        time.sleep(60*60)
