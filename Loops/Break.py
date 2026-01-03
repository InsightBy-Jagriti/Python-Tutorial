# Break Statement in Python
# -------------------------
# The 'break' statement is used to stop a loop immediately.
# As soon as Python sees 'break', it exits the loop — even if the condition is still true.


# -------------------------------------------------------
# 1. Breaking a loop based on a condition
# -------------------------------------------------------

print("Example 1: Stop the loop when number reaches 5")

for number in range(1, 11):
    if number == 5:
        break   # loop stops right here
    print(number)

print("Loop ended because break was executed.\n")


# -------------------------------------------------------
# 2. Using break inside a while loop
# -------------------------------------------------------

print("Example 2: Asking user until they say STOP")

while True:
    user_input = input("Type STOP to exit: ")

    if user_input == "STOP":
        break   # user chooses to end the loop

    print("You typed:", user_input)

print("Exited the loop using break.\n")


# -------------------------------------------------------
# 3. Break used to find the first matching item
# -------------------------------------------------------

print("Example 3: Finding the first even number")

numbers = [3, 7, 9, 12, 15, 18]

for n in numbers:
    if n % 2 == 0:
        print("First even number found:", n)
        break   # stop after finding the first match

print("Search completed.\n")


# -------------------------------------------------------
# 4. break inside nested loops
# -------------------------------------------------------

print("Example 4: Break in nested loops")

for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

        if j == 1:
            break   # breaks ONLY the inner loop

    print("Inner loop ended for i =", i)

print("\nAll demonstrations completed.")

