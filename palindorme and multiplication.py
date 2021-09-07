"""#PALINDORME SERIES
word = input("Enter the word")
rev = (word[::-1])
if (rev == word):
    print("PALINDORME WORD")
else:
    print("NOT A PALINDORME WORD")"""


#MULTIPLICATION TABLE
num = int(input("Enter the number for the mulitiplication table:"))
for i in range (1,11):
    print("The multiplication table of",num,"*",i,"=",num*i)

