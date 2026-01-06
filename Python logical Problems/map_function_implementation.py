#Implementing map function to calculate square of numbers in a list
#using def function
nums = list(map(int, input("Enter the elements of a list to be squared: ").split()))
def square(num):
    return num*num
squared_list = list(map(square, nums))
print("The squared elements in the list are:", squared_list)

#using lambda function
squared_list_lambda = list(map(lambda x: x*x, nums))
print("The squared elements in the list using Lambda are:", squared_list_lambda)