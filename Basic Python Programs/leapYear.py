"""
    @Author: Tukaram Rathod
    @Date: 2021-08-24 08:00:30 AM
    @Title :Leap Year
"""
def leapYear(year):
    if(year < 1000):
        print("Please Enter 4 Digit Year")
        return

    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print("Leap Year")
    else:
        print("Not a Leap Year")

leapYear(int(input("Enter Year:")))




