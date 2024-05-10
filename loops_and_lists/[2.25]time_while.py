# Exercise 2.25: Demonstrating time-controlled while loops

import time

# Part 1: Loop that runs for approximately 10 seconds
t0 = time.time()  # Record the start time
while time.time() - t0 < 10:  # Check if less than 10 seconds have passed
    print('....I like while loops!')
    time.sleep(2)
print('Oh, no - the loop is over.')
