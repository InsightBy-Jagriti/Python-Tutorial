# Simulating do-while loop behavior in Python

# Example 1: Basic do-while simulation
count = 1

while True:
    print("Count:", count)
    count += 1

    if count > 5:
        break   # condition checked after execution


# Example 2: Password validation (real-world use case)
password = ""

while True:
    password = input("\nEnter password: ")

    if password == "python123":
        print("Access granted")
        break
    else:
        print("Wrong password, try again")


# Example 3: Menu-driven program
choice = 0

while True:
    print("\n1. Start")
    print("2. Settings")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 3:
        print("Exiting program...")
        break

