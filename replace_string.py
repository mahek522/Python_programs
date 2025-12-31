username = input("Enter User Name: ")

# Check minimum length
if len(username) < 3:
    print("User Name must have at least 3 characters.")
else:
    template = "Hello <<UserName>>, How are you?"
    result = template.replace("<<UserName>>", username)
    print(result)