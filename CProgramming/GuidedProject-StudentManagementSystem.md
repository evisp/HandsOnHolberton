### **Guided Project: Student Data Management System**

#### **Objective**:  
Develop a menu-driven application that manages student data using structs, arrays, and functions in C. You will practice creating and manipulating structs, performing basic operations (e.g., calculating average, searching, sorting), and writing modular code with functions.

---

### **Project Requirements**

1. **Declare a `struct` for a Student**  
   Define a `struct` named `Student` with the following fields:
   - `name` (string) — Student’s name.
   - `id` (int) — Unique student ID.
   - `grade` (float) — Student’s grade.

2. **Create an Array of Students**  
   Declare an array of `Student` structs (e.g., size 5) and initialize it with sample data (name, ID, grade).

3. **Functions to Implement**  
   Write functions for the following tasks:
   - **Print Students**: Print details of all students.
   - **Find Average Grade**: Calculate the average grade of all students.
   - **Count Students**: Return the number of students in the array.
   - **Search by ID**: Search for a student by ID and print their details if found.
   - **Sort by Grade**: Sort students by grade in descending order (hint: use bubble sort).

   **Function Signatures** (for reference):
   - `void printStudents(Student students[], int size);`
   - `float findAverageGrade(Student students[], int size);`
   - `int countStudents(Student students[], int size);`
   - `int searchByID(Student students[], int size, int id);`
   - `void sortStudentsByGrade(Student students[], int size);`

4. **Menu-Driven Application**  
   In `main()`, create a menu to allow the user to select from the following options:
   - **1. Print all students**
   - **2. Find average grade**
   - **3. Search student by ID**
   - **4. Sort students by grade**
   - **5. Exit**
   
   Based on the user's choice, call the appropriate function and display results.

---

### **Guidelines for File Organization**

1. **Header File (`student.h`)**  
   - Declare the `Student` struct and function prototypes.

2. **Implementation File (`student.c`)**  
   - Implement the functions declared in `student.h`.

3. **Main File (`main.c`)**  
   - Implement the `main()` function with a menu to call the corresponding operations.

---

### **Struct and Function Hints**

1. **Struct Declaration**:  
   Declare the `Student` struct with `name`, `id`, and `grade` fields:
   ```c
   struct Student {
       char name[100];
       int id;
       float grade;
   };
   ```

2. **Function Signatures**:
   - `void printStudents(Student students[], int size);`
   - `float findAverageGrade(Student students[], int size);`
   - `int searchByID(Student students[], int size, int id);`
   - `void sortStudentsByGrade(Student students[], int size);`

---

### **Menu-Driven Application Hints**

- **Menu Display**: Use `printf` to show available options.
  ```c
  printf("1. Print all students\n");
  printf("2. Find average grade\n");
  printf("3. Search student by ID\n");
  printf("4. Sort students by grade\n");
  printf("5. Exit\n");
  ```

- **User Input**: Use `scanf` to capture user choice and execute the corresponding action.
  ```c
  int choice;
  scanf("%d", &choice);
  ```

- **Switch Case**: Use a `switch` statement to handle menu options and call the appropriate function:
  ```c
  switch(choice) {
      case 1: printStudents(students, size); break;
      case 2: printf("Average: %.2f\n", findAverageGrade(students, size)); break;
      case 3: searchByID(students, size, id); break;
      case 4: sortStudentsByGrade(students, size); break;
      case 5: printf("Exiting...\n"); break;
      default: printf("Invalid choice.\n");
  }
  ```

---

### **Final Testing**

- Test all menu options.
- Ensure correct handling of invalid input.
- Verify sorting works properly.

