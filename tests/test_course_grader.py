import pytest
from course_grader import convert_to_letter_grade
# TODO-1: Add test_exact_grade_boundaries() function
def test_exact_boundaries():
  assert convert_to_letter_grade(59) == 'F'
  assert convert_to_letter_grade(60) == 'D'
  assert convert_to_letter_grade(69) == 'D'"
  assert convert_to_letter_grade(70) == 'C'
  assert convert_to_letter_grade(79) == 'C'
  assert convert_to_letter_grade(80) == 'B'
  assert convert_to_letter_grade(89) == 'B'
  assert convert_to_letter_grade(90) == 'A'
  assert convert_to_letter_grade(100) == 'A'
  assert convert_to_letter_grade(0) == 'F'
# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
  with pytest.raises(TypeError):
    convert_to_letter_grade(-1)
  with pytest.raises(TypeError):
    convert_to_letter_grade(101)
# TODO-3: Add test_non_numeric_input() function
def test_non_numeric_input():
  with pytest.raises(TypeError):
    convert_to_letter_grade("a", 61)
  with pytest.raises(TypeError):
    convert_to_letter_grade([a,b,c])
  with pytest.raises(TypeError):
    convert_to_letter_grade(None)
