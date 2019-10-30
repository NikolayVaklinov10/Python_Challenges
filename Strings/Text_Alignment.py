"""
In Python, a string of text can be aligned left, right and center.

.ljust(width)

This method returns a left aligned string of length width.

#>>> width = 20
#>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------

.center(width)

This method returns a centered string of length width.

#>>> width = 20
#>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----

.rjust(width)

This method returns a right aligned string of length width.

#>>> width = 20
#>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank

Task

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

Input Format

A single line containing the thickness value for the logo.

Constraints

The thickness must be an odd number.

Output Format

Output the desired logo.

Sample Input

5

Sample Output

    H
   HHH
  HHHHH
 HHHHHHH
HHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
                    HHHHHHHHH
                     HHHHHHH
                      HHHHH
                       HHH
                        H


"""

#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).center(thickness)+c+(c*(thickness-i-1)).center(thickness)).center(thickness*6))

# SOLUTION
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))






import math

c='♥'
width = 40

print ((c*2).center(width//2)*2)

for i in range(1,width//10+1):
    print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

for i in range(width//4,0,-1):
    print ((c*i*4).center(width))
print ((c*2).center(width))

#*********************************************************
# #Bottom Cone
# for i in range(thickness):
#     print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)
#
# #Bottom Cone
# for myShift in range(1,7):
#     print ""
#     print "|Btm Cone |".rjust(thickness*myShift)
#     print ""
#     for i in range(thickness):
#         print (
#                 ('O'*(thickness-i-1)).rjust(thickness,'"')+
#                 'v'+
#                 ('X'*(thickness-i-1)).ljust(thickness,'^')
#             ).rjust(thickness*myShift,'.')
#
#
#
#



















