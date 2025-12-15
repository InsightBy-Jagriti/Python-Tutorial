# Input and Output Example in Python

# Taking input from user
name = input("Enter your name: ")
age = input("Enter your age: ")

print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)

# Type conversion
age = int(age)

# Using f-string for formatted output
print(f"\n{name} will be {age + 1} years old next year.")

# Taking numeric input directly
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
print("Sum:", sum_result)
