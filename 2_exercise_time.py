# Create a countdown timer from 10 to 0, printing each number every second.
import time

n = int(input("Enter the number from which you would like to start the countdown:"))

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)
# Print a message when the countdown is finished
print("Time's up!")