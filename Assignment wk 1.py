# Step 1: Get the first number from user
num1 = float(input("Enter the first number: "))

# Step 2: Get the second number from user
num2 = float(input("Enter the second number: "))

# Step 3: Get the operation from user
operation = input("Enter the operation (+, -, *, /): ")

# Step 4: Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operation."

# Step 5: Display the result
if isinstance(result, float):
    print(f"{num1} {operation} {num2} = {result}")
else:
    # result contains an error message string
    print(result)
