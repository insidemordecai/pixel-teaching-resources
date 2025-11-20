# Conditional Statements 
# They check if a certain condition is true or false and execute different block of code accordingly

name = input("What is your name? ")
age = int(input("How old are you? "))

# we want to check for teenagers (age 13 to 19)
if age >= 13 and age <= 19:
  print("Welcome to the teen club", name)
elif age > 19:
  print("Sorry ", name, ", you are too old 😂")
else:
  print("Sorry ", name, ", you need to be older to join the club!")

# task: try the above age comparison using a different code
# ALTERNATIVE 1
# if age >= 13:
#   if age >= 20:
#     print("You are too old 😂")
#   else:
#     print("Welcome to the teen club.")
# else:
#   print("You are too young 🙂")

# # ALTERNATIVE 2
# if age >= 13 and age <= 19:
#   print("Welcome to the teen club")
# else: 
#   if age >= 20:
#     print("You are too old 😂")
#   else: 
#     print("You are too young 🙂")

# task: perform math operation 
# ask the user for firstNumber, secondNumber and operator
# check the operator using a conditional statement to perform
# either addition or subtraction and print the result
