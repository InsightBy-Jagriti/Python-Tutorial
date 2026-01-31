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
