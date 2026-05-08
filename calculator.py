# calculator.py
"""
Simple calculator module with common operations.
This module demonstrates basic functionality suitable for unit testing.
"""

def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def reverse_string(text):
    """Reverse a string."""
    return text[::-1]


def count_vowels(text):
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text):
    """Check if a string is a palindrome (ignoring spaces and case)."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def factorial(n):
    """Calculate factorial of n. Raises ValueError if n is negative."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
