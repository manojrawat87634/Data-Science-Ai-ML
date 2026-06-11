# Variables - 
# Datatypes 
# Operators
# loops 
# Function - is used to store code 
# for i in range(4, 20, 2):
#     print(i)

# def loginFunc():
#     email = input("Enter your name")
#     password = input("Enter your password")
#     if email == 'abc@gmail.com' and password == '123':
#         print('Login successfully')
#     else:
#         print("invalid info")
#     # print("Login function")

# loginFunc()
# def rF(name, email):
#     print("User registered with name : {name}\nemail : {email}")

# rF("abc", 'abc@gmail.com')
# rF("xyz", 'xyz@gmail.com')

arr = []

def rF(email, password):
    arr.append({"email" : email, "password" : password})


rF( 'abc@gmail.com', '123')
rF( 'xyz@gmail.com', '123')
# print(arr)
def lF():
    email = input("Enter email")
    password = input("Enter password")
    for i in arr:
        if (i['email'] == email) and i['password'] == password:
            print("Login successfully !!")
            return
    print("no user found")

lF()
    
