##  File Handling in Python

File handling allows Python programs to **read data from files** and **write data to files**.  
It is useful when data needs to be stored permanently or shared between programs.

Python provides built-in functions to work with files easily.

---

### 🔹 Why File Handling?
- Store data permanently
- Read large data from files
- Process CSV / text data
- Log program output

---

### 🔹 File Modes

| Mode | Description |
|------|-------------|
| `r` | Read (default) |
| `w` | Write (overwrites file) |
| `a` | Append (adds data) |
| `x` | Create new file |
| `rb` | Read binary |
| `wb` | Write binary |

---

### 🔹 Common File Operations
- Open a file
- Read data
- Write data
- Close the file
- Use `with` statement (recommended)

---

## ✍️ Writing Data to a File in Python

This program demonstrates how to **write data to a file** using Python’s built-in file handling features.

When a file is opened in **write (`"w"`) mode**, Python:
- Creates the file if it does not exist  
- **Overwrites existing content** if the file already exists  

---

### 🔹 What This Code Does

- Opens a file named `sample.txt` in write mode  
- Writes a line of text into the file  
- Closes the file properly to save changes  

---

### 🔹 File Mode Used

| Mode | Description |
|------|-------------|
| `w` | Write mode (creates or overwrites file) |

---

### 🔹 Important Points

- Existing data in the file will be **deleted** before writing  
- Always close the file after writing to avoid data loss  
- Writing files is useful for saving logs, results, or user data  

---

### 🔹 Use Cases

- Saving program output  
- Writing reports or logs  
- Storing user input  
- Generating text files automatically  

---

### 📌 Note

For safer file handling, Python also provides the `with open()` method,  
which automatically closes the file after use.

---
