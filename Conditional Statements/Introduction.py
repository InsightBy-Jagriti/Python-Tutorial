# Conditional Statements in Python
# Conditions help Python take decisions based on situations.

# --------------------------------------------------
# 1. Simple if statement
# --------------------------------------------------

age = 20

if age >= 18:
    print("You are eligible to vote.")
# If condition is false, nothing happens here


# --------------------------------------------------
# 2. if – else statement
# --------------------------------------------------

number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# --------------------------------------------------
# 3. if – elif – else statement
# --------------------------------------------------
# Used when there are multiple conditions

marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Fail")


# --------------------------------------------------
# 4. Nested if statement
# --------------------------------------------------
# if inside another if

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")


# --------------------------------------------------
# 5. Shorthand if (Ternary Operator)
# --------------------------------------------------
# Used when condition is very simple

age = int(input("\nEnter your age: "))

status = "Adult" if age >= 18 else "Minor"
print("Status:", status)


# --------------------------------------------------
# 6. Using logical operators in conditions
# --------------------------------------------------

salary = int(input("\nEnter salary: "))
experience = int(input("Enter years of experience: "))

if salary >= 30000 and experience >= 2:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# --------------------------------------------------
# End of conditional statements demo
# --------------------------------------------------
print("\nConditional statements practice completed ✔")
