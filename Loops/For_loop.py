# Example of for loop in Python

# Looping through a list
fruits = ["apple", "banana", "mango"]

print("Fruits list:")
for fruit in fruits:
    print(fruit)

# Looping through a string
print("\nCharacters in name:")
for char in "Jagriti":
    print(char)

# Looping using range
print("\nNumbers from 1 to 5:")
for number in range(1, 6):
    print(number)

# Using for loop with dictionary
student = {
    "name": "Jagriti",
    "age": 22,
    "course": "Python"
}

print("\nStudent details:")
for key, value in student.items():
    print(key, ":", value)

print("\nfor loop execution completed.")

