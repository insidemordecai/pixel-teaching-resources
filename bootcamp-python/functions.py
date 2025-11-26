# functions provide us with reusability and organization of code

def prepare_dough():
  print("I'm preparing the dough...")

prepare_dough()

# how to include parameters in your functions
# task: create functions for different math operations
def add_numbers(a,b):
  return a + b

def subtract_numbers(a,b):
  return a - b

def divide_numbers(a,b):
  return a / b

def multiply_numbers(a,b):
  return a * b

def get_remainder(a,b):
  return a % b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

total = add_numbers(num1, num2)
subtraction_answer = subtract_numbers(num1, num2)
product = multiply_numbers(num1, num2)
division_answer = divide_numbers(num1, num2)
remainder = get_remainder(num1, num2)

print("The sum is", total)
print(num1, "minus",num2, "is", subtraction_answer)
print(num1, "multiplied by", num2, "is", product)
print(num1, "divided by", num2, "is", division_answer)
print("The remainder of", num1, "divided by", num2, "is", remainder)