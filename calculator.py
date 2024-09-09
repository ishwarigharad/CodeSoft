def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference between x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x divided by y."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    """Main function to perform the calculator operations."""
    print("Simple Calculator")
    
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

       
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter the number of the operation (1/2/3/4): ").strip()

    
        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        else:
            print("Invalid input. Please select a valid operation.")
            return
        
       
        if isinstance(result, str):  
            print(result)
        else:
            print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
