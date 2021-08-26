"""
    @Author: Tukaram Rathod
    @Date: 2021-08-24 08:26:30 AM
    @Title :Power of 2
"""
def power(num):
    i=1
    while i <= num:
        print(f"2^{i} is : {2 ** i}")
        i+=1
power(int(input("Enter Number : ")))