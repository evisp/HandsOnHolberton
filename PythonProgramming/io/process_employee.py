import os

EMPLOYEE_FILE = os.path.join("files", "employees.txt")

def read_employees(filepath):
    """Reads employee data from the file and returns a list of dictionaries."""
    employees = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            next(file)  
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    emp_id, name, department, salary = parts
                    employees.append({
                        "ID": int(emp_id),
                        "Name": name,
                        "Department": department,
                        "Salary": float(salary)
                    })
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
    return employees

def print_all_employees(filepath):
    """Prints all employees in a formatted way."""
    employees = read_employees(filepath)
    if not employees:
        print("No employees found.")
        return
    print(f"\n{'ID':<5} {'Name':<20} {'Department':<15} {'Salary':<10}")
    print("-" * 50)
    for emp in employees:
        print(f"{emp['ID']:<5} {emp['Name']:<20} {emp['Department']:<15} {emp['Salary']:<10.2f}")

def count_employees(filepath):
    """Counts the total number of employees."""
    employees = read_employees(filepath)
    print(f"Total number of employees: {len(employees)}")

def search_employee(filepath, search_name):
    """Searches for an employee by name."""
    employees = read_employees(filepath)
    results = [emp for emp in employees if search_name.lower() in emp["Name"].lower()]
    
    if results:
        print("\nFound Employees:")
        for emp in results:
            print(f"{emp['ID']}: {emp['Name']} - {emp['Department']} - ${emp['Salary']}")
    else:
        print(f"No employee found with name containing '{search_name}'.")

def sort_employees_by_salary(filepath, descending=True):
    """Sorts employees by salary and prints them."""
    employees = read_employees(filepath)
    sorted_employees = sorted(employees, key=lambda x: x["Salary"], reverse=descending)

    print("\nEmployees Sorted by Salary:")
    for emp in sorted_employees:
        print(f"{emp['ID']}: {emp['Name']} - {emp['Department']} - ${emp['Salary']:.2f}")

def group_employees_by_department(filepath):
    """Groups employees by department and prints them (Using Pure Dictionary and If-Else)."""
    employees = read_employees(filepath)
    department_groups = {}

    # Group employees manually using dictionary and if-else
    for emp in employees:
        department = emp["Department"]
        if department in department_groups:
            department_groups[department].append(emp)
        else:
            department_groups[department] = [emp]

    print("\nEmployees Grouped by Department:")
    for department in department_groups:
        print(f"\n🔹 {department}:")
        for emp in department_groups[department]:
            print(f"   {emp['ID']}: {emp['Name']} - ${emp['Salary']:.2f}")

def write_top_10_salaries_to_file(filepath, output_file):
    """Writes the top 10 highest-paid employees to another file."""
    employees = read_employees(filepath)
    top_10 = sorted(employees, key=lambda x: x["Salary"], reverse=True)[:10]

    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("ID|Name|Department|Salary\n")
            for emp in top_10:
                file.write(f"{emp['ID']}|{emp['Name']}|{emp['Department']}|{emp['Salary']}\n")
        print(f"\nTop 10 highest-paid employees written to {output_file}")
    except Exception as e:
        print(f"Error writing file: {e}")

def main():
    """Main function to execute employee processing tasks."""
    print_all_employees(EMPLOYEE_FILE)
    count_employees(EMPLOYEE_FILE)

    search_name = "Arben"
    search_employee(EMPLOYEE_FILE, search_name)

    sort_employees_by_salary(EMPLOYEE_FILE, descending=True)
    group_employees_by_department(EMPLOYEE_FILE)

    output_file = os.path.join("files", "top_10_salaries.txt")
    write_top_10_salaries_to_file(EMPLOYEE_FILE, output_file)

if __name__ == "__main__":
    main()
