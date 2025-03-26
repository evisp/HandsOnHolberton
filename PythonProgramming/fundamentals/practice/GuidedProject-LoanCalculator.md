### Loan Repayment Calculator

#### **Objective:**
The goal of this project is to create a loan repayment calculator that helps users estimate the monthly payments based on the loan amount, interest rate, and loan term. It will calculate the monthly repayment amount and the total amount paid over the loan term.

#### **Task Requirements:**

##### **1. Loan Repayment Formula:**
Use the following formula to calculate the monthly repayment amount:

<p style="font-size: 28px;">$$ M = \frac{P \cdot r \cdot (1 + r)^n}{(1 + r)^n - 1} $$</p>



Where:
- \( M \) = monthly repayment
- \( P \) = loan principal (loan amount)
- \( r \) = monthly interest rate (annual interest rate divided by 12)
- \( n \) = number of payments (loan term in years multiplied by 12)

The total amount paid over the loan term can be calculated as:

$$
\text{Total Payment} = M \cdot n
$$

##### **2. User Input:**
- The program will prompt the user to input the following:
  1. **Loan Amount (Principal)**: The amount of money borrowed (e.g., 5000).
  2. **Annual Interest Rate**: The annual interest rate in percentage (e.g., 5%).
  3. **Loan Term**: The loan term in years (e.g., 5 years).

##### **3. Output:**
- Display the following results:
  1. **Monthly Repayment**: The calculated monthly repayment amount.
  2. **Total Amount Paid**: The total amount paid over the course of the loan term.

##### **4. Validation:**
Ensure that the input values are valid:
- The loan amount must be greater than zero.
- The interest rate must be a non-negative value.
- The loan term must be a positive integer.
- If invalid input is given, prompt the user to enter valid data.

##### **5. Specific Functions:**

- **`calculateMonthlyRepayment(principal, annualInterestRate, loanTerm)`**  
  This function will calculate and return the monthly repayment amount based on the provided formula. It will take in:
  - `principal`: The loan amount (P).
  - `annualInterestRate`: The annual interest rate as a percentage (annual rate).
  - `loanTerm`: The loan term in years.

- **`calculateTotalAmountPaid(monthlyRepayment, loanTerm)`**  
  This function will calculate and return the total amount paid over the loan term by multiplying the monthly repayment by the total number of payments (loan term in years multiplied by 12).

##### **6. Program Flow:**
- The program should prompt the user for the required inputs (loan amount, interest rate, and loan term).
- Use the provided functions to calculate the monthly repayment and total payment.
- Display the calculated values to the user.

##### **7. Sample Interaction:**

```
Welcome to the Loan Repayment Calculator!

Enter loan amount (e.g., 5000): 5000
Enter annual interest rate (e.g., 5): 5
Enter loan term in years (e.g., 5): 5

Calculating...

Your monthly repayment is: 94.47
The total amount paid over the term is: 5668.40
```

##### **8. Edge Cases:**
- If the user enters a zero or negative loan amount, interest rate, or loan term, ask for valid inputs.
- Ensure that the program handles interest rates that are very small or large (e.g., 0% or 100%).

