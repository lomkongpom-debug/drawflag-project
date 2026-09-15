R = int(input())
C = int(input())

for i in range(R):
    row = ""
    for j in range(C):
        if j % 2 == 0:
            row += "@"
        else:
            row += "#"
    print(row)
