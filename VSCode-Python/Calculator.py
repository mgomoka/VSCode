'''
CALCULATOR
'''

# Addition Function
def add(x, y):
    return x + y

# Subtraction Function
def subtract(x, y):
    return x - y

# Multiplication Function
def multiply(x, y):
    return x * y

# Division Function
def divide(x, y):
    return x / y



# continueCalc = "Y" 

print("Please Select Operation:")
print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")

while True:
    # Store Input
    operation = input("Enter choice(1/2/3/4): ")

    # Checks Operation
    if operation in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operation == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operation == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
