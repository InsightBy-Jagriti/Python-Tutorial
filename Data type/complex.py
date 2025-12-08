# Complex Data Type in Python

# A complex number has two parts: real + imaginary
num1 = 3 + 4j
num2 = 2 - 1j
num3 = 5j      # only imaginary part
num4 = 10      # a normal integer (not complex)

print("num1 =", num1)
print("num2 =", num2)
print("num3 =", num3)
print("num4 =", num4)

# Accessing real and imaginary parts
print("\n--- Real & Imaginary Parts ---")
print("Real part of num1:", num1.real)
print("Imag part of num1:", num1.imag)

print("Real part of num2:", num2.real)
print("Imag part of num2:", num2.imag)

# Basic operations
print("\n--- Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Type checking
print("\nType of num1:", type(num1))
