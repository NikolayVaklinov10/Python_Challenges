"""
Read an integer N.
Without using string methods, try to print the following:
123...N
Note that "..." represents the values in between.

Input Format

The first contains an integer N.

Output Format




"""

# my solution
n = 3

for i in range(1, n + 1):
    print(i, end='')

# solution 2
def fun(*args):
    total = 0
    for i in args:
        total += i
    return total


# solution 3
print(*range(1, int(input())+1), sep='')


























