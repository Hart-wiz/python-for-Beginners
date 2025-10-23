# authentication using data collection modu;les



user_db = []

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
    print(" registratiion successful ")



while True:
    print(" Welcome to the open network \n type Register to register and login to login")
    user_input = input("register or login: ")

    if user_input =="register":
        register()
    
    
    print(user_db)
