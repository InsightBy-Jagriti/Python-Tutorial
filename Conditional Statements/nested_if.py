# Example of Nested if statement in Python

username = input("Enter username: ")
password = input("Enter password: ")

# Outer condition
if username == "admin":
    
    # Inner condition
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")

else:
    print("User not found")

print("Login process completed.")
