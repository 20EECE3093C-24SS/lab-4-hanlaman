import pytest
from course_grader import convert_to_letter_grade
# TODO-1: Add test_exact_grade_boundaries() function
def test_exact_boundaries():
    assert convert_to_letter_grade(0) == 'F', "Test Failed: a score of 0 is an F"
    assert convert_to_letter_grade(59) == 'F', "Test Failed: a score of 59 is an F"
    assert convert_to_letter_grade(60) == 'D', "Test Failed: a score of 60 is a D"
    assert convert_to_letter_grade(69) == 'D', "Test Failed: a score of 69 is a D"
    assert convert_to_letter_grade(70) == 'C', "Test Failed: a score of 70 is a C"
    assert convert_to_letter_grade(79) == 'C', "Test Failed: a score of 79 is a C"
    assert convert_to_letter_grade(80) == 'B', "Test Failed: a score of 80 is a B"
    assert convert_to_letter_grade(89) == 'B', "Test Failed: a score of 89 is a B"
    assert convert_to_letter_grade(90) == 'A', "Test Failed: a score of 90 is an A"
    assert convert_to_letter_grade(100) == 'A', "Test Failed: a score of 100 is an A"
# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
    with pytest.raises(ValueError, match="Score must be between 0 and 100."):
        convert_to_letter_grade(-1)
    with pytest.raises(ValueError, match="Score must be between 0 and 100."):
        convert_to_letter_grade(101)
# TODO-3: Add test_non_numeric_input() function
def test_non_numeric_input():
    with pytest.raises(TypeError, match="Score must be a numeric value."):
        convert_to_letter_grade("abc")
    with pytest.raises(TypeError, match="Score must be a numeric value."):
        convert_to_letter_grade([1, 2, 3])
    with pytest.raises(TypeError, match="Score must be a numeric value."):
        convert_to_letter_grade(None)
