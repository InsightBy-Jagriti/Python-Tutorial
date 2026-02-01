## 🔄 Iterators in Python

An **iterator** is an object that allows you to **loop through a collection one element at a time**.

It follows two main rules:
- `__iter__()` → returns the iterator object  
- `__next__()` → returns the next item in the sequence  

When no items are left, it raises a **StopIteration** error.

---

## 🔹 Why Use Iterators?

- Efficient memory usage  
- Process items one by one  
- Useful for large datasets  
- Power behind loops like `for`  

---

## 🔹 Iterator vs Iterable

| Term | Meaning |
|------|--------|
| Iterable | Any object you can loop over (list, tuple, string) |
| Iterator | Object that remembers current position |

---

## 🔹 Built-in Iteration Flow

Python’s `for` loop internally uses iterators to fetch items step-by-step.

---

## 🔹 Key Benefits

- Saves memory  
- Works well with large data  
- Enables lazy processing  

---
## ⚙️ Generators in Python

A **generator** is a special type of function that **returns values one at a time** using the `yield` keyword.  
Unlike normal functions, generators **pause execution** and resume from where they left off.

Generators are memory-efficient and ideal for working with large data.

---

## 🔹 Why Use Generators?

- Saves memory  
- Produces values lazily  
- Improves performance  
- Useful for large or infinite data sequences  

---

## 🔹 Generator vs Normal Function

| Feature | Normal Function | Generator |
|--------|-----------------|-----------|
| Uses | `return` | `yield` |
| Memory | High | Low |
| Execution | Runs completely | Pauses and resumes |
| Output | Single value | Sequence of values |

---

## 🔹 Key Idea

Each time `yield` is executed, the function state is saved.  
On the next call, execution continues from the last `yield`.

---

## 🎁 Decorators in Python

A **decorator** is a function that **adds extra behavior** to another function **without modifying its code**.  
Decorators wrap a function and extend its functionality in a clean and reusable way.

Decorators are widely used for:
- logging
- authentication
- performance timing
- access control

---

## 🔹 Why Use Decorators?

- Keep code clean and DRY  
- Reuse common functionality  
- Separate concerns (logic vs extra behavior)  
- Improve readability and maintenance  

---

## 🔹 How Decorators Work (Concept)

1. A function is passed as an argument  
2. Another function wraps it  
3. Extra behavior runs **before or after** the original function  

---

## 🔹 Decorator Syntax

| Concept | Description |
|--------|-------------|
| Wrapper function | Adds extra behavior |
| `@decorator` | Cleaner decorator syntax |
| Inner function | Executes original function |

---

