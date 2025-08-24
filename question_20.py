correct_password = "Admin@123"
attempts = 0

while attempts < 3:
    user_input = input ("Enter password: ")
    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password")
        attempts += 1
        
        if attempts == 3:
            print("Too many failed attempts. Try later.")