def find_last_digit(number):
    """
    Returns the last digit of the given number.
    
    Parameters:
        number (int): The input number.
    
    Returns:
        int: The last digit of the number.
    """
    return abs(number) % 10

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The last digit of {num} is {find_last_digit(num)}.")        