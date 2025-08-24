while True:
    email = input("Enter your email: ")
    if "@" in email and "." in email:
        print("Email accepted:",email)
        break
    else:
        print("Invalid email format")