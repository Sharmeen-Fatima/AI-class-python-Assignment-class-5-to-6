# Function to perform arithmetic operations
def calculator():
    # User input for first number, operator, and second number
    num1 = int(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = int(input("Enter second number: "))
    
    # Check for the operator and perform corresponding operation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Adding condition to handle division by zero
        if num2 == 0:
            return "Error! Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Invalid operator! Please enter one of (+, -, *, /)."
    
    return f"The result of {num1} {operator} {num2} is: {result}"

# Call the function to run the calculator
print(calculator())