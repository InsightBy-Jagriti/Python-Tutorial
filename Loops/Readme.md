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

## 🔁 while Loop in Python

The **`while` loop** is used to repeatedly execute a block of code **as long as a given condition remains true**.  
Unlike the `for` loop, the number of iterations is **not fixed in advance**.

The loop stops automatically when the condition becomes **false**.

---

### ✔ Why use a while loop?
- When the number of repetitions is **unknown**
- When looping depends on a **condition**
- For continuous input or validation tasks
- For menu-driven programs

---

### ✔ How while Loop Works (Concept)

1. Python checks the condition  
2. If the condition is **True**, the loop body executes  
3. The condition is checked again  
4. This continues until the condition becomes **False**

---

### ✔ Important Rule
The condition **must change inside the loop**.  
If it does not change, the loop will run forever (infinite loop).

---

### ✔ Common Use Cases
- Counting until a limit is reached  
- Repeating until user gives correct input  
- Running programs with exit conditions  
- Games and menu-based systems  

---

### ✔ Key Points

| Concept | Description |
|-------|-------------|
| Condition | Checked before every iteration |
| Iterations | Unknown or condition-based |
| Control | Stops when condition becomes false |
| Risk | Infinite loop if condition never changes |
| Indentation | Defines loop body |

---

### ✔ while Loop vs for Loop

| Feature | while Loop | for Loop |
|-------|------------|----------|
| Iterations | Unknown | Known |
| Control | Condition-based | Sequence-based |
| Use Case | Validation, menus | Lists, ranges |

---


