***Conditional Statements in Python***

Conditional statements allow a program to make decisions.
They check a condition and execute different actions based on whether the condition is true or false.

Python uses conditional statements to control the flow of execution.

**Types of Conditional Statements**
| Statement Type | Purpose                                   |
| -------------- | ----------------------------------------- |
| `if`           | Executes a block when a condition is true |
| `if–else`      | Chooses between two actions               |
| `if–elif–else` | Handles multiple conditions               |

**Comparison Operators Used in Conditions**
| Operator | Description              |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

## 🧩 if Statement 

The **`if` statement** allows a program to make decisions.  
It runs a block of code **only when the given condition is true**.  
If the condition is false, Python simply skips that block.

### ✔ Why use `if`?
- To check user inputs  
- To validate data  
- To control program flow  
- For simple decision-making  

### ✔ Key Points
| Concept      | Description                                |
|--------------|--------------------------------------------|
| Condition    | Must evaluate to True or False             |
| Execution    | Runs only when condition is true           |
| else needed? | No, it's optional                          |
| Use Case     | Single-condition checks                    |
| Indentation  | Defines which code belongs to the `if`     |

### ✔ Example Explanation
The `if` checks whether a condition is true.  
If it is true → the message prints.  
If false → nothing happens.

## 🧩 if–else Statement

The **`if–else` statement** is used when a program must choose between **two possible outcomes**.  
If the condition is true, the `if` block runs.  
If the condition is false, the `else` block runs.

### ✔ Why use `if–else`?
- When there are exactly two choices  
- To handle yes/no decisions  
- To control alternative program flow  

### ✔ Key Points
| Concept      | Description                                      |
|--------------|--------------------------------------------------|
| Condition    | Must return True or False                        |
| if block    | Executes when condition is true                 |
| else block  | Executes when condition is false                |
| Use Case    | Two-way decision making                         |
| Indentation | Required for defining blocks                    |

### ✔ Example Explanation
Python checks the condition.  
If it is true → code inside `if` runs.  
Otherwise → code inside `else` runs.


## 🧩 if–elif–else Statement 

The **`if–elif–else` statement** is used when a program needs to check **multiple conditions**.  
Python evaluates conditions from top to bottom and executes **only the first true block**.  
If none of the conditions are true, the `else` block runs.

### ✔ Why use `if–elif–else`?
- When there are more than two choices  
- To avoid writing multiple separate `if` statements  
- To handle multiple decision paths  

### ✔ Key Points
| Concept        | Description                                      |
|----------------|--------------------------------------------------|
| if             | First condition check                            |
| elif           | Checked only if previous condition is false      |
| else           | Executes when all conditions are false           |
| Execution      | Only one block runs                              |
| Use Case       | Multiple condition decision making               |

### ✔ Example Explanation
Python checks each condition in order.  
As soon as one condition is true, its block executes and the rest are skipped.

## 🧩 Nested if Statement

A **Nested if statement** means placing one `if` statement inside another `if`.  
It is used when a condition depends on another condition being true first.

### ✔ Why use Nested if?
- When decisions are dependent on previous checks  
- For multi-level validation  
- For step-by-step decision making  

### ✔ Key Points
| Concept        | Description                                      |
|----------------|--------------------------------------------------|
| Nested if      | `if` inside another `if`                         |
| Dependency     | Inner condition runs only if outer is true       |
| Complexity     | Used for layered logic                           |
| Use Case       | Login checks, eligibility checks, validations    |

### ✔ Example Explanation
First, Python checks the **outer condition**.  
If it is true, then the **inner condition** is checked.  
If the outer condition is false, inner checks are skipped.

