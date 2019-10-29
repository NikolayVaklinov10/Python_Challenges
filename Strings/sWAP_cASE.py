"""
You are given a string and your task is to swap cases. In
other words, convert all lowercase letters to uppercase letters
and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2


Input Format

A single line containing a string S.

Constrains

0 < len(S) <= 1000

Output Format

Print the modified string S.

Sample Input 0

HackerRank.com presents "Pythonist 2".

Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""


s = 'hACkEr'
container = []


# MY SOLUTION
def swap_case(s):
    print(s.swapcase())


print(swap_case(s))

# SOLUTION 2
print(''.join([i.lower() if i.isupper() else i.upper() for i in input()]))


# SOLUTION 3
def swap_case(s):
    a = ""
    for let in s:
        if let.isupper() == True:
            a+=(let.lower())
        else:
            a+=(let.upper())
    return a


# SOLUTION 4
def swap_case(s):
    return s.swapcase()


# SOLUTION 5
def swap_case(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result















































































