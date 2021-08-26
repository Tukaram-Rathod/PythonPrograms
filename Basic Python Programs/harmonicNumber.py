"""
    @Author: Tukaram Rathod
    @Date: 2021-08-24 08:57:30 AM
    @Title :Harmonic Number
"""
def harmonic(number):
    i=1
    total=0

    while i<= num:
        print(f"1/{i}")
        total += 1/i
        i+=1
        print(f"Harmonic number is {total}")

num = int(input("Enter Number: "))
if num <=0:
    print("Invalid Number.")
else:
    harmonic(num)

