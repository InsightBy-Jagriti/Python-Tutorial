# Polymorphism in Python

# --------------------------------------------------
# 1. Method Overriding Example
# --------------------------------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]

print("Polymorphism using method overriding:")
for animal in animals:
    animal.sound()


# --------------------------------------------------
# 2. Duck Typing Example
# --------------------------------------------------

class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def make_it_fly(obj):
    obj.fly()

print("\nPolymorphism using duck typing:")
make_it_fly(Bird())
make_it_fly(Airplane())


# --------------------------------------------------
# 3. Function Polymorphism Example
# --------------------------------------------------

print("\nFunction polymorphism:")
print(len("Python"))      # works on string
print(len([1, 2, 3, 4]))   # works on list


print("\nPolymorphism examples completed.")
