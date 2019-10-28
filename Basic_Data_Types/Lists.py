"""
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.

2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of
followed by lines of commands where each command will be of the

types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer,
, denoting the number of commands.
Each line of the

subsequent lines contains one of the commands described above.

Constraints

    The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]



"""

def lines_from_stdin(n):
    n = int(n)
    for i in range(n):
        yield input().rstrip('\n').split()

def matching_lines(lines, patterns):
    for line in lines:
        for pattern in patterns:
            if pattern in line:
                yield line

def matching_lines_from_stdin(pattern, n):
    lines = lines_from_stdin(n)
    matching = matching_lines(lines, pattern)
    yield from matching

def map_list_commands(n):
    answer = list()
    funcs = dir(list) + ['print']
    matching = matching_lines_from_stdin(funcs, n)
    for vals in matching:
        func = vals[0]
        if func in dir(list):
            try:
                val1, val2 = int(vals[1]), int(vals[2])
                method = getattr(answer, func)(val1, val2)
            except IndexError:
                try:
                    val1 = int(vals[1])
                    method = getattr(answer, func)(val1)
                except IndexError:
                    method = getattr(answer, func)()
        elif func == 'print':
            print(answer)

if __name__ == '__main__':
    N = int(input())
    map_list_commands(N)






















