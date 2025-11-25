# functions provide us with reusability and organization of code

def prepare_dough():
  print("I'm preparing the dough...")

prepare_dough()

# how to include parameters in your functions
def add_numbers(a,b):
  return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

total = add_numbers(num1, num2)
print("The sum is", total)