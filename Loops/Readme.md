**🔁 Loops in Python (Basics)**

Loops are used to repeat a block of code multiple times.
They help avoid writing the same code again and again.

Python mainly provides two types of loops:

for loop

while loop

| Loop Type | Purpose                                 |
| --------- | --------------------------------------- |
| `for`     | Used when number of iterations is known |
| `while`   | Used when condition controls repetition |

| Feature     | for Loop          | while Loop          |
| ----------- | ----------------- | ------------------- |
| Control     | Iteration-based   | Condition-based     |
| Use Case    | Known repetitions | Unknown repetitions |
| Readability | More concise      | More flexible       |

## 🔁 for Loop in Python

The **`for` loop** is used to **repeat a block of code** for each item in a sequence.  
It is commonly used when the **number of iterations is known in advance**.

The `for` loop works with sequences such as:
- lists
- tuples
- strings
- sets
- dictionaries
- ranges

---

### ✔ Why use a for loop?
- To iterate over data collections  
- To perform repeated tasks  
- To process elements one by one  
- To write cleaner and shorter code  

---

### ✔ How for Loop Works (Concept)

1. Python picks the **first item** from the sequence  
2. Executes the loop body  
3. Moves to the **next item**  
4. Repeats until all items are processed  

---

### ✔ Common Use Cases
- Looping through a list of items  
- Printing numbers in a range  
- Reading characters from a string  
- Processing dictionary keys or values  

---

### ✔ Key Points

| Concept | Description |
|-------|-------------|
| Iteration | Goes through items one by one |
| Sequence | List, tuple, string, range, etc. |
| Control | Stops automatically after last item |
| Indentation | Defines the loop body |
| Infinite Loop? | ❌ No (safe by default) |

---

### ✔ for Loop vs while Loop

| Feature | for Loop | while Loop |
|------|----------|------------|
| Iterations | Fixed / known | Unknown |
| Condition | Sequence-based | Condition-based |
| Usage | More common | More flexible |

---
