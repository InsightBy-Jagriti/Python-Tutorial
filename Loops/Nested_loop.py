# Nested Loops in Python
# ---------------------
# One loop running inside another loop

# -------------------------------------------------------
# 1. Basic nested for loop
# -------------------------------------------------------

print("Example 1: Nested for loop")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
    print("Inner loop completed for i =", i)

print("\n")


# -------------------------------------------------------
# 2. Nested loop for pattern printing
# -------------------------------------------------------

print("Example 2: Star pattern")

for row in range(1, 5):
    for col in range(row):
        print("*", end=" ")
    print()

print("\n")


# -------------------------------------------------------
# 3. Nested loop with break
# -------------------------------------------------------

print("Example 3: break in nested loop")

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break   # breaks only inner loop
        print(f"i={i}, j={j}")
    print("Inner loop stopped, outer continues")

print("\n")


# -------------------------------------------------------
# 4. Nested loop using while
# -------------------------------------------------------

print("Example 4: Nested while loop")

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

print("\nNested loops execution completed.")
