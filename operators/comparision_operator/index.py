# age = int(input("Enter your age"))
# if age >= 18:
#     print('your are ready to vote')
# else:
#     print("you are not ready to vote")

# email = input("Enter you email")
# password = input("Enter your password")

# if email == 'abc@gmail.com' and password == '123':
#     print("Login Successfully!!")
# else:
#     print("Invalid Info")

ch = input("Enter ch")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("This is vowel")
else:
    print("This is consonant") 


age = int(input("Enter your age"))
if not age > 18:
    print('Not ready to vote')
else:
    print("Ready to vote")