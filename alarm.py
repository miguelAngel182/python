import time
import winsound
import opencv

def alarm(duration):
    time.sleep(duration)
    winsound.Beep(900,1000)
    return "¡Time´s up!"

duration = int(input("Enter here duration in seconds: "))
print(alarm(duration))