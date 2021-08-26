"""
    @Author: Tukaram Rathod
    @Date: 2021-08-24 06:06:30 PM
    @Title :2D Array
"""
Rows = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

matrix = []
print("Enter entries in row wise:")

for M in range(Rows):
    array = []
    for N in range(col):
        array.append(int(input())) #Adding input in array
    matrix.append(array)
print("The 2D array is given below:")
for M in range(Rows):
    for N in range(col):
         print(matrix[M][N],end=" ")
    print()