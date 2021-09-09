string = input("enter the string:")
count = 0
words = 1
for i in string:
    count = count+1
    if (i==" "):
        words = words+1
        print("Number of character in the string:",count)
        print("Number of words in the string:",words)