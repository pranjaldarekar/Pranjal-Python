#Accept one number & display pattern
print("Number Pattern");

LN = 6
for row in range(1, LN):
    for colmun in range(1, row+1):
        print(colmun, end=" ");
    print("");
