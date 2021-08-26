"""
    @Author: Tukaram Rathod
    @Date: 2021-08-25 11:06:30 AM
    @Title :To find the roots of the equation.
"""
import math

# taking input from user
a = int(input("Enter value of A:"))
b = int(input("Enter value of B:"))
c = int(input("Enter value of C:"))

# calculate value of function
val = b ** 2 - 4 * a * c
root = math.sqrt(abs(val))

# Check for root and print according to their nature
if val > 0:
    print("Two Real Roots")
    try:
        root1 = (-b + root) / (2 * a)
        print(root1)
        root2 = (-b - root) / (2 * a)
        print(root2)
    except Exception:
        print("Can not Divide by zero")
elif val == 0 :
    print("one real root")
    try:
        print(-b / (2 * a))
    except Exception:
        print("Can not Divide by zero")
else:
    print("No Real Root")
    print(-b / (2 * a)," + i",root)
    print(-b / (2 * a)," - i",root)