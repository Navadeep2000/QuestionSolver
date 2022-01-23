"""
Program to find Nth term in a Fibonacci sequence with a complexity of O(2N) or O(N) using memoization

Fibonacci sequence: 1 1 2 3 5 8 13 21 ... so on
Logic : A term in this sequence is obtained by adding up the previous 2 values
i.e., Nth term is obtained by adding up (N-1)th and (N-2)th terms


Basic function without memo has a complexity of O(2^N), it is as follows:

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

"""


# Defining a function 'fib(n)' which has a memo of previous values
# It returns the nth value of the sequence using recursion
def fib(n, memo={}):
    # memo stores previously calculated values of the process
    # This reduces re-calculation of same value and saves time
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


# main() function
# This is a custom print and can be changed as pleased for checking an nth term

print(fib(5))  # Gives 5
print(fib(15))  # 610
print(fib(50))  # 12586269025
print(fib(8))  # 21
print(fib(28))  # 317811
