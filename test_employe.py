from employe import employee_info

def test_employee_info():
    
    expected_output = (
        "Employee Name: Bouna\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 30000"
    )
    
    assert employee_info("Alice", "e101", "IT", 55000) == expected_output