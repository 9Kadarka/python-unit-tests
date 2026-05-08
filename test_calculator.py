# test_calculator.py
"""
Unit tests for calculator module using pytest framework.
These tests verify that all calculator functions work correctly.
"""

import pytest
from calculator import (
    add, subtract, multiply, divide, is_even, is_prime,
    reverse_string, count_vowels, is_palindrome, factorial
)


class TestArithmetic:
    """Tests for basic arithmetic operations."""

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        assert add(3, 5) == 8

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-3, -5) == -8

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(10, 3) == 7

    def test_subtract_resulting_negative(self):
        """Test subtraction resulting in negative."""
        assert subtract(3, 10) == -7

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(100, 0) == 0

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(10, 2) == 5

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestNumberProperties:
    """Tests for checking number properties."""

    def test_is_even_with_even_number(self):
        """Test is_even returns True for even numbers."""
        assert is_even(4) is True

    def test_is_even_with_odd_number(self):
        """Test is_even returns False for odd numbers."""
        assert is_even(7) is False

    def test_is_prime_with_prime_number(self):
        """Test is_prime returns True for prime numbers."""
        assert is_prime(7) is True
        assert is_prime(17) is True

    def test_is_prime_with_non_prime_number(self):
        """Test is_prime returns False for non-prime numbers."""
        assert is_prime(4) is False
        assert is_prime(15) is False

    def test_is_prime_with_edge_cases(self):
        """Test is_prime with edge cases (0, 1, 2)."""
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(2) is True


class TestStringOperations:
    """Tests for string manipulation functions."""

    def test_reverse_string_basic(self):
        """Test string reversal with basic text."""
        assert reverse_string("hello") == "olleh"

    def test_reverse_string_with_spaces(self):
        """Test string reversal with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"

    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        assert reverse_string("") == ""

    def test_count_vowels_basic(self):
        """Test vowel counting in basic text."""
        assert count_vowels("hello") == 2

    def test_count_vowels_case_insensitive(self):
        """Test that vowel counting is case-insensitive."""
        assert count_vowels("HELLO") == 2
        assert count_vowels("HeLLo") == 2

    def test_count_vowels_no_vowels(self):
        """Test counting vowels when there are none."""
        assert count_vowels("xyz") == 0

    def test_is_palindrome_simple(self):
        """Test palindrome detection for simple words."""
        assert is_palindrome("racecar") is True
        assert is_palindrome("hello") is False

    def test_is_palindrome_with_spaces(self):
        """Test palindrome detection ignoring spaces."""
        assert is_palindrome("race car") is True

    def test_is_palindrome_case_insensitive(self):
        """Test palindrome detection is case-insensitive."""
        assert is_palindrome("RaceCar") is True


class TestFactorial:
    """Tests for factorial calculation."""

    def test_factorial_of_zero(self):
        """Test that factorial of 0 is 1."""
        assert factorial(0) == 1

    def test_factorial_of_one(self):
        """Test that factorial of 1 is 1."""
        assert factorial(1) == 1

    def test_factorial_of_positive_number(self):
        """Test factorial of positive numbers."""
        assert factorial(5) == 120
        assert factorial(6) == 720

    def test_factorial_of_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined"):
            factorial(-5)


# Integration tests
class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_complex_calculation(self):
        """Test a complex calculation using multiple functions."""
        result = add(multiply(3, 4), divide(10, 2))
        assert result == 17

    def test_string_and_number_operations(self):
        """Test combining string and number operations."""
        text = "hello"
        vowel_count = count_vowels(text)
        reversed_text = reverse_string(text)
        assert vowel_count == 2
        assert reversed_text == "olleh"
