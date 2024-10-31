# 1 AttributeError

# number = 10
# number.append(10)

# class function:
#     pass

# fn = function()
# fn.run()

# 2 Import error

# import subscribe

# 3 syntax error

# x = 'hello'

# print("hello")

# def fun():
#     pass

# 4 Type error

# print("hello" + 10) 

# 5 Index Error

# numbers = [1, 2, 3]

# print(numbers[10])

# 6 Name error

# def something():
#     x = 10
# print(x)

# print(hello)

# 8 Recursion error
# def func():
#     func()

# func()

# 9 Indentation error

# def hello():
#     print("hello")

# hello()

# 10 Value error

# import math

# print(math.sqrt(-10))

# number = int("hello")
# print(number)

# 11 Runtime error

# num1 = 11
# num2 = 0

# print(num1/num2)

#12 logical error

# num = [10,20,30,40,50]

# total = 0

# for i in num:
#     total += i

# ave = total/len(num)-1

# print(ave)

# ERROR HANDLING

# try:
#     x = int(input("numbers"))
#     result = 10/x
# except ZeroDivisionError:
#     print("cant divide by zero")

# except ValueError:
#     print("incorrect input")

# try:
#     result = 3/0
# except ZeroDivisionError:
#     print("cant divide by zero")
# else:
#     print(result)

# try:
#     result = 3/0
# except ZeroDivisionError: #fileNotFoundError
#     print("cant divide by zero")
# else:
#     print(result) #read file

# finally:
#     print("always executed")

# x = int(input("number1"))
# y = int(input("number2"))

# if x == 0:
#     print("can't divide by zero")

# else:
#     print(y/x)

try:
    x = int(input("numbers"))
    result = 10/x

except (ValueError, ZeroDivisionError):
    print("incorrect")