# authentication using data collection modu;les




# james = {
#     "username": "james",
#     "email": "james@gmail.com",
#     "phone": "09030890344",
#     "password": "qwertyuiop"
# }

# dan = {
#      "username": "dan09",
#     "email": "dannys@gmail.com",
#     "phone": "0704903455",
#     "password": "asdfghjkl"
# }



user_db = []


def register():

    username = input("enter your username: ")
    email = input("enter your email here: ")
    phone = input("phone number here: ")
    password = input(" enter a password: ")

    user = {
        "username": username,
        "email": email,
        "phone": phone,
        "password": password
    }

    user_db.append(user)
    print("\n registratiion successful \n")


def login():
    username = input("enter your username: ")
    password = input(" enter a password: ")


    if username == user["username"]







while True:
    print("\n \n Welcome to the open network \n type Register to register and login to login")
    user_input = input("register or login: ")

    if user_input =="register":
        register()
    
    
    print(len(user_db))
