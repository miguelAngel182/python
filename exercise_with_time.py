#Measure how long it takes the user to answer a simple math question.
import time

start = time.time()
print("120+790")
input()
end = time.time()
print("Answer time: ", end - start, "seconds")