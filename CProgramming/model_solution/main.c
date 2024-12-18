#include <stdio.h>
#include "employee.h"

#define MAX_EMPLOYEES 200

int main() {
    Employee employees[MAX_EMPLOYEES];
    Employee bonusEmployees[MAX_EMPLOYEES];
    int employeeCount = 0;
    int bonusCount = 0;

    // Read data from text file
    employeeCount = readFromFile("employees.txt", employees, MAX_EMPLOYEES);
    if (employeeCount == -1) {
        return 1; // Exit if file cannot be read
    }

    // Print the data
    printf("Employee Data:\n");
    printEmployees(employees, employeeCount);

    // Calculate average salary
    double avgSalary = calculateAverageSalary(employees, employeeCount);
    printf("\nAverage Salary: %.2f\n", avgSalary);

    // Find max salary
    double maxSalary = findMaxSalary(employees, employeeCount);
    printf("Max Salary: %.2f\n", maxSalary);

    // Count employees with salary between 1000 and 2000
    int countInRange = countEmployeesInSalaryRange(employees, employeeCount, 1000, 2000);
    printf("Employees with salary between 1000 and 2000: %d\n", countInRange);

    // Apply bonus to IT employees and write to binary file
    applyBonusToIT(employees, employeeCount, 500.00);
    writeToBinaryFile("employees_bonus.bin", employees, employeeCount);

    // Read back from binary file and print
    bonusCount = readFromBinaryFile("employees_bonus.bin", bonusEmployees, MAX_EMPLOYEES);
    if (bonusCount != -1) {
        printf("\nEmployee Data After Bonus:\n");
        printEmployees(bonusEmployees, bonusCount);
    }

    return 0;
}
