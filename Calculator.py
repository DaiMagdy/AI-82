"""
Calculator Class

This class represents a simple calculator that performs basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division (with zero division check)

It takes two float numbers as input and provides methods to perform the operations.
"""



class Calculator:

    def __init__(self, x: float, y: float):
        """
        Initializes the calculator with two numbers.
        """
        self.x=x
        self.y=y
        

    def add(self):
        '''
        this function sum two number and return the sum
        type_return:float
        '''
        return self.x + self.y
    

    def subtract(self):
        '''
        this function substract two number and return the result
        type_return:float
        '''
        return self.x - self.y
    


    def multiply(self):
        '''
        this function multiply two number and return the result
        type_return:float
        '''
        return self.x * self.y
    


    def divide(self):
       '''
       Divides one number by another.
       and return the result.
       type_return:float or str: Error message if division by zero.
       '''
       if self.y == 0:
            return "Cannot divide by zero"
       return self.x / self.y
    

if __name__ == "__main__":

    # Simple Calculator Program
    while True:
        print("Welcome to the Simple Calculator!")
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("Type 'exit' to quit.")
        choice = input("Enter your choice (1/2/3/4/exit): ")
        
        # Check if the user wants to exit
        if choice == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        # Validate the choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please choose 1, 2, 3, 4, or 'exit'.")
            continue

        # Get numbers from the user
        print("Please enter two numbers:")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        calc = Calculator(num1, num2)

        # Perform the chosen operation
        if choice == '1':
            result = calc.add()
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = calc.subtract()
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = calc.multiply()
            print(f"{num1} * {num2} = {result}")
        else: # choice == '4'
            result = calc.divide()
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")

    

    ###Good job thank you so much




        


