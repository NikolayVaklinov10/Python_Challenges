"""
Given an integer, n , print the following values for each integer i from 1 to n:

    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

The four values must be printed on a single line in the order specified above for each i
from 1 to n. Each value should be space-padded to match the width of the binary value of n.

Input Format

A single integer denoting n.

Constraints

* 1<= n<= 99

Output Format

Print
lines where each line (in the range ) contains the respective decimal, octal, capitalized
hexadecimal, and binary values of . Each printed value must be formatted to the width of
the binary value of

.

Sample Input

17

Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001



"""
from __future__ import print_function

# MY SOLUTION
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1,1):
        print(str((i).rjust(width,' ')),str(oct(i)[2:].rjust(width,' ')),str(hex(i).upper()[2:].rjust(width,' ')),str(bin(i)[2:]))


# solution 2


number = int(input())


def print_formatted(number):
    for i in range(1,number+1):
        width = len(bin(number)[2:])
        print(str(i).rjust(width,' '),str(oct(i)[2:]).rjust(width,' '),str(hex(i)[2:].upper()).rjust(width,' '),str(bin(i)[2:]).rjust(width,' '),sep=' ')


print(print_formatted(17))









