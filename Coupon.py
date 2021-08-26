"""
@Author: Tukaram Rathod
@Date: 2021-08-25 11:33:30 AM
@Title :Coupon Numbers
a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you need to
    generate distinct coupon number? This program simulates this random process.
b. I/P -> N Distinct Coupon Number
c. Logic -> repeatedly choose a random number and check whether it's a new one.
d. O/P -> total random number needed to have all distinct numbers.
e. Functions => Write Class Static Functions to generate random number and to
    process distinct coupons.
"""
import random

class CouponNumber():

    def __init__(self,num):
        # Construction initialize using parameter
        self.num = num

    def calculateDistinctNumber(self):
         distinct_Number = []
         while len(distinct_Number) < self.num:
             rand = random.randomrange(0,self.num)
             if rand not in distinct_Number:
                 distinct_Number.append(rand)
             else:
                 pass
         return distinct_Number

while True:
    try:
        num = int(input("Enter the distinct number :"))
        if num < 0:
            print("Please Enter Positive Number:")
            continue
        couponNumber = CouponNumber(num)
        total_Random_Number = couponNumber.calculateDistinctNumber()
        print("Total Distinct Coupon number :",total_Random_Number)
    except ValueError:
        print("Enter Valid! input ")
    except:
        print("Exception Occured")