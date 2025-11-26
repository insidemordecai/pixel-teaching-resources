# a simple calculator that allows the use to choose their desired operation

# 1. Define functions
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b  # assume b is not 0 for now

# 2. Ask the user what to do
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose 1, 2, 3, or 4: ")

# 3. Get the two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 4. Use if/elif to call the right function