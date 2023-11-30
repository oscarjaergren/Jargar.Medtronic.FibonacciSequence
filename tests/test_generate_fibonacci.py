import unittest

from src.generate_fibonacci import FibonacciGenerator


class TestFibonacciGenerator(unittest.TestCase):

    # Test with valid input (non-negative integers)
    def test_generate_fibonacci_valid_input(self):
        test_cases = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)]
        for n, expected_result in test_cases:
            with self.subTest(n=n, expected_result=expected_result):
                result = FibonacciGenerator.generate_fibonacci(n)
                self.assertEqual(result, expected_result)

    # Test with invalid input (negative integers and non-integers)
    def test_generate_fibonacci_invalid_input(self):
        invalid_inputs = [-1, -2, -5, 1.5, 'string']
        for n in invalid_inputs:
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    FibonacciGenerator.generate_fibonacci(n)
