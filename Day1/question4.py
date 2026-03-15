# Input: a 5-digit number
num = int(input("enter a 5-digit number: "))

# Extract digits using arithmetic
d1 = num // 10000
d2 = (num // 1000) % 10
d3 = (num // 100) % 10
d4 = (num // 10) % 10
d5 = num % 10

# Sum of digits
digit_sum = d1 + d2 + d3 + d4 + d5

# Reverse the number (rebuild manually)
reversed_num = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1

print("Original number:", num)
print("Sum of digits:", digit_sum)
print("Reversed number:", reversed_num)