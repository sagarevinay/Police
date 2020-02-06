# name = input("What is your name????"'\n')
# color = input("What is your favourite color????"'\n')
# print(name +" likes "+ color)

# birth_year = input('Birth year : ')
# age = 2019 - int(birth_year)
# print(age)

# Weight_Kilogram = input("Please enter your weight in kilogram:")
# Weight_Pound = int(Weight_Kilogram) * 1.75
# print(Weight_Pound)

# Title = "This is python tutorial"
# Sub_Title = Title
# print(Sub_Title[1])
# print(Title[2])
# print(Title[-1])
# print(Title[0:8])
# print(Title[0:])
# print(Title[1:])
# print(Title[:9])
# print(Title[1:-1])

# First = "Vinay"
# Last = "Sagare"
# Message = f'{First} {Last} is a Coder'
# print(Message)

# Len Function
# Course = 'Python is programming language'
# print(len(Course))
# print(Course.upper())
# Course = 'VINAY SAGARE'
# print(Course.lower())
# Ans = len(Course) * 30
# print(Ans)
# print(Course.find('G'))
# print(Course.find('g'))

# in Function
# print('VINAY' in Course)
# print(Course.title())
# print(Course.replace('VINAY','MEGHA'))

# Arithmatic Operation
# print(10**3)

# Math Function
# x = 2.3
# y = 2.9
# z = -2.22
# print(round(x))
# print(round(y))
# print(abs(z))

# import math
# x = 2.3
# print(math.ceil(x))
# print(math.floor(x))

# Statements in Python
# is_hot = False
# is_cold = True
#
# if is_hot:
#     print("Its hot day")
# elif is_cold:
#     print("Its cold day")
# else:
#     print("Its Lovely Day")

# good_credit = False
# house_price = 1000000
# if good_credit:
#     House_Price = (house_price*10)/100
# else:
#     House_Price = (house_price*20)/100
# print(f"Your House rent is : {House_Price}")

# AND Operator
# good_credit = True
# good_personality = True
# has_Criminal_Record = True
# if good_credit and good_personality and not has_Criminal_Record:
#     print("Man is Perect")
# else:
#     print("Man is not Perfect")

# Comparator Operator
# good_credit = 1000000
# if good_credit >100000 :
#     print("Man is Perect")
# else:
#     print("Man is not Perfect")

#  Weight Converter
# Weight = int(input("Enter your Weight"))
# Unit = input('(L)bs or(K)g :')
# if Unit.upper() == "L":
#     Converted = Weight*45
#     print(f"you are {Converted} kilos")
# else:
#     Converted = Weight / 0.45
#     print(f"you are {Converted} pounds")

# While Loop
# Number = 9
# i = 0
# while 3 > i:
#     Input = int(input("Enter Guess number: "))
#     i +=1
#     if Input == Number:
#         print("You Win")
#         break
# else:
#     print("Sorry, You failed")

# For Loops
# for item in 'PYTHON':
#     print(item)
#
# for item in ['Vinay','Sagare']:
#     print(item)
#
# for item in range(1,10,):
#     print(item)
#
# for item in range(1,10,3):
#     print(item)

# NestedLoops
# for x in range(4):
#     for y in range(3):
#         print(f'({x} ,{y})')

# Number = [5,2,5,2,2]
# for x in Number:
#     print('x' * x)

# Number_List = [1,2,3,5,65,34,78,98,23,45,7,6,76,89,91,95,33]
# gretest_number = 0
# for x in Number_List:
#     if x > gretest_number:
#         gretest_number = x
# print(gretest_number)

# 2 Dimensional List
# matrix = [
#     [1,2,3],[4,5,6],[7,8,9]
# ]
# matrix[0][1] = 2000
# print(matrix[0][1])

# Numbers = [12,10,34,24]
# Numbers.append(20)
# print(Numbers)
# Numbers.insert(0,111)
# print(Numbers)
# Numbers.remove(111)
# Numbers.sort()
# print(Numbers)

# Numbers = [1,2,3,4,5,3,4]
# uniques = []
# for x in Numbers:
#     if x not in uniques:
#         uniques.append(x)
# print(uniques)

# Tuple Concept
# Numbers = (1,2,3,4,5)
# print(Numbers[0])
# Numbers[0] = 12  #TypeError: 'tuple' object does not support item assignment
# print(Numbers[0])

# Tuple Unpacking Concept
# Numbers = (1,2,3,4,5)
# x,y,z,a,b = Numbers
# print(x,y)

# Exceptional handling
# try:
#     Number = input("Enter the number")
#     Answer = int(Number) * 10
#     print(f'your answer is: {Answer}')
#     Number1 = 20/ int(Number)
#     print(Number1)
# except ZeroDivisionError:
#     print("Zero dividation error")
# except ValueError:
#     print("Invalide input")

# class concept
# class Example:
#     def Numbers(self):
#         Num = input("enter your number: ")
#         if int(Num)>10 :
#             print (f'{Num} is greater than 10')
#         else:
#             print(f'{Num} is less than 10')
#     def String(self):
#         Stirngs = input("Enter a string :")
#         print(f'you have enterd: {Stirngs}')
#
# Numerical = Example()
# Numerical.Numbers()
# Numerical.String()

# Accessing methods from anather class
# import NumString
# NumString.Numbers(self=2)
# NumString.String(self=1)

# Random Function
# import random
#
# class Random_fun: 
#     def Ran(self):
#         members = ["vinay","satish","naresh","paras"]
#         first = random.randint(1,2)
#         second = random.choice(members)
#         return (first,second)
#
# Answer = Random_fun()
# print(Answer.Ran())
#
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
# print(f'Your answer is :{factorial(5)}')

# Name = input("Please enter your name: ")
# Surname = input("Please enter your surname: ")
#
# message = "Hello %s %s" %(Name, Surname)
# print(message)

# def concatinate(phrase):
#     interrogatives = ("how", "what", "what")
#     capitalized = phrase.capitalize()
#     if phrase.startswith(interrogatives):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)
#
# results = []
# while True:
#     user_input = input("say something: ")
#     if user_input=="end":
#         break
#     else:
#         results.append(concatinate(user_input))
#
# print(" ".join(results))

# List comprehensions
# number_list = [200, 320, 345, 243, 435]
# Num_temp = [Num / 10 for Num in number_list]
# print(Num_temp)

# number_list = [200, 320, -345, 243, 435]
# for Num in number_list:
#     if Num < 0:
#         Num_temp = (Num * -1) / 10
#     else:
#         Num_temp = (Num / 10)
#     print(Num_temp)
#
# Num_temp = [Num / 10 for Num in number_list if Num < 0]
# print(Num_temp)
# Num_temp = [Num / 10 for Num in number_list if Num > 0]
# print(Num_temp)

# File operations
# myfile = open("/home/vinay/PycharmProjects/Police/Police/MyApplication/venv/fruits.txt")
# print(myfile.read())
#
# with open("/home/vinay/PycharmProjects/Police/Police/MyApplication/venv/fruits.txt") as myfile:
#     content = myfile.read()
#     print(content)
