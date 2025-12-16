# Python Operators Example

a = 10
b = 3

print("--- Arithmetic Operators ---")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)   # floor division
print("a % b =", a % b)     # remainder
print("a ** b =", a ** b)   # power

print("\n--- Comparison Operators ---")
print("a > b:", a > b)
print("a == 10:", a == 10)
print("a != b:", a != b)

print("\n--- Logical Operators ---")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\n--- Assignment Operators ---")
c = 5
c += 3
print("c += 3:", c)
c *= 2
print("c *= 2:", c)

print("\n--- Membership Operators ---")
items = [1, 2, 3, 4]
print("2 in items:", 2 in items)
print("5 not in items:", 5 not in items)

print("\n--- Identity Operators ---")
p = 10
q = 10
print("p is q:", p is q)
print("p is not q:", p is not q)
