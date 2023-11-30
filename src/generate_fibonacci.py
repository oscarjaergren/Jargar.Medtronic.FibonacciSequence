from functools import lru_cache


class FibonacciGenerator:
    def __init__(self) -> None:
        pass

    @staticmethod
    @lru_cache(maxsize=None)
    def generate_fibonacci(n: int) -> int:
        """
        Generate the nth Fibonacci number using recursion and memoization.
        Args: n (int): The index of the Fibonacci number to generate.
        Returns: int: The nth Fibonacci number.
        Raises: ValueError: If the input is not a non-negative integer.
        """
        # Check if the input is a non-negative integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a non-negative integer.")

        # Base case: return n for n <= 1
        if n <= 1:
            return n
        # Recursive case: generate Fibonacci numbers using memoization
        else:
            return (
                    FibonacciGenerator.generate_fibonacci(n - 1)
                    + FibonacciGenerator.generate_fibonacci(n - 2)
            )
