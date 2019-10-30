"""
Task
Given an integer,

, perform the following conditional actions:

    If

is odd, print Weird
If
is even and in the inclusive range of to
, print Not Weird
If
is even and in the inclusive range of to
, print Weird
If
is even and greater than

    , print Not Weird

Input Format

A single line containing a positive integer,

.

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.


"""
# n = 100
#
# #
# # my solution
#

# BETTER SOLUTION
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    check = {True: "Not Weird", False: "Weird"}

    print(check[
            n%2==0 and (
                n in range(2,6) or
                n > 20)
        ])



#
# # another one #1
# n = int(input().strip())
# check = {True: "Not Weird", False: "Weird"}
#
# print(check[n % 2 == 0 and (n in range(2, 6) or n > 20)])
#
#
#
# # another one #2
# n = int(input())
# if n % 2 == 0:
#     if n in range(2,6):
#         print("Not Weird")
#
#     elif n in range(6,21):
#         print("Weird")
#
#     elif n > 20:
#         print("Not Weird")
# else:
#     print("Weird")
#
#
# # another one #3
# num = int(input())
# n = num % 2
#
# if n == 0 and (2<= num <=5):
#     print('Not Weird')
# elif n == 0 and (6<= num <=20):
#     print('Weird')
# elif n == 0 and num > 20:
#     print("Not Weird")
# elif num % 2 != 0:
#     print('Weird')
#
# # another # 4
# n = int(input().strip())
# check = {True: "Not Weird", False: "Weird"}
# print(check[n%2==0 and n not in range(6, 21)])
#
# # another #5
# n = int(input())
# check = {True:'Weird',False:'Not Weird'}
# print (check[n%2 != 0 or n in range(6,21)])
#
# # another # 5
# n = int(input())
# if n%2==1 :
#     print("Weird")
# elif n%2==0 and 2<=n<=5 :
#     print("Not Weird")
# elif n%2==0 and 6<=n<=20 :
#     print("Weird")
# elif n%2==0 and n>20 :
#     print("Not Weird")
#
#
# # solution 6
#
# n = int(input().strip())
# check = {True: "Not Weird", False: "Weird"}
#
# print(check[
#         n%2==0 and (
#             n in range(2,6) or
#             n > 20)
#     ])

#
# def check(n):
#     if n in range(6, 21) or n % 2 != 0:
#         return "Weird"
#     else:
#         return "Not Weird"
#
# print(check(25))


def checked(n):
    check = {True: "Not Weird", False: "Weird"}
    return check[n % 2 == 0 and n not in range(6, 21)]

print(checked(6))




































