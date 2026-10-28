from employee import employee_details


def test_employee_details():
    result = employee_details("Rahul","EMP101","IT","5000")

    expected = "Name:Rahul\nEmployee ID: EMP101\nDepartment:IT\nSalary"

    assert result == expected