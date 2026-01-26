# Inheritance in Python

# --------------------------------------------------
# 1. Single Inheritance
# --------------------------------------------------

class Person:
    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def study(self):
        print("I am studying Python.")

student = Student()
student.greet()
student.study()


# --------------------------------------------------
# 2. Method Overriding
# --------------------------------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

dog = Dog()
dog.sound()


# --------------------------------------------------
# 3. Multilevel Inheritance
# --------------------------------------------------

class Grandparent:
    def show(self):
        print("I am Grandparent.")

class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent.")

class Child(Parent):
    def show_child(self):
        print("I am Child.")

child = Child()
child.show()
child.show_parent()
child.show_child()


# --------------------------------------------------
# 4. Multiple Inheritance
# --------------------------------------------------

class Father:
    def skill1(self):
        print("Father teaches discipline.")

class Mother:
    def skill2(self):
        print("Mother teaches kindness.")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()

print("\nInheritance examples completed.")
