#Accept no from user and return addition of its factors

no=int(input("enter a number"))
sum=0;
for i in range(1, no):
        if((no % i)==0):
            sum = sum+i


print("addition is", sum)


