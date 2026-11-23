
from employee import employee_details

def test_employee_details():
    expected = (
        "Name: Rahul\n"
        "Employee ID: EMP101\n"
        "Department: IT\n"
        "Salary: 5000"
    )

    assert employee_details("Rahul", "EMP101", "IT", 5000) == expected


def test_employee_hr():
    expected = (
        "Name: Priya\n"
        "Employee ID: 102\n"
        "Department: HR\n"
        "Salary: 40000"
    )

    assert employee_details("Priya", 102, "HR", 40000) == expected
