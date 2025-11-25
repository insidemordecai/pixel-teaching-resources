# Loops allow the computer to repeat a block of code multiple times
# Types of Loops: For Loop & While Loop

# For loops are used to repeat a block of code a specific number of times or over a collection of items
for i in range(5):
  print("Hello world!")

# While loops are used to repeat a block of code as long as a certain condition is true
count = 0

while count < 3:
  print("Mark is annoying and Merossa is violent.")
  count += 1

count = 3

while count > 0:
  print("Mark is violent and Merossa is annoying.")
  count -= 1

# task: print a right-angled triangle of stars 
for i in range(1,6):
  print("*" * i)

# task: perform addition and multiplication of numbers in a list
numbers = [4,5,6,7]
total = 0 
product = 1
for num in numbers:
  total += num
  product *= num
  
print("The total is", total, "and the product is", product) 
