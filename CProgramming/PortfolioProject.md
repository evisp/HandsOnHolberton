# Holberton School C Programming Portfolio Project

## Objectives

This project will help you bring together and apply the C programming and data structure skills you have learned during the trimester. You will build a menu-driven application that uses key programming concepts to solve a real-world problem. The goal is to write clear, well-structured, and reusable code while practicing good programming habits.  

### Key Concepts to Include

1. **Basic Programming**
   - Use loops (`for`, `while`, `do-while`) to repeat tasks.
   - Use conditional statements (`if`, `else`, `switch`) to make decisions in your program.
   - Write functions to split your program into smaller, reusable parts.

2. **Using Structs**
   - Create and use `struct` types to represent real-world objects with multiple pieces of information (for example: a `Student` with name, age, and grade).

3. **Function Pointers or Switch Cases**
   - Use `switch` statements to handle menu choices.
   - (Optional) Use function pointers for more flexible program logic.

4. **Menu-Driven Program**
   - Build a program where users can choose actions from a menu (for example:  
     `1 - Add Item`  
     `2 - View All Items`  
     `3 - Search Item`  
     `4 - Exit`).

5. **File Handling**
   - Save and load data using text files so information is not lost when the program closes.  
   - Use file operations like `fopen`, `fprintf`, `fscanf`, and `fclose`.

6. **Data Structures**
   - Choose one data structure to organize your data:  
     - Arrays for fixed-size storage.  
     - Linked Lists for flexible, dynamic lists.  
     - Binary Search Trees for sorting and fast searching.

7. **Searching and Sorting**
   - Add at least one search method (like linear search or binary search).  
   - Add at least one sorting method (like bubble sort, insertion sort, or quicksort).  

---

## Project Description

You are free to choose your own application idea as long as it meets the key requirements listed above. Below are three example projects you can consider:  


### 1. **Product Management System**
Develop a program to manage products in a small shop or warehouse. Each product can have a name, product ID, price, and quantity in stock. Users should be able to:  
- Add a new product  
- View all products  
- Search for a product by name or ID  
- Update product details (price, quantity)  
- Delete a product from the list  
- Save and load product data from a text file  

**Key Concepts**:  
Use structs to represent products, and choose a suitable data structure like an array, linked list, or binary search tree to store them. Implement sorting to view products by price or name, and searching to locate products quickly.  

### 2. **Library Book Management System**
Create a program to manage books in a small library. Each book can have a title, author, ISBN number, and availability status. Users should be able to:  
- Add new books to the system  
- Display all books  
- Search for a book by title or ISBN  
- Update the availability status (e.g., borrowed or returned)  
- Save and load book records from a file  

**Key Concepts**:  
Use structs for book records and select a data structure such as an array, linked list, or binary search tree for storage.  

### 3. **Student Grades Tracker**
Design a program to track student grades for a course. Each student can have a name, ID number, and a list of grades. Users should be able to:  
- Add a new student and their grades  
- View all students and their average grades  
- Search for a student by ID  
- Sort students by their average grade or name  
- Save and load student records from a file  

**Key Concepts**:  
Use nested structs (for students and their grades), sorting algorithms for ranking, and file handling for persistence.  

### Custom Project Option
If you have another idea for a project, you can propose it to your mentor for approval. Your idea must include:  
- A menu-driven interface  
- Use of structs and at least one data structure  
- File storage for saving and loading data  
- Searching and sorting features  

---
## Requirements and Deliverables

This project is designed to be completed in phases to help you plan, develop, and refine your work over time. You are encouraged to work in teams of two, but you may also work individually if you prefer.  

### Phase 1: Project Proposal  
**Deadline:** July 23  

- Present your project idea and key functionalities.  
- Submit either:  
  - A **one-page document** describing the application, its purpose, and the main features you plan to implement.  
  - Or a **3-slide presentation** outlining the same information.  
- The proposal should include:  
  - The type of application (e.g., product manager, library system, etc.)  
  - The data to be managed and how it will be represented using `structs` and stored using a data structure. 
  - The planned menu options for the user interface.  


### Phase 2: Initial Implementation  
**Deadline:** August 4  

- Deliver the first version of your application with the following features:  
  - Use of `structs` to represent your data.  
  - Implementation of loops, conditional statements, and functions to handle core logic.  
  - Ability to read data from a file and display it.  
  - Use of a simple data structure such as an array or a linked list to store records in memory.  
- Submit your code on **GitHub** with:  
  - Proper commit history showing your progress.  
  - Comments in the code following **Betty style guidelines** for C programming.  
- Provide a short document explaining what has been implemented and any challenges faced.  

### Phase 3: Final Implementation and Refinement  
**Deadline:** August 18  

- Complete and refine your application by adding the following features:  
  - A fully functional **menu-driven interface**.  
  - Implementation of searching and sorting algorithms to manage and retrieve data effectively.  
  - (Optional) Use of an advanced data structure such as a binary search tree for improved performance.  
  - Ability to save updated data back to the file.  
- Ensure the program handles errors gracefully (e.g., invalid input, file not found).  
- Submit on **GitHub**:  
  - Final version of the code, fully documented and commented using **Betty style**.  
  - A `README.md` file explaining how to compile, run, and use your program.  
  - A short report (1–2 pages) describing the completed application, its features, and lessons learned.  

---

### General Guidelines  
- Use **GitHub** throughout the project to track changes and collaborate effectively.  
- Write **clean, modular, and well-documented code**. Follow the **Betty style guide** for all C code formatting and comments.  
- Each phase deliverable must include proper documentation of your work.  



