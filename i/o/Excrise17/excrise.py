#Exercise 17. Masked password input (getpass)
import getpass
user = input("Enter Username: ")
pwd=getpass.getpass("Password")
if user == "admin" and pwd == "SecretPassword123":
    print(f"Login successful for {user}!")
else:
    print("Access Denied.")
