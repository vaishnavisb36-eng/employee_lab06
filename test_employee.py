from employee import employee_details

def test_employee_details():
    expected = (
        "Name: Rahul\n"
        "Employee ID: EMP101\n"
        "Department: IT\n"
        "Salary: 5000"
    )

    assert employee_details("Rahul", "EMP101", "IT", 5000) == expected