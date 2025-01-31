# Bank System - Guided Project

### Overview
Create a system with three classes: `Account`, `Customer`, and `Bank`. These classes will be connected to represent a simple bank system where customers have accounts with balances, and the bank manages a list of customers.

### Class Requirements:

1. **Account Class:**
   - **Property:**
     - `balance` (float): The balance of the account.
   - **Methods:**
     - **Setter** and **Getter** for `balance`.
     - **`__init__`** to initialize the balance.
     - **`deposit(amount)`** to add money to the account.
     - **`withdraw(amount)`** to subtract money from the account (ensure balance doesn’t go negative).
   
2. **Customer Class:**
   - **Properties:**
     - `name` (string): The name of the customer.
     - `account` (Account): An instance of the `Account` class for the customer's balance.
   - **Methods:**
     - **`__init__`** to initialize the customer’s name and account.
     - **`get_name()`** to get the customer’s name.
     - **`get_balance()`** to get the balance from the customer’s account.
   
3. **Bank Class:**
   - **Property:**
     - `customers` (list): A list of `Customer` objects.
   - **Methods:**
     - **`add_customer(customer)`** to add a customer to the bank’s list.
     - **`find_customer(name)`** to find a customer by name and return the corresponding `Customer` object.
     - **`get_total_balance()`** to calculate the total balance of all customers in the bank.

---

### Project Flow:
1. **Create the `Account` class** with methods to set/get the balance and perform deposit/withdraw actions.
2. **Create the `Customer` class** with properties for name and account, and methods to interact with customer data.
3. **Create the `Bank` class** that manages a list of customers and provides methods for customer addition and total balance calculation.
4. **Connect the classes**:
   - Each `Customer` has an `Account` with a `balance`.
   - The `Bank` stores and manages a list of `Customer` objects.

---