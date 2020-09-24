import time 
from plyer import notification


if __name__ == "__main__":
    #you can add loop here to repeat this process
    notification.notify( 
    title="Please drink Water and do Pranayam",
    message = "This is the time, don't forget the rules. Drink water and mind your breath.",
    app_icon="icon.ico",
    timeout=20
        
    )
    time.sleep(60*60)

