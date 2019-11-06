"""
In this challenge, the user enters a string and a substring. You have to print the
number of times that the substring occurs in the given string. String traversal
will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the
substring.

Constrains

1 <= len(string) <= 200

Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the
substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2

Concept

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where

is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])

A range function is used to loop over some length:

range (0, 5)

Here, the range loops over
to . is excluded.

"""

# MY SOLUTION
def count_substring(string, sub_string):
    count = string.count(sub_string)
    count += 1
    return count


print(count_substring("Thisisthebestfromthecodewrittentodaycode.", "code"))

# solution 2
def count_substring(string, sub_string):
    count = 0
    for n in range(len(string), 0, -1):
        try:
            if string[n - len(sub_string):n] == sub_string:
                count += 1
        except IndexError:
            break
        return count


# solution 3
string, substring = (input().strip(), input().strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))

# solution 4 !!!


def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count

# solution 5
# if name == 'main': string = input().strip() sub_string = input().strip()
#
# count = count_substring(string, sub_string)
# print(count)
#





















