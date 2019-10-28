"""
We add a Leap Day on February 29, almost every four years.
The leap day is an extra, or intercalary day and we add it to
the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into
account to identify leap years:

* The year can be evenly divided by 4, is a leap year, unless:
* The year can be evenly divided by 100, it is NOT a leap year,
unless:
* The year is also evenly divisible by 400. Then it is leap year.

This means that in the Gregorian calendar, the years 2000 and 2400
are leap years, while 1800, 1900, 2100,2200, 2300 and 2500 are NOT
leap years.

Task

You are given the year, and you have to write a function to check
if the year is leap or not.

Note that you have to complete the function and remaining code
is given as template.

Input Format

Read y, the year that needs to be checked.

Constrains

1900 <= y <= 10^5

Output Format

Output is taken care of by the template. Your function must
return a boolean value (True/False)



"""
# my solution
import calendar


def is_leap(year):

    leap = calendar.isleap(year)

    return leap


print(is_leap(2000))


# solution 2
def is_leap(year):
    """Determine whether a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# solution 3
def is_leap(n):
    if n%4==0 and n%100!=0:
        if n%400 == 0:
            print(n, " is a leap year.")
        elif n%4!=0:
            print(n, " is not a leap year.")
print(is_leap(1900))


# solution 4
def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False
print(is_leap(1900))











































