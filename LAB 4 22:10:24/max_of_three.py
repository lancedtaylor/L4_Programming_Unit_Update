def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Determine the maximum of the three numbers
    maximum = max(num1, num2, num3)
    
    return maximum

# Example usage:
maximum = max_of_three(10, 20, 30)
print(maximum, "is the maximum")
