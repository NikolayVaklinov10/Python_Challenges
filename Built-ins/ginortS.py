"""
You are given a string .
contains alphanumeric characters only.
Your task is to sort the string

in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string

.

Constraints

Output Format

Output the sorted string

.

Sample Input

Sorting1234

Sample Output

ginortS1324
"""
# solution 1
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')
# solution 2
print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
# solution 3
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

# solution 4
import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')















