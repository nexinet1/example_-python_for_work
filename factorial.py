#calculates the factorial of a given number using recursion


def factorial(n):
    # base case: factorial of 0 is 1
    if n == 0:
        return 1
    # recursive case: calculate factorial of n-1 and multiply by n
    else:
        return n * factorial(n-1)

# test the function with some sample inputs

print(factorial(5))  # output: 120
print(factorial(10)) # output: 3628800
