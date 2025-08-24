while True:
    password = input("create a password (min 6 chars , must include a number) : ")
    
    if len(password) < 6:
        print("To short!")
    elif not any (char.isdigit() for char in password):
        print("Must contain a number.")
    else:
        print("Password accepted")
        break