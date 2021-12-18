"""
***********************
World of Flavors
***********************

Monica is the head chef in the Central Perk cafe. She wants to serve her customers with as many different flavours of
coffee but she has coffee seeds of only N different flavours. But she knows a trick to get new flavours from the
existing flavours.

The trick is as follows :
A combination of 2 or more of the original flavours gives a new flavour (amount of the original flavour does not matter)
A combination of K or less different flavours is a good flavour and all the original flavours are good, where K is a
non-negative integer.

input1 : N, denoting the number of different flavours
input2 : K, denoting the maximum number of flavours that can be used

Example1 :
    input1 : 5
    input2 : 2
    Output : 15
    Explanation : Flavours from 1 to 5. Therefore the combinations are:
        (1,2) (1,3) (1,4) (1,5) -------------------- 4
        (2,3) (2,4) (2,5) -------------------------- 3
        (3,4) (3,5) -------------------------------- 2
        (4,5) -------------------------------------- 1
        1, 2, 3, 4, 5  ----------------------------- 5
    *******************************************************
        TOTAL -------------------------------------- 15
    *******************************************************
Example2:
    input1, input2 = 5, 3
    Output = 
    Explanation : 
        (1,2,3) (1,2,4) (1,2,5) (1,3,4) (1,3,5) ---- 5
        (2,3,4) (2,3,5) (2,4,5) -------------------- 3
        (3,4,5) ------------------------------------ 1
        (1,2) (1,3) (1,4) (1,5) -------------------- 4
        (2,3) (2,4) (2,5) -------------------------- 3
        (3,4) (3,5) -------------------------------- 2
        (4,5) -------------------------------------- 1
        1, 2, 3, 4, 5  ----------------------------- 5
    *******************************************************
        TOTAL -------------------------------------- 24
    *******************************************************
"""

# Taking the inputs

input1 = int(input("Enter input 1 : "))
input2 = int(input("Enter input 2 : "))


def factorial(N):  # Function to find the factorial of a number
    return 1 if (N == 1 or N == 0) else N * factorial(N - 1)


def ncr(n, r):  # Function to find mathematical combination nCr 
    return factorial(n) / (factorial(n - r) * factorial(r))


count = 0   # A variable to count the combinations

for combination in range(1, input2 + 1):
    count += ncr(input1, combination)

print("Final count = ", int(count))
