n = 5
# my solution
for i in range(n):
    print(i**2)

# solution 2
n = 5
# * is an arbitrary list. It works by expanding a list into a sequence of positional parameters
# by using the * operator.
print(*[num**2 for num in range(n)], sep='\n')


# solution 3
[print(i**2) for i in range(n)]


# solution 4
i=0
for i in range(n):
    print(pow(i,2))




