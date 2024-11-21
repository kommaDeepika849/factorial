def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

from functools import reduce

def factorial_functional(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Iterative")
    print("2. Recursive")
    print("3. Functional")
    
    choice = int(input("Enter your choice (1/2/3): "))
    number = int(input("Enter the number to calculate the factorial: "))
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        if choice == 1:
            print(f"Factorial of {number} using iterative approach is: {factorial_iterative(number)}")
        elif choice == 2:
            print(f"Factorial of {number} using recursive approach is: {factorial_recursive(number)}")
        elif choice == 3:
            print(f"Factorial of {number} using functional approach is: {factorial_functional(number)}")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
