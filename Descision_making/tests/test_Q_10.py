from Descision_making.code.Q_10 import Student
import pytest


def test_student_total_average_grade():
    student = Student("Alice", 70, 80, 90)
    assert student.total == 240
    assert student.average == 80.0
    assert student.grade_class == "First Class"

    student = Student("Bob", 55, 45, 50)
    assert student.total == 150
    assert student.average == 50.0
    assert student.grade_class == "Second Class"


def test_invalid_input():
    with pytest.raises(ValueError):
        Student("Alice", -70, -80, 90)