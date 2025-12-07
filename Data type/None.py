# NoneType in Python

# None represents "no value" or "nothing"
result = None
data = None

print("Result:", result)
print("Data:", data)

# Checking the type
print("\nType of result:", type(result))

# None is often used as a placeholder
user_name = None  # We will assign real name later

print("\nUser name before assignment:", user_name)

# Now assigning value
user_name = "Jagriti"
print("User name after assignment:", user_name)

# None used in conditions
value = None

if value is None:
    print("\nValue is empty or not set yet.")
else:
    print("Value has data.")
