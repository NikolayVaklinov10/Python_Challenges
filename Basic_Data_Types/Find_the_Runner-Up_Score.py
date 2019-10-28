"""
Given the participants' score sheet for your University Sports Day, you are required
to find the runner-up score. You are given n scores. Store them in a list and find
the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers
each separated by a space.

Constraints

* 2 <= n <= 10

* -100 <= A[i] <= 100

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5

Sample Output 0

5

Explanation 0

Given list is [2, 3, 6, 6, 5]. The maximum score is 6, send maximum is 5. Hence,
we print 5 as runner-up score.

"""
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     runner_up_score = sorted(list(set([n for n in arr])))
#     print(runner_up_score)
#



# possible solution

i = int(input())
lis = list(map(int, input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print(max(lis))













