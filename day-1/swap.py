# Input the numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print the original values
print("Before swapping:")
print("First number =", num1)
print("Second number =", num2)

# Swap the values
temp = num1
num1 = num2
num2 = temp

# Print the swapped values
print("After swapping:")
print("First number =", num1)
print("Second number =", num2)
# Swap the values again
num1, num2 = num2, num1

# Print the swapped values again
print("After swapping again:")
print("First number =", num1)
print("Second number =", num2)