"""
You are given an integer followed by

email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The maximum length of the extension is

    .

Concept

A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters.

Let's say you have to make a list of the squares of integers from
to

(both included).

>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))

Now, you only require those elements that are greater than
but less than

.

>> l = list(filter(lambda x: x > 10 and x < 80, l))

Easy, isn't it?

Input Format

The first line of input is the integer
, the number of email addresses.

lines follow, each containing a string.

Constraints

Each line is a non-empty string.

Output Format

Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']


"""


def fun(s):
	s_prcocess = s.replace('@','.').split('.')
	order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468-_'
	if len(s_prcocess) == 3 and all(s_items != '' for s_items in s_prcocess):
		if len(s_prcocess[2]) <= 3 and s_prcocess[1].isalnum() and all(item in order for item in s_prcocess[0]):
			return True
	return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)












