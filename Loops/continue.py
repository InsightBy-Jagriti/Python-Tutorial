# Continue Statement in Python
# ----------------------------
# The 'continue' statement skips the current iteration of a loop
# and moves directly to the next iteration.

# -------------------------------------------------------
# 1. Using continue in a for loop
# -------------------------------------------------------

print("Example 1: Skip number 3")

for num in range(1, 6):
    if num == 3:
        continue   # skip this iteration
    print("Number:", num)

print("Loop finished.\n")


# -------------------------------------------------------
# 2. Using continue in a while loop
# -------------------------------------------------------

print("Example 2: Skip even numbers")

count = 0

while count < 6:
    count += 1
    if count % 2 == 0:
        continue   # skip even numbers
    print("Odd number:", count)

print("While loop finished.\n")


# -------------------------------------------------------
# 3. Continue with user input
# -------------------------------------------------------

print("Example 3: Skip empty input")

while True:
    text = input("Enter something (type exit to stop): ")

    if text == "":
        continue   # ignore empty input

    if text == "exit":
        break

    print("You entered:", text)

print("Program ended.")
