"""
    @Author: Tukaram Rathod
    @Date: 2021-08-24 08:57:30 AM
    @Title :Prime Factor
"""
f=0
num = int(input("Enter Number:"))
for i in range (2, num + 1):
    if num % i == 0:
        for j in range (2, int(i/2)):
            if i%j ==0:
                f=1
                break
        if f==0:
            print(i)