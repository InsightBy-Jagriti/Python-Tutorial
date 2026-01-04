# Pass Statement in Python
# ------------------------
# The 'pass' statement is a placeholder used when you want to
# write a block of code but are not ready to add logic yet.
# It does nothing — Python simply skips it.

# -------------------------------------------------------
# 1. Using pass inside a loop
# -------------------------------------------------------

print("Example 1: pass inside a for loop")

for num in range(1, 6):
    if num == 3:
        pass    # placeholder – does nothing
    print("Number:", num)

print("\nWhen num == 3, 'pass' simply skipped that step.\n")


# -------------------------------------------------------
# 2. Using pass inside a function definition
# -------------------------------------------------------

print("Example 2: Defining an empty function")

def future_feature():
    pass    # function will be completed later

print("Function created but has no behavior yet.\n")


# -------------------------------------------------------
# 3. Using pass inside a conditional block
# -------------------------------------------------------

print("Example 3: pass in if condition")

age = 18

if age >= 18:
    pass    # logic will be added later
else:
    print("Not an adult")

print("Program continues normally.\n")


# -------------------------------------------------------
# 4. Using pass as a placeholder in classes
# -------------------------------------------------------

print("Example 4: pass in class definition")

class MyClass:
    pass    # class structure defined, logic pending

obj = MyClass()
print("Class created successfully with pass.\n")


print("All pass statement examples completed.")

