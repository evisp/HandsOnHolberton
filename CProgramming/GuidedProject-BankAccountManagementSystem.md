### **Guided Project: Simple Bank Account Management**

#### **Objective**:  
Develop a menu-driven application to simulate basic banking operations using structs, arrays, and functions in C. This project will help you practice structuring data with `struct` and performing basic operations such as deposit, withdrawal, and balance viewing.

---

### **Use Case**:

Imagine you are creating a simple bank system where each client has a name and a bank account with a balance. The bank should be able to:

1. **View Balance**: Show the current balance of the client's account.
2. **Deposit Funds**: Add money to the client's balance.
3. **Withdraw Funds**: Subtract money from the client's balance, ensuring sufficient funds are available.
4. **Exit**: End the program.

**Example Interaction**:

```
Menu:
1. View balance
2. Deposit money
3. Withdraw money
4. Exit

Enter your choice: 1
Account balance for John Doe: $1000.00

Enter your choice: 2
Enter deposit amount: 200
Deposited $200.00. New balance: $1200.00

Enter your choice: 3
Enter withdrawal amount: 500
Withdrawn $500.00. New balance: $700.00

Enter your choice: 4
Exiting program...
```

---

### **Project Requirements**

1. **Define a `struct` for a Bank Client**  
   Create a `struct` named `BankClient` with the following fields:
   - `name` (string) — The name of the client.
   - `accountNumber` (int) — A unique account number for the client.
   - `balance` (float) — The current balance in the client's account.
   
   **Hint**: This struct represents a client’s basic bank account information.

2. **Create an Array of Clients**  
   Declare an array of `BankClient` structs (e.g., size 5). Each client will have a name, account number, and balance. Initialize this array with sample data.

3. **Write Functions for the Following Operations**:
   - **View Balance**: Write a function that displays the current balance of a client.
   - **Deposit**: Write a function that deposits money into the client’s account and updates the balance.
   - **Withdraw**: Write a function that withdraws money from the client’s account, ensuring the balance doesn’t go below zero.
   - **Exit**: Gracefully exit the program when the user selects the option to quit.

   **Function Signatures** (for reference):
   - `void viewBalance(BankClient clients[], int size, int accountNumber);`
   - `void deposit(BankClient clients[], int size, int accountNumber, float amount);`
   - `void withdraw(BankClient clients[], int size, int accountNumber, float amount);`
   
4. **Menu-Driven Application**  
   In the `main()` function, create a menu that allows the user to select from the following options:
   - **1. View balance**
   - **2. Deposit money**
   - **3. Withdraw money**
   - **4. Exit**

   The user will be asked to enter an account number (for simplicity, assume a unique account number for each client). Based on the user’s input, the corresponding function will be called.

---

### **Guidelines for File Organization**

1. **Header File (`bank.h`)**  
   - Declare the `BankClient` struct and function prototypes.

2. **Implementation File (`bank.c`)**  
   - Implement the functions for viewing balance, depositing, and withdrawing.

3. **Main File (`main.c`)**  
   - Implement the `main()` function, which displays the menu and processes user input.

---

### **Struct and Function Hints**

1. **Struct Declaration**:  
   Declare the `BankClient` struct with `name`, `accountNumber`, and `balance` fields:
   ```c
   struct BankClient {
       char name[100];
       int accountNumber;
       float balance;
   };
   ```

2. **Function Signatures**:  
   Define functions that accept an array of `BankClient`, an account number, and an amount to handle deposits and withdrawals:
   - **`void viewBalance(BankClient clients[], int size, int accountNumber);`**  
     Prints the balance for the client identified by `accountNumber`.
   - **`void deposit(BankClient clients[], int size, int accountNumber, float amount);`**  
     Adds the specified amount to the balance of the client identified by `accountNumber`.
   - **`void withdraw(BankClient clients[], int size, int accountNumber, float amount);`**  
     Subtracts the specified amount from the balance of the client, checking if there are sufficient funds.

---

### **Menu-Driven Application Hints**

- **Menu Display**: Use `printf` to show the options for the user.
  ```c
  printf("1. View balance\n");
  printf("2. Deposit money\n");
  printf("3. Withdraw money\n");
  printf("4. Exit\n");
  ```

- **User Input**: Use `scanf` to get the user’s choice and process it:
  ```c
  int choice;
  scanf("%d", &choice);
  ```

- **Switch Case for Menu**: Implement a `switch` statement to handle menu selections:
  ```c
  switch(choice) {
      case 1: viewBalance(clients, size, accountNumber); break;
      case 2: deposit(clients, size, accountNumber, amount); break;
      case 3: withdraw(clients, size, accountNumber, amount); break;
      case 4: printf("Exiting program...\n"); break;
      default: printf("Invalid choice. Try again.\n");
  }
  ```

---

### **Final Testing**

- Test all menu options thoroughly, especially deposit and withdraw functions.
- Ensure that the program prevents withdrawal if there aren’t sufficient funds.
- Check that balances update correctly after deposit and withdrawal operations.

