# python_script.py

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer.

    Returns:
        int: The factorial of n. Returns 1 if n is 0.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    # Example usage of the factorial function
    try:
        num1 = 5
        print(f"The factorial of {num1} is: {factorial(num1)}") # Expected: 120

        num2 = 0
        print(f"The factorial of {num2} is: {factorial(num2)}") # Expected: 1

        num3 = 7
        print(f"The factorial of {num3} is: {factorial(num3)}") # Expected: 5040

        # Example of invalid input
        # num4 = -3
        # print(f"The factorial of {num4} is: {factorial(num4)}")

        # num5 = 4.5
        # print(f"The factorial of {num5} is: {factorial(num5)}")

    except ValueError as e:
        print(f"Error: {e}")

    print("\nThis is a simple Python script.")
    print("You can replace this code with your own projects and upload it to GitHub!")
