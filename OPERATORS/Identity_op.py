# Identity Operators in Python

a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

print("a is b:", a is b)
print("a is not b:", a is not b)

print("\nList comparison:")
print("c == d:", c == d)      # values are same
print("c is d:", c is d)      # memory is different

# Correct use with None
result = None

if result is None:
    print("\nResult is not set yet")
