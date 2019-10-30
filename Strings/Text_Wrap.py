"""
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Input Format

The first line contains a string, S.
The second line contains the width, w.

Constraints

* 0 < len(S) < 1,000

* 0 < w < len(S)

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ


"""
#
#
# import textwrap
#
# def wrap(string, max_width):
#     return
#
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)
#
#


# MY SOLUTION
def wrap(string, max_width):
    return "\n".join(string[i:i+max_width] for i in range(0, len(string), max_width))


print(wrap("ASDFGJJKKHFDSQWRTYUI", 4))


# solution 2
def wrap(string, max_width):
    for i in range(0,len(string),max_width):
                        print(string[i:i+max_width])


# solution 3
import textwrap

print (textwrap.fill(input(),int(input())))


# solution 4
def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

# solution 5


















