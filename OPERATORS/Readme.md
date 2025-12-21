🧩 What are Operators in Python?

Operators are symbols that tell Python to perform an action.
They work on values and variables to do tasks like calculations, comparisons, and decision-making.

Example:

a + b
a > b
x and y

✔ Types of Operators
1️⃣ Arithmetic Operators

Used for basic math.
+ - * / // % **

2️⃣ Comparison Operators

Used to compare two values.
== != > < >= <=

3️⃣ Logical Operators

Used for True/False conditions.
and or not

4️⃣ Assignment Operators

Used to assign or update values.
= += -= *= /= %=

5️⃣ Membership Operators

Check if a value exists inside another.
in not in

6️⃣ Identity Operators

Check if two variables refer to the same memory.
is is not

7️⃣ Bitwise Operators

Work on numbers at the binary level.
& | ^ ~ << >>

✔ Why operators are important?

Perform calculations

Compare values

Create decision-based logic

Build conditions for loops & functions

Work with data structures

***WHAT IS ARITHMETIC OPERATOR***

Arithmetic operators are used to perform mathematical calculations on numbers like addition, subtraction, multiplication, etc.

They mostly work with int and float data types.

✔ Types of Arithmetic Operators
Operator	Meaning
+	Addition, 
-	Subtraction, 
*	Multiplication, 
/	Division, 
//	Floor Division,           
%	Modulus (Remainder), 
**	Exponent (Power), 
✔ Examples
a = 10
b = 3

print(a + b)    # 13

print(a - b)    # 7

print(a * b)    # 30

print(a / b)    # 3.333...

print(a // b)   # 3

print(a % b)    # 1

print(a ** b)   # 1000

***What are Comparison Operators?***

Comparison operators are used to compare two values.
They always return a boolean result → True or False.

These operators help in decisions, conditions, and if-else statements.

✔ List of Comparison Operators
Operator	Meaning
==	Equal to
!=	Not equal to
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to


| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |



***What are Logical Operators?***

Logical operators are used to combine conditions.
They work with boolean values (True / False) and return a boolean result.

They are mainly used in if-else statements, loops, and validations.

✔ Types of Logical Operators
Operator	Meaning :-
and	True if both conditions are true
or	True if at least one condition is true
not	Reverses the result

| Operator | Meaning                                    |
| -------- | ------------------------------------------ |
| `and`    | True if **both** conditions are true       |
| `or`     | True if **at least one** condition is true |
| `not`    | Reverses the result                        |



***What are Assignment Operators?***

Assignment operators are used to assign values to variables
and update existing values in a short and simple way.

They help reduce code length and improve readability.

Types of Assignment Operators
| Operator | Meaning                 |
| -------- | ----------------------- |
| `=`      | Assign value            |
| `+=`     | Add and assign          |
| `-=`     | Subtract and assign     |
| `*=`     | Multiply and assign     |
| `/=`     | Divide and assign       |
| `//=`    | Floor divide and assign |
| `%=`     | Modulus and assign      |
| `**=`    | Power and assign        |

***What are Membership Operators?***

Membership operators are used to check whether a value exists inside a sequence or collection like a list, tuple, string, set, or dictionary.

They return True or False.



x = 10

x += 5   # same as x = x + 5

x *= 2   # same as x = x * 2

*Types of Membership Operators*

| Operator | Meaning                              |
| -------- | ------------------------------------ |
| `in`     | Returns True if value is present     |
| `not in` | Returns True if value is not present |

Example

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)      # True

print("grapes" not in fruits) # True

