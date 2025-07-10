class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

calc = Calculator()
print("Welcome to the Simple Calculator!")
print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("Type 'exit' to quit.")

while True:
    choice = input("Enter your choice (1/2/3/4/exit): ")

    if choice == 'exit':
        print("Exiting the calculator. Goodbye!")
        break

    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = calc.add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = calc.subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = calc.multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = calc.divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please choose 1, 2, 3, 4, or 'exit'.")
