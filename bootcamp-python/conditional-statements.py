# Conditional Statements 
# They check if a certain condition is true or false and execute different block of code accordingly

age = 15

# we want to check for teenagers (age 13 to 19)
if age >= 13 and age <= 19:
  print("You are in the teen club")
elif age > 19:
  print("You are too old 😂")
else:
  print("Sorry, you need to be older to join the club!")

# task: try the above age comparison using a different code
# OPTION 1
# if age >= 13
#   if age >= 20
#     too old
#   else
#     teen club
# else
#   too young

if age >= 13:
  if age >= 20:
    print("You are too old 😂")
  else:
    print("Welcome to the teen club.")
else:
  print("You are too young 🙂")

# OPTION 2
# if age >= 13 and age <= 19 
#   teen club
# else
#   if age >= 20 
#     too old
#   else 
#     too young

if age >= 13 and age <= 19:
  print("Welcome to the teen club")
else: 
  if age >= 20:
    print("You are too old 😂")
  else: 
    print("You are too young 🙂")