"""
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the
second lowest grade.

Note:
    If there are multiple students with the same grade, order their names
    alphabetically and print each name on a new line.


Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line
contains a student's name, and the second line contains their grade.

Constraints

* 2 <= N <= 5

* There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in
Physics; if there are multiple students, order their names alphabetically
and print each one on a new line.


Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry

Explanation 0

There are 5 students in this class whose names and grades are assembled to build
the following list:

python_students = [['Harry', 37.21],['Berry', 37.21],['Tina', 37.2],['Akriti',41],
['Harsh',39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs
to both Harry and Berry, so we order their names alphabetically and print each
name on a new line.

"""
# solution 1
marksheet = []
for _ in range(0, int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]

print('\n'.join([ a for a,b in sorted(marksheet) if b == second_highest]))
#
# **************************************************************
#
# solution 2
# n = int(input())
# marksheet = [[input(), float(input())] for _ in range(n)]




#
#
#
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#
#
# # solution 3
# score_list = []
# for _ in range(int(input())):
# 	name = input()
# 	score = float(input())
# 	mark_sheet.append([name,score])
# 	score_list.append(score)
#
#
# second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]
#
# for name,marks in sorted(mark_sheet):
# 	if marks == second_lowest_mark:
# 		print(name)
#

























