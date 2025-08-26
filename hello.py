#introduction to python
"""
save python file with ".py" extension
execute python file via terminal by typing the python version and the name of the file e.g pyhton3 hello.py
filename must be descriptive of it task
Python uses indentation to indicate a block of code.
The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

"""

""" Check the Python version of the editor:
    import sys
    print(sys.version)
"""

"""_EXERCISES_
        True or False: Indentation in Python is for readability only.
        Which character is used to define a Python comment: ',//,#,/*
        What is a correct way to declare a Python variable? var x = 5,#x = 5,$x = 5,x = 5

        What will be the result of the following syntax:
        x = 5
        x += 3
        print(x)
"""
#print("Hello world!")
# a=5
# b=10

# sum = a + b
# print(sum)

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# num3 = num1 * num2
#print("Product is: ", num3)
# print(type(num3)) 

#data =('Laptop',['Apple', 'Orange',["Fan","Socket",["120",100,500,[50,96],],],], "Android","Windows",[30+56j,["Nigeria","Canada"],],150)

#data_type = type(data)
#convert_to_list = list(data)
#android = convert_to_list[2]

# convert_to_list[2]="Ubuntu"
# element_96 = convert_to_list[1][2][2][3][1]
# element_Nigeria = convert_to_list[4][1][0]
# convert_to_list[4][1].insert(1,"London")
# last_element = convert_to_list[::-1]
# #convert_to_list[1][2][2].pop(0)
# convert_to_list[1][2][2].remove("120")

# output_2_5 = convert_to_list[2:5]
# #print("Output of 2:5 =",output_2_5)

# output_8 = convert_to_list[:8]
# #print("Output of :8 =",output_8)

# output_4_down = convert_to_list[4:]
# #print("Output of 4: =",output_4_down)

# output_122 = convert_to_list[1][2][:2]
# print("Output of 4: =",output_122)





#print(convert_to_list)

# x=2
# y=3
# result_2a=(x // y + x % y)
# result_2b =((x // y + x % y) +(5 / 2 + (4 ** 2) - 5 - 2 * 4*(9 % 4))) **2
# print(result_2a)
# print(result_2b)
# print(2//3)

print('--------Built-in functions----------')
print("Absolute value =",abs(-7.25))
#print(pow(4,3))
#print(max(4,6,8,2,1))
#print(min(4,6,8,2,1))
#print(round(3.14))
#print(round(3.5))
# print(round(3.5))
#print(round(3.45,1))
#print(round(3.456,1))
# print(round(3.4567,3))
# print(round(3.45678,4))
#print(len("Hello World"))
#print(type([1,2,3,4,5,6,7,8,9,10]))
#print(len((1,2,3,4,5,6,7,8,9,10)))
#print(type({"Name": "John", "Age": 30, "City": "New York"}))
#print(type(3.14))
# print(type("Hello"))
# print(type([1,2,3,4,5]))
# print(type((1,2,3,4,5)))
# print(type({"Name": "John", "Age": 30, "City": "New York"}))
#print(type(True))
#print(type(None))
#print(type(5 + 3j))
#print(type(lambda x: x + 1))



print('--------User defined functions----------')
#factotial
# 5 factorial = 5 * 4 * 3 * 2 * 1 = 120
# 6 factorial = 6 * 5 * 4 * 3 * 2 * 1 = 720

# def fact(n):
#     total = 1
#     for k in range(1, n + 1):
#         #print(k)
#         #total *= k
#         total = total * k

#     return total

#print(fact(5))


# 1,5+1,
#k=1,2,3,4,5,6
#total = 1
#total = 1 * 1=1
#total = 1 * 2=2
#total = 2 * 3=6
#total = 6 * 4=24
#total = 24 * 5=120

#fibonacci sequence
# def fibonacci(n):
#     #a, b = 0, 1
#     a=0
#     b=1
#     list = []
#     for k in range(n):
#         list.append(a)
#         #a, b = b, a + b
#         a=b
#         b=a+b
#     return list

#list=[]
#n=10
#K=0,1,2,3,4,5,6,7,8,9
#k=0,list=[0], a=1,b=1
#k=1,list=[0,1], a=1,b=2
#k=2,list=[0,1,1], a=2,b=3
#k=3,list=[0,1,1,2], a=3,b=5
#k=4,list=[0,1,1,2,3], a=5,b=8
#k=5,list=[0,1,1,2,3,5], a=8,b=13
#k=6,list=[0,1,1,2,3,5,8], a=13,b=21
#k=7,list=[0,1,1,2,3,5,8,13], a=21,b=34
#k=8,list=[0,1,1,2,3,5,8,13,21], a=34,b=55
#k=9,list=[0,1,1,2,3,5,8,13,21,34], a=55,b=89

#print(fibonacci(10))  # Example: Get first 10 Fibonacci numbers

#example of fibonacci sequence (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)

#palindrome
# def is_palindrome(word):
#     word = word.lower()  # Convert to lowercase for case-insensitive comparison
#     return word == word[::-1]  # Check if the string is equal to its reverse
# # Example usage
# print(is_palindrome("ada"))  # Output: True
# print(is_palindrome("Hello"))    # Output: False  

#convert character to ASCII value
#ASCII = American Standard Code for Information Interchange
#print(ord('A'))  # Output: 65
#print(ord('a'))  # Output: 97
#print(ord('0'))  # Output: 48
#print(ord(' '))  # Output: 32
#print(chr(65))  # Output: 'A'
#print(chr(97))  # Output: 'a'
#print(chr(48))  # Output: '0'
#print(chr(32))  # Output: ' '

#Sum of numbers from 1 to n
# def sum_of_numbers(n):
#     total = 0
#     for k in range(1, n + 1):
#         total += k
#     return total

#n=5
#total=0
#k=1, total=0+1=1
#k=2, total=1+2=3
#k=3, total=3+3=6
#k=4, total=6+4=10
#k=5, total=10+5=15
#print(sum_of_numbers(10))  # Output: 55
#print('--------Dictionaries----------')

#git basic tutoria for beginners
#how to create a repository

#how to clone a repository
#how to create a branch
#how to commit changes
#how to push changes to remote repository
#how to create a pull request
#how to merge a pull request
#how to resolve merge conflicts
#how to view commit history
#how to revert a commit
#how to delete a branch

