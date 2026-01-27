##  Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming approach that organizes code into **objects** and **classes**.  
It helps in building **scalable, reusable, and real-world-based** programs.

OOP is based on the idea of modeling real-world entities like students, cars, employees, etc.

---

## 🔹 Core Concepts of OOP

| Concept | Description |
|--------|-------------|
| Class | Blueprint or template for creating objects |
| Object | Instance of a class |
| Attributes | Data stored inside an object |
| Methods | Functions that belong to a class |
| Encapsulation | Hiding internal data |
| Inheritance | Reusing features from a parent class |
| Polymorphism | One function, multiple behaviors |
| Abstraction | Showing only essential details |

---

## 🔹 Why Use OOP?

- Makes code more organized  
- Encourages reusability  
- Models real-world problems easily  
- Easier to maintain and scale  
- Improves code readability  

---

## 🔹 Real-World Example

A **class** is like a blueprint of a **Student**.  
An **object** is an actual student created using that blueprint.

---

## 🔹 OOP Topics Covered

- Classes and Objects  
- Constructors (`__init__`)  
- Instance variables and methods  
- Inheritance  
- Polymorphism  
- Encapsulation  
- Abstraction  

---

## 🧱 Classes & Objects in Python

A **class** is a blueprint or template used to create objects.  
An **object** is an instance of a class that contains real data and behavior.

Classes define **attributes** (data) and **methods** (functions).  
Objects use those attributes and methods to perform actions.

---

## 🔹 Class vs Object

| Term | Description |
|------|-------------|
| Class | Blueprint or design |
| Object | Real instance of a class |
| Attributes | Data stored in an object |
| Methods | Functions defined in a class |

---

## 🔹 Why Use Classes & Objects?

- Organize code better  
- Represent real-world entities  
- Improve reusability  
- Make programs scalable and modular  

---

## 🔹 Real-World Example

A **class** is like a design of a **Car**.  
An **object** is an actual car created from that design.

---

## 🔹 Key Concepts

- Class defines structure  
- Object stores real values  
- Multiple objects can be created from one class  
- Each object has its own data  

---
## 🏗 Constructors (`__init__`) in Python

A **constructor** is a special method in a class that is **automatically called when an object is created**.  
It is mainly used to **initialize object attributes**.

In Python, the constructor method is named **`__init__`**.

---

## 🔹 Why Use a Constructor?

- To assign initial values to object attributes  
- To ensure objects start with valid data  
- To reduce repetitive code  
- To make object creation more organized  

---

## 🔹 Key Points About `__init__`

| Concept | Description |
|--------|-------------|
| Method Name | `__init__` |
| Called When | Object is created |
| Purpose | Initialize object data |
| Uses `self` | Refers to the current object |
| Runs Automatically | Yes |

---

## 🔹 Constructor vs Normal Method

| Feature | Constructor | Normal Method |
|--------|------------|---------------|
| Called Automatically | ✅ Yes | ❌ No |
| Used for Setup | ✅ Yes | ❌ Usually no |
| Name Fixed | `__init__` | Any name |

---

## 🔹 Real-World Example

A constructor is like **filling a form when creating a new account** —  
every object gets its own personalized data.

---

## 🧬 Inheritance in Python

**Inheritance** allows a class to **reuse properties and methods** from another class.  
The class being inherited from is called the **Parent (Base) Class**,  
and the class that inherits is called the **Child (Derived) Class**.

This helps reduce code duplication and improves reusability.

---

## 🔹 Why Use Inheritance?

- Reuse existing code  
- Create hierarchical relationships  
- Extend features of existing classes  
- Keep programs organized and scalable  

---

## 🔹 Key Terms

| Term | Description |
|------|-------------|
| Parent Class | Class being inherited from |
| Child Class | Class that inherits features |
| Inheritance | Process of reusing class features |
| Override | Redefining a parent method in child |

---

## 🔹 Types of Inheritance

| Type | Description |
|------|-------------|
| Single | One child inherits one parent |
| Multiple | One child inherits multiple parents |
| Multilevel | Child inherits from another child |
| Hierarchical | Multiple children inherit one parent |

---

## 🔹 Real-World Example

A **Person** class can be inherited by **Student** and **Teacher**,  
so both reuse common behavior like name and greeting.

---

## 🔒 Encapsulation in Python

**Encapsulation** is an OOP concept that **hides internal data** and allows access only through controlled methods.  
It helps protect data from being modified directly and keeps code more secure and organized.

Encapsulation is achieved using:
- Public variables  
- Protected variables (`_variable`)  
- Private variables (`__variable`)  

---

## 🔹 Why Use Encapsulation?

- Protects sensitive data  
- Prevents accidental modification  
- Improves code security  
- Makes code easier to maintain  
- Encourages controlled access  

---

## 🔹 Access Levels in Python

| Type | Syntax | Meaning |
|------|--------|--------|
| Public | `name` | Accessible anywhere |
| Protected | `_name` | Should be accessed inside class/subclass |
| Private | `__name` | Accessible only inside the class |

---

## 🔹 Key Idea

Encapsulation allows you to **control how data is accessed and changed**,  
instead of exposing everything directly.

---
