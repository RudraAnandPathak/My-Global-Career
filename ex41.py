# Function to count digits in a number
def count_digits(number):
    return len(str(abs(number)))

# Example usage
num = int(input())
print("Number of digits:", count_digits(num))
