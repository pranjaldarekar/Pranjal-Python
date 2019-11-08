#program to check +ve,-ve,zero number
def checknum():

 no = int(input("Enter a number: "));
 if no > 0:
   print(" Number is Positive number")
 elif no == 0:
   print("Number is Zero")
 elif no < 0:
   print("Number is Negative number")
checknum()