# Dictionary Example in Python

# A dictionary stores key-value pairs.
student = {
    "name": "Jagriti",
    "age": 22,
    "course": "Python"
}

print("Student Dictionary:", student)

# Accessing values
print("\nName:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["city"] = "Delhi"
print("\nAfter adding city:", student)

# Updating values
student["age"] = 23
print("After updating age:", student)

# Removing a key
student.pop("course")
print("After removing course:", student)

# Looping through dictionary
print("\nLooping through keys & values:")
for key, value in student.items():
    print(key, ":", value)

# Checking type
print("\nType:", type(student))
