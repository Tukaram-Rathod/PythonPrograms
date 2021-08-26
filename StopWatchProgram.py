"""
@Author: Tukaram Rathod
@Date: 2021-08-25 11:50:30 AM
@Title : Simulate Stopwatch Program
a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
    the start and end clicks
b. I/P -> Start the Stopwatch and End the Stopwatch
c. Logic -> Measure the elapsed time between start and end
d. O/P -> Print the elapsed time.
"""
import time

class StopWatch:
    try:
        while True:
            # print("Enter 1 to Start Time:");
            start = int(input("Enter 1 to Start:"))
            startTime = time.time()
            stop = int(input("Enter 0 to Stop Time:"))
            endTime = time.time()
            timeElapsed = endTime - startTime
            print("Time elapsed from Start to Stop is: ", timeElapsed, " Sec")
    except ValueError:
        print("Invalid input ")