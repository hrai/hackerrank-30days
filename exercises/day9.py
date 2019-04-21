#!/bin/python3

# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return n

    return n * factorial(n - 1)
