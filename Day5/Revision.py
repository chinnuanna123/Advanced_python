# Variables and Data Types

#name = "Chinnu"
#age = 30
#height = 2.3
#is_employee = True
#hobbies = ["reading","Gardening","Cooking","travelling"]
#person_info = {
#    "Name": name,
#    "Age": age,
#    "height": height,
#    "is_employee": is_employee
#}
#print(f"Name : {name} Type : {type(name)}")
#print(f"Age : {age}  Type : {type(age)}")
#print(f"Height : {height}  Type: {type(height)}")
#print(f"is_employee : {is_employee} Type : {type(is_employee)}")
#print(f"Hobbies: {hobbies}  Type : {type(hobbies)}")
#print(f"Personal Information : {person_info}  Type : {type(person_info)}")


#OUTPUT

#Name : Chinnu Type : <class 'str'>
#Age : 30  Type : <class 'int'>
#Height : 2.3  Type: <class 'float'>
#is_employee : True Type : <class 'bool'>
#Hobbies: ['reading', 'Gardening', 'Cooking', 'travelling']  Type : <class 'list'>
#Personal Information : {'Name': 'Chinnu', 'Age': 30, 'height': 2.3, 'is_employee': True}  Type : <class 'dict'>


# Basic Control Flow


#number = int(input("Enter the Number: "))
#if number%3 == 0 and not number%5 ==0:
#    print("Fizz")
#elif number%5 ==0 and not number%3 ==0:
#      print("Buzz")
#elif (number%3 ==0 and number%5 ==0):
#   print("FIZZBUZZ")
#else:
#   print("number:",number)     


#OUTPUT


#  Enter the Number: 3
#  Fizz  
#  Enter the Number: 5
#  Buzz
#  Enter the Number: 15
#  FIZZBUZZ
#  Enter the Number: 17
#  number: 17


# For Loop: Print Numbers from 1 to 10

#for number in range(1,11):
#    print(number)

# OUTPUT
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10    


# While Loop: Sum of First N Numbers
#sum=0
#num = int(input("enter the Number:"))
#i=1
#while i<=num:
#    sum +=i
#    i +=1
#print(f"The sum of first {num} numbers is : {sum}")   


#OUTPUT

# enter the Number:5
# The sum of first 5 numbers is : 15


#  Functions

# Write a function that takes an integer n and returns the sum of all numbers from 1 to n

#def cal_sum(n):
#    sum = 0
#    for i in range(1,n+1):
#        sum +=i
#    return sum
#n = int(input("Enter the value of n : "))
#Total = cal_sum(n)
#print(f"The sum of all numbers from 1 to {n} is: {Total}")

# OUTPUT

# Enter the value of n : 5
# The sum of all numbers from 1 to 5 is: 15


# Function with Return Statement


#def square(n):
#    return n*n

#print(square(4))

# OUTPUT
#  16

# Function with Multiple Return Values
#def arithmetic_operations(a,b):
#    return a+b,a-b,a*b,a%b

#sum,sub,multi,div = arithmetic_operations(8,7)
#print(f"The Sum is : {sum} \n The difference is : {sub} \n The product is : {multi} \n The division is: {div}")


# OUTPUT

 #The Sum is : 15 
 #The difference is : 1 
 #The product is : 56 
 #The division is: 1


# Lambda Function

#cube = lambda x:x**3
#print(cube(2))

# OUTPUT
#8

# Exception Handling
#try:
#  num = int(input("enter the number: "))
#  value = 1/num
#  print("The value is :", value)
#except ZeroDivisionError:
#  print("Please enter a nonzero denominator!")
#finally:
#  print("The code executed successfully")


  #OUTPUT
#  enter the number: 0
#Please enter a nonzero denominator!

#enter the number: 7
#The value is : 0.14285714285714285
#The code executed successfully


#try:
#  a = input("enter a name:")
#  b= input("enter a number:")
#  b= int(input("enter a number:"))
#  print(a+b)
#except TypeError:
#  print("Only same data type can be Added:")
#finally:
#  print("code is executed")


# OUTPUT

#enter a name:Alice
#enter a number:12
#Only same data type can be Added:
#code is executed


#enter a name:Alice
#enter a number:12
#Alice12
#code is executed


#"Create a simple calculator that can perform basic arithmetic 
#operations: addition, subtraction, multiplication, and division."


#choice = int(input("Enter a number from (1 to 4): "))
#a = 8
#b = 7
#match choice:
#      case 1: 
#         print(f"The sum : {a+b}")
#      case 2:
#         print(f"The Difference: {a-b}")  
#      case 3:
#         print(f"The product: {a*b}") 
#      case 4:
#         print(f"The division: {a%b}")     
       
#      case 5:
#        print("Wrong Number!")

#         OUTPUT
# Enter a number from (1 to 4): 3
# The product: 56         
