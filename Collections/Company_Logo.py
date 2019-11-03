"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string

, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

    Print the three most common characters along with their occurrence count.
    Sort in descending order of occurrence count.
    If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,

would have it's logo with the letters

.

Input Format

A single line of input containing the string

.

Constraints

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde

Sample Output 0

b 3
a 2
c 2

Explanation 0

Here, b occurs times. It is printed first.
Both a and c occur

times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string
has at least distinct characters.
"""


# solution 1
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]


# solution 2
from collections import Counter

for each in Counter(sorted(input())).most_common(3):
    print(*each)



# solution 3
if __name__ == '__main__':
    s = input()
    ans = []

    for i in set(s):
        ans.append((i, s.count(i)))

    list.sort(ans, key=lambda x: (x[1], -ord(x[0])), reverse=True)

    for x in range(3):
        print(ans[x][0], ans[x][1])
















