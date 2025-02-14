import os

EMPLOYEE_FILE = os.path.join("files", "employees.txt")

def read_employees(filepath):
    """Reads employee data from the file and returns a list of dictionaries."""
    pass 

def print_all_employees(filepath):
    """Prints all employees in a formatted way."""
    pass

def count_employees(filepath):
    """Counts the total number of employees."""
    pass 

def search_employee(filepath, search_name):
    """Searches for an employee by name."""
    pass 

def sort_employees_by_salary(filepath, descending=True):
    """Sorts employees by salary and prints them."""
    pass

def group_employees_by_department(filepath):
    """Groups employees by department and prints them (Using Pure Dictionary and If-Else)."""
    pass

   

def write_top_10_salaries_to_file(filepath, output_file):
    """Writes the top 10 highest-paid employees to another file."""
    pass

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
