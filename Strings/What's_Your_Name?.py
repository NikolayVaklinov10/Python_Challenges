"""
You are given the firstname and lastname of a person on two different
 lines. Your task is to read them and print the following:

 Hello firstname lastname! You just delved into python.

Input Format

The first line contains the first name, and the second line contains
 the last name.

Constraints

The length of the first and last name ≤ 10.


Output Format

Print the output as mentioned above.

Sample Input 0

Ross
Taylor

Sample Output 0

Hello Ross Taylor! You just delved into python.

Explanation 0

The input read by the program is stored as a string data type. A string is a collection of characters.

"""

# MY SOLUTION
def print_full_name(a, b):
    print( "Hello " + a +" " + b + "! " + "You just delved into python.")


print(print_full_name("Nick"," Vaklinov"))


# solution 2
print("Hello {0} {1}! You just delved into python.".format(input(), input()))


# solution 3
def message(first_name, last_name):
    print("Hello %s %s! You just delved into python." % (first_name, last_name))


# solution 3
def another_message(a,b):
    print("Hello",a," ",b, "! You just delved into python.",sep="")


# solution 4
def yet_another():
    print(f"Hello {input()} {input()}! You just delved into python.")


# solution 5
def print_full_name(first_name, last_name):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))













