"""
    @Author: Tukaram Rathod
    @Date: 2021-08-25 10:06:30 AM
    @Title :Distance
"""
import math

class Distance:
    try:
        X = int(input("Enter the value for X :"))
        Y = int(input("Enter the value for Y :"))
        if (X and Y) == 0:
            raise ValueError
        else:
            result = (X * X) + (Y * Y)
            distance = math.sqrt(result)
            print("Distance between the two points ", +distance)
    except ValueError:
        print("Invalid Input")