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

def factorial(a):
    if a < 0: 
        return "Factorial is not defined for negative numbers"
    else: 
        fact = 1
        for i in range(1, a + 1):
            fact *= i 
        return fact

# 2. Ask the user what to do
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Factorial")

choice = input("Choose 1, 2, 3, 4, or 5: ")

# 3. Get the two numbers
if choice == "5":
    num = int(input("Enter a non-negative integer: "))
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

# 4. Use if/elif to call the right function
if choice == "1":
    result = add_numbers(num1, num2)
    print("Result:", result)
elif choice == "2":
    result = subtract_numbers(num1, num2)
    print("Result:", result)
elif choice == "3":
    result = multiply_numbers(num1, num2)
    print("Result:", result)
elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        result = divide_numbers(num1, num2)
        print("Result:", result)
elif choice == "5":
    result = factorial(num)
    print("Result: ", result)
else:
    print("Invalid choice")