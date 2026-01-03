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

**## 🔁 Do-While Loop in Python**

A **do-while loop** is a control structure where the loop body **executes at least once**,  
and the condition is checked **after** the execution.

This means:
- The code runs **first**
- The condition is checked **later**
- If the condition is true, the loop continues

---

### ❗ Important Note
Python does **not** have a built-in `do-while` loop like C, C++, or Java.  
However, we can **achieve the same behavior** using a `while` loop.

---

### ✔ How Do-While Logic Works

1. Execute the loop body once  
2. Check the condition  
3. If the condition is true → repeat  
4. If the condition is false → stop  

This guarantees **at least one execution**.

---

### ✔ When Do-While Logic Is Useful
- Menu-driven programs  
- Input validation  
- Password checks  
- Programs that must run once before checking condition  

---

### ✔ Comparison: while vs do-while

| Feature | while Loop | do-while Logic |
|-------|------------|---------------|
| Condition check | Before execution | After execution |
| Executes at least once | ❌ No | ✅ Yes |
| Native in Python | ✅ Yes | ❌ No (simulated) |

---

## 🔁 Break Statement in Python

The **`break` statement** is used to stop a loop immediately.  
As soon as Python encounters `break`, it exits the loop — even if the loop condition is still true.

This makes `break` useful when you want to stop a loop early based on some condition.

---

### ✔ Why use `break`?
- To stop looping when a condition is met  
- To exit infinite loops  
- To find the first matching item in a sequence  
- To break only the **current** loop (not outer loops)

---

### ✔ Key Points

| Concept | Description |
|--------|-------------|
| Purpose | Stops the loop immediately |
| Works in | `for` and `while` loops |
| After break | No further iterations are executed |
| Nested loops | Break affects only the inner loop |
| Common use | Validation, search, menu systems |

---

### ✔ Example Explanation
`break` checks a condition inside the loop.  
When the condition is satisfied, the loop terminates instantly and control moves outside the loop.

---



