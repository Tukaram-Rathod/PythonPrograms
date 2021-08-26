"""
    @Author: Tukaram Rathod
    @Date: 2021-08-24 07:30:30 AM
    @Title :User Input and Replace String Template
"""
name = input("Enter Your Name Here:")
length = len(name)
if length >= 3:
    template = 'Hello' + ' ' + name + ',How are you?'
else:
    print("Invalid Name")
print(template)