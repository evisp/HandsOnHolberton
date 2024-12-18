#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "employee.h"

// Function to read employee data from a text file
int readFromFile(const char *fileName, Employee employees[], int maxSize) {
    FILE *file = fopen(fileName, "r");
    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }

    int count = 0;
    while (count < maxSize && fscanf(file, "%d,%49[^,],%19[^,],%lf", 
            &employees[count].id, 
            employees[count].fullName, 
            employees[count].department, 
            &employees[count].salary) == 4) {
        count++;
    }

    fclose(file);
    return count;
}

// Function to calculate the average salary
double calculateAverageSalary(const Employee employees[], int size) {
    double total = 0;
    for (int i = 0; i < size; i++) {
        total += employees[i].salary;
    }
    return size > 0 ? total / size : 0;
}

// Function to find the maximum salary
double findMaxSalary(const Employee employees[], int size) {
    double maxSalary = 0;
    for (int i = 0; i < size; i++) {
        if (employees[i].salary > maxSalary) {
            maxSalary = employees[i].salary;
        }
    }
    return maxSalary;
}

// Function to count employees with salaries in a given range
int countEmployeesInSalaryRange(const Employee employees[], int size, double min, double max) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (employees[i].salary >= min && employees[i].salary <= max) {
            count++;
        }
    }
    return count;
}

// Function to apply a bonus to employees in the IT department
void applyBonusToIT(Employee employees[], int size, double bonus) {
    for (int i = 0; i < size; i++) {
        if (strcmp(employees[i].department, "IT") == 0) {
            employees[i].salary += bonus;
        }
    }
}

// Function to write employee data to a binary file
void writeToBinaryFile(const char *fileName, const Employee employees[], int size) {
    FILE *file = fopen(fileName, "wb");
    if (file == NULL) {
        perror("Error opening file");
        return;
    }

    fwrite(employees, sizeof(Employee), size, file);
    fclose(file);
}

// Function to read employee data from a binary file
int readFromBinaryFile(const char *fileName, Employee employees[], int maxSize) {
    FILE *file = fopen(fileName, "rb");
    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }

    int count = fread(employees, sizeof(Employee), maxSize, file);
    fclose(file);
    return count;
}

// Function to print employees to the screen
void printEmployees(const Employee employees[], int size) {
    printf("%-5s %-30s %-15s %-10s\n", "ID", "Full Name", "Department", "Salary");
    for (int i = 0; i < size; i++) {
        printf("%-5d %-30s %-15s %-10.2f\n", 
               employees[i].id, employees[i].fullName, employees[i].department, employees[i].salary);
    }
}
