# Object-Oriented Programming (OOP) Basics in Python

# --------------------------------------------------
# 1. Creating a Class
# --------------------------------------------------

class Student:
    # Constructor (runs when object is created)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display student details
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# --------------------------------------------------
# 2. Creating Objects
# --------------------------------------------------

student1 = Student("Jagriti", 22)
student2 = Student("Alex", 21)

student1.display_info()
print("----")
student2.display_info()


# --------------------------------------------------
# 3. Inheritance Example
# --------------------------------------------------

class Person:
    def greet(self):
        print("Hello! I am a person.")

class Teacher(Person):
    def teach(self):
        print("I teach Python.")

teacher = Teacher()
teacher.greet()
teacher.teach()


# --------------------------------------------------
# 4. Polymorphism Example
# --------------------------------------------------

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


print("\nOOP basics completed.")
