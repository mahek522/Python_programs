#check if the expression has balanced parenthesis or not.
s = input("Enter the expression with brackets/parenthesis: \n")
list = []
for i in s:
    if i=='[' or i=='{' or i=='(':
        list.append(i)
    elif i==']' and list[-1]=='[':
        list.pop()
    elif i=='}' and list[-1]=='{':
        list.pop()
    elif i==')' and list[-1]=='(':
        list.pop()
    else:
        break
if len(list)==0:
    print("The expression has balanced parenthesis.")
else:
    print("The expression does not have balanced parenthesis.")