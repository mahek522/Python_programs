#Program to write Mathematical tables
#Implementing a function to return a lambda function
def tables(num):
    return lambda x : x*num
number = int(input("Enter a number\n"))
math_table = tables(number)
for i in range(1, 11):
    print(number,"X",i,"=",math_table(i))