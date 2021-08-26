"""
    @Author: Tukaram Rathod
    @Date: 2021-08-25 11:26:30 AM
    @Title : WindChill
"""
import math

while True:
    try:
        # taking input from user
        t = int(input("Enter Temperature T: "))
        v = int(input("Enter wind speed V: "))
        break
    except ValueError:  #Exception ValueError
        print("Check the input")

if t <= 50 and 3 <= v and v <= 120:
    w = 35.74 + 0.625 * t + (0.4275 * t - 35.75) * math.pow(v,0.16)
    print(w)
else:
    print("Enter Correct Values.")