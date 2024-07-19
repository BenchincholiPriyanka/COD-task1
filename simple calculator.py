def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    result = float('inf')  # positive infinity
                else:
                    result = num1 / num2
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result}")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except ZeroDivisionError:
            print("Division by zero is not allowed!")

        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            break

print("Simple Calculator")
calculator()
