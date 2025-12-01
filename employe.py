import pytest

def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Employee Salary: {salary}"
    )
    return result

if __name__ == "__main__":
    # simple input (you can change)
    name = "Alice"
    emp_id = "E101"
    department = "IT"
    salary = 55000

    print(employee_details(name, emp_id, department, salary))
