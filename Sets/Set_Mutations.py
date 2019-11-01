"""


"""

# solution 1
if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))


# solution 2
(_, A) = (
    input(),
    set(map(int, input().split()))
)

for _ in range(input()):
    (command, newSet) = (
        input().split()[0],
        set(map(int, input().split()))
    )

    # Cool trick. Since our commands are method names, just
    # execute the method on A with our new set as its argument.
    getattr(A, command)(newSet)

print(str(sum(A)))