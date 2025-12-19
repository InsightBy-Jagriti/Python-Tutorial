# Logical Operators in Python

age = 22
has_id = True

print("Age:", age)
print("Has ID:", has_id)

print("\n--- Logical AND ---")
print(age >= 18 and has_id)

print("\n--- Logical OR ---")
print(age < 18 or has_id)

print("\n--- Logical NOT ---")
print(not has_id)

# Using logical operators in conditions
marks = int(input("\nEnter your marks: "))

if marks >= 40 and marks <= 100:
    print("You passed the exam.")
else:
    print("You failed the exam.")
