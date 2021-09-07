#LEAP YEAR
year = int(input("Enter the year:"))
if (year%4==0,year%100!=0,year%400):
    print(year,"is an Leap year")
else:
    prnit(year,"is not an Leap year")

#ODD & EVEN
num=int(input("Enter the number:"))
if (num%2)==0:
    print("The Given Number is Even no.")
else:
    print("The Given Number is Odd")
#FACTORIAL NUMBER
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input("Enter the Number:"))
if n==0:
    print("Factorial of 0 is 1")
elif (n<0):
    print("Invaild")
else:
    print("Factorial of",n, "is",(n-1))

#FIBONACCI SERIES
num=int(input("Enter the Number:"))
n1=0
n2=1
count=0
if num<=0:
    print("please enter the positive number")
elif(num==1):
    print("The fibonacci series of 1 is",n1)
else:
    print("The Fibonacci series is:")
while count<num:
    print(n1)
    last=n1+n2
    n1=n2
    n2=last
    count+=1
 #To check prime no.whether prime no.or Not
 num = int(input("Enter the Number"))
 if num>1:
  for i in range (2,num):
 if (num%i)==0:
     print(i,"times",num//i,"is",num)
if(num%i)!=0:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")
        
        
    

