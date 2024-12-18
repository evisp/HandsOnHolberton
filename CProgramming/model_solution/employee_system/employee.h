#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <stdio.h>

typedef struct Employee {
    int id;
    char fullName[50];
    char department[20];
    double salary;
} Employee;

int readFromFile(const char *fileName, Employee employees[], int maxSize);
void printEmployees(const Employee employees[], int size);

double calculateAverageSalary(const Employee employees[], int size);
double findMaxSalary(const Employee employees[], int size);
int countEmployeesInSalaryRange(const Employee employees[], int size, double min, double max);

void applyBonusToIT(Employee employees[], int size, double bonus);

void writeToBinaryFile(const char *fileName, const Employee employees[], int size);
int readFromBinaryFile(const char *fileName, Employee employees[], int maxSize);


#endif 
