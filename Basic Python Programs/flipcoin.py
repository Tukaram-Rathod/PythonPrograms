"""
    @Author: Tukaram Rathod
    @Date: 2021-08-24 07:42:30 AM
    @Title :Flip Coin and print percentage of Heads and Tails
"""

import random

number = input("How many times you want to flip the coin ? ")
number = int(number)

if number <=0:
    print("Please enter 1 or more.")

head = 0
tail = 0

for i in range(number):
    coin = random.randint(0,1)
    if coin == 0:
        tail += 1
    else:
        head += 1

tailPercent = ( tail / number ) * 100
print("Tails ", tailPercent)

headPercent = (head / number) * 100
print("Heads ", headPercent)