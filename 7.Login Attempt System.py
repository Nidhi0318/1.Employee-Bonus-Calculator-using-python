username = "admin"
password = "Python@123"

for attempt in range(1, 4):
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == username and pwd == password:
        print("Login successful")
        break
    elif user != username:
        print("User not found")
    else:
        print("Incorrect password")

    if attempt == 3:
        print("Account locked")