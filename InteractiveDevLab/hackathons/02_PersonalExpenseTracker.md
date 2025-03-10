### **Hackathon Challenge: Expense Tracker Database**  

#### **Objective:**  
Design and implement a relational database for an **Expense Tracker** application. The goal is to define a well-structured database that allows users to manage their expenses efficiently while considering scalability, data integrity, and future extensibility.

---

### **Key Requirements:**  

1. **User Management:**  
   - Users should have unique identifiers, usernames, and credentials.  
   - Think about what additional user details might be useful.  

2. **Expense Categorization:**  
   - Expenses must be grouped into categories.  
   - Consider how to ensure consistency in category names.  

3. **Tracking Expenses:**  
   - Each expense must belong to a user and be associated with a category.  
   - It should store an amount, a description, and a date.  
   - How would you ensure that an expense always belongs to a user?  
   - What should happen if a category is deleted?  

4. **Budgeting System:**  
   - Users should be able to set monthly spending limits for different categories.  
   - Think about how to prevent duplicate budgets for the same user-category pair.  

5. **Data Constraints & Relationships:**  
   - Ensure proper data types and constraints to maintain integrity.  
   - Implement necessary **foreign keys** and **cascade behaviors** to handle deletions properly.  
   - Consider how you would prevent invalid data entries (e.g., negative expense amounts).  

---

### **Hints & Thought Questions:**  
- How will you ensure that usernames and emails are unique?  
- Should categories be predefined or user-created?  
- What should happen if a user deletes their account?  
- How can you prevent data inconsistencies when handling foreign key relationships?  
- What indexes would improve performance for frequent queries?  

---

### **Deliverables:**  
1. **SQL Script** to create the database and tables.  
2. **Justification Document** explaining key design choices.  
3. **Bonus:** Test queries to insert and retrieve sample data efficiently.  

---