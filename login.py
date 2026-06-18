attempts = 3

while attempts > 0:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "1234":
        print("Login successful")
        break

    else:
        attempts -= 1

        if username != "admin":
            print("Username not found")
        else:
            print("Wrong password")

        if attempts == 2:
            print("Hint: Password is a 4-digit number")

        elif attempts == 1:
            print("Last attempt!")

        print("Attempts left:", attempts)

if attempts == 0:
    print("Account locked")