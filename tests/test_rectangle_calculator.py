import pytest
from rectangle_calculator.rectangle_calculator import calculate_rectangle_area


def test_calculate_rectangle_area():
    assert calculate_rectangle_area(2, 3) == 6
    assert calculate_rectangle_area(5, 5) == 25
    assert calculate_rectangle_area(1.5, 2.5) == 10  # to fix 3.75


def test_invalid_input():
    try:
        calculate_rectangle_area(-2, 3)
    except ValueError as e:
        assert str(e) == "Length and width should be positive numbers."

    try:
        calculate_rectangle_area(2, -3)
    except ValueError as e:
        assert str(e) == "Length and width should be positive numbers."

    try:
        calculate_rectangle_area("hello", 3)
    except ValueError as e:
        assert str(e) == "could not convert string to float: 'hello'"


def test_rectangle_area_positive_numbers():
    assert calculate_rectangle_area(5, 10) == 50


def test_rectangle_area_negative_numbers():
    with pytest.raises(ValueError):
        calculate_rectangle_area(-5, 10)


def test_rectangle_area_one_negative_number():
    with pytest.raises(ValueError):
        calculate_rectangle_area(-5, 5)


def test_rectangle_area_zero_width():
    with pytest.raises(ValueError):
        calculate_rectangle_area(0, 10)


def test_rectangle_area_zero_length():
    with pytest.raises(ValueError):
        calculate_rectangle_area(5, 0)


def test_rectangle_area_large_numbers():
    assert calculate_rectangle_area(1000000, 1000000) == 1000000000000


def test_rectangle_area_decimal_numbers():
    assert calculate_rectangle_area(2.5, 3) == 7.5


def test_rectangle_area_invalid_input():
    with pytest.raises(ValueError):
        calculate_rectangle_area("a", 10)


def test_rectangle_area_negative_float_input():
    with pytest.raises(ValueError):
        calculate_rectangle_area(-2.5, 3.5)


def test_rectangle_area_with_both_negative_numbers():
    with pytest.raises(ValueError):
        calculate_rectangle_area(-5, -5)
