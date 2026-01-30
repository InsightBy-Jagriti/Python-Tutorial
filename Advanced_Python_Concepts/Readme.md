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
