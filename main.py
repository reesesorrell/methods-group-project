from Inventory import Inventory
from User import User
from Cart import Cart

inventory = Inventory("store.db", "Inventory")
user = User("store.db", "User")
cart = Cart("store.db", "Cart")

def beforeLoginMenu():
    while True:
        choice = input("\nWelcome to the E-Commerce Store\n1.\tLogin\n2.\tCreate an account\n3.\tLogout\n4.\tExit\n\nPlease choose an option: ")

        if choice == "1":
            if user.login():
                print("Logged in successfully.\n")
                mainMenu()
            else:
                print("Login failed. Please try again.\n")
        elif choice == "2":
            user.createAccount()
        elif choice == "3":
            if user.getLoggedIn():
                user.logout()
                print("Logged out successfully.\n")
            else:
                print("You are not logged in.\n")
        elif choice == "4":
            print("\nThank you for using the E-Commerce Store. Bye!")
            break;
        else:
            print("Invalid choice, please try again.\n")

def mainMenu():
    while True:
        choice = input("\nMain Menu:\n1.\tLogout\n2.\tView account information\n3.\tView inventory information\n4.\tView cart information\n\nPlease choose an option: ")

        if choice == "1":
            user.logout()
            print("Logged out successfully.\n")
            beforeLoginMenu()
            break;
        elif choice == "2":
            user.viewAccountInformation()
        elif choice == "3":
            inventoryMenu()
        elif choice == "4":
            cartMenu()
        else:
            print("Invalid choice, please try again.\n")

def inventoryMenu():
    choice = input("\nInventory Information Menu:\n1.\tGo back to Main Menu\n2.\tView inventory information\n4.\tSearch Inventory\n\nPlease choose an option: ")

    if choice == "1":
        mainMenu()
    elif choice == "2":
        inventory.viewInventory()
    elif choice == "3":
        inventory.searchInventory()
    else:
        print("Invalid choice.\n")
    
def cartMenu():
    choice = input("\Cart Information Menu:\n1.\tGo back to Main Menu\n2.\tView Cart information\n3.\tAdd items to Cart\n4.\tRemove an item from Cart\n5.\tCheck-Out\n\nPlease choose an option: ")

    if choice == "1":
        mainMenu()
    elif choice == "2":
        cart.viewCart()
    elif choice == "3":
        book = input("Please enter the ISBN of the book you wish to add to the Cart: ")
        cart.addToCart(user.getUserID(), int(book))
    elif choice == "4":
        book = input("Please enter the ISBN of the book you wish to remove from the Cart: ")
        cart.removeFromCart(user.getUserID(), int(book))
    elif choice == "5":
        cart.checkOut(user.getUserID())
    else:
        print("Invalid choice.\n")

beforeLoginMenu()