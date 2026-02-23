import time

while 1:
    current_time = time.strftime("%H:%M:%S")
    print("Current time:", current_time, end = "\r")
    time.sleep(1)
    