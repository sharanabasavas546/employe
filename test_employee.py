from employee import employee_details

def test_employee_details():
    
    expected_output = (
        "Employee Name: Bouna\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 30000"
    )
    
    assert employee_details("Alice", "e101", "IT", 55000) == expected_output
