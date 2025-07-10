## C Programming Mini Tasks

### Objective

These tasks will help you practice working with **strings, arrays, and functions** in C. Each function solves a small real-world inspired problem.

Write **separate functions** for each task. You can test them one by one in a simple `main()` program.


### 1. Generate Random Password

* Write a function that generates a random password.
* The password should contain **letters (a-z, A-Z)** and **digits (0-9)**.
* The function should take the **password length** as an argument.
* Return the password as a string.

Example:

```
Input: length = 8  
Output: "aB3kX9pQ"
```

### 2. Validate Username

* Write a function to check if a username is valid.
* Rules:

  * Username must have at least **5 characters**.
  * It can only contain **letters and digits** (no spaces or symbols).
* Return `1` if valid, `0` if invalid.

Example:

```
Input: "John99" → Output: 1 (valid)  
Input: "jo@"     → Output: 0 (invalid)
```

### 3. Concatenate Strings with Prefix

* Write a function that joins a **prefix** string and a **name** string.
* Use `strcat` or `strcpy` to create the new string.

Example:

```
Input: prefix = "user_", name = "alice"  
Output: "user_alice"
```

### 4. Capitalize First Letter

* Write a function that takes a string and **capitalizes the first letter**.
* All other letters remain unchanged.

Example:

```
Input: "hello"  → Output: "Hello"  
Input: "Alice"  → Output: "Alice"
```

### 5. Mask Password for Display

* Write a function that **hides all characters** of a password with `*`.
* The masked password should have the **same length** as the original.

Example:

```
Input: "MySecret123"  
Output: "***********"
```

### 6. Check if Password is Strong

* Write a function to check if a password is strong.
* A password is strong if:

  * It has at least **8 characters**.
  * It contains **at least one letter** and **at least one digit**.
* Return `1` if strong, `0` if weak.

Example:

```
Input: "abc123"      → Output: 0 (weak)  
Input: "abc123XYZ"   → Output: 1 (strong)
```

---

### 💡 Notes:

* Use functions like `rand()`, `strlen()`, `strcat()`, `isalpha()`, `isdigit()` as needed.
* Make sure all strings are **null-terminated**.
* Test each function in a simple `main()` program.

