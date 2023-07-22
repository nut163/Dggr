import sys
from src.app import App
from src.login import login
from src.register import register
from src.logout import logout
from src.delete_account import deleteAccount

def main():
    app = App()

    while True:
        print("Welcome to Dog Tinder!")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = login()
            if user_id:
                while True:
                    print("1. Logout")
                    print("2. Delete Account")
                    print("3. Exit")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        logout(user_id)
                        break
                    elif choice == '2':
                        deleteAccount(user_id)
                        break
                    elif choice == '3':
                        sys.exit()
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Login failed. Please try again.")
        elif choice == '2':
            register()
        elif choice == '3':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()