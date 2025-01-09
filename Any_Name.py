def greet(name):
    """
    Function to greet a person with their name.
    """
    return f"Hello, {name}!"

def add(a, b):
    """
    Function to add two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Function to subtract two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Function to multiply two numbers.
    """
    return a * b

def divide(a, b):
    """
    Function to divide two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    """
    Main function to demonstrate the usage of the above functions.
    """
    name = "CS 202"
    print(greet(name))

    x, y = 10, 5
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")

if __name__ == "__main__":
    main()