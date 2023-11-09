from user import User 
def main():
    database_name = "store.db"
    table_name = "user"

    user_system = User(databaseName=database_name, tableName=table_name)

    while True:
        print("\nWelcome to the E-Commerce Store")
        print("1. Create an account")
        print("2. Login")
        print("3. View Account Information")
        print("4. Logout")
        print("5. Exit")

        choice = input("Please choose an option: ")

        if choice == '1':
            user_system.createAccount()
        elif choice == '2':
            if user_system.login():
                print("Logged in successfully.")
            else:
                print("Login failed.")
        elif choice == '3':
            user_system.viewAccountInformation()
        elif choice == '4':
            if user_system.getLoggedIn():
                user_system.logout()
                print("Logged out successfully.")
            else:
                print("You are not logged in.")
        elif choice == '5':
            print("Thank you for using the E-Commerce Store.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
