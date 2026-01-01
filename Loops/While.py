# Example of while loop in Python

# 1. Simple counting loop
count = 1

print("Counting from 1 to 5:")
while count <= 5:
    print(count)
    count += 1   # condition update

# 2. Using while loop for user input
password = ""

while password != "python123":
    password = input("\nEnter the password: ")

print("Access granted!")

# 3. Using while loop with break
number = 1

print("\nPrinting numbers until 3:")
while True:
    print(number)
    number += 1
    if number > 3:
        break

print("\nwhile loop execution completed.")

