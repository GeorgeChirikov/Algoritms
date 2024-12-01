def fib(n):
    """
    Calculate the Fibonacci's series value for integer n

    Parameters:
    - n: The number to use in the Fibonacci's series.

    Returns: The calculated value of the Fibonacci's series for n
    """
    # ficonacci that uses tabulation
    fib = [1, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]







def test_fib1():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(10) == 89
    assert fib(100) == 573147844013817084101

print(fib(0))
print(fib(1))
print(fib(10))
print(fib(100))
test_fib1()


# def fib(n):
#     """
#     Calculate the Fibonacci's series value for integer n
#
#     Parameters:
#     - n: The number to use in the Fibonacci's series.
#
#     Returns: The calculated value of the Fibonacci's series for n
#     """
#     fib = [1, 1]
#
#     for i in range(2, n + 1):
#         fib.append(fib[i - 1] + fib[i - 2])
#     return fib[n]
