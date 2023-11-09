import sqlite3

class Cart:
    def __init__(self, databaseName="", inventoryName=""):
        self.databaseName = databaseName
        self.inventoryName = inventoryName
    
    '''
    Displays all books in the logged in
    User`s cart. Please note: this cooperates with the inventory database to display all the
    correct information on the inventory items - it just selectively shows the books in the
    User`s cart
    '''
    def viewCart(self, userID, inventoryDatabase):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f'''SELECT i.Title, i.Author, c.Quantity, 
                        FROM {inventoryDatabase} as i, {self.databaseName} as c 
                        WHERE c.UserID={userID} AND c.ISBN=i.ISBN''')
        result = cursor.fetchall()

        print("Your Current Shopping Cart:")
        print("Title - Author  xQuantity")
        for listing in result:
            listingRow = f"{listing[0]} - {listing[1]} x{listing[2]}"
            print(listingRow)

        cursor.close()
        connection.close()

    '''
    This relies on the user viewing the inventory
    previously - from the main. Once they select a book, this ISBN is used to add an item to
    the appropriate cart
    '''
    def addToCart(self, userID, ISBN):
        pass

    
    '''
    This relies on the user viewing the cart
    previous - from the main. Once they select a book to remove, this ISBN is used to
    remove an item from the user`s cart
    '''
    def removeFromCart(self, userID, ISBN):
        pass

    '''
    The user checks out - this removes all their cart items. It also
    calls the Inventory class function to decrease the stock of the books by the correct
    amount the user bought (prior to removing them from the cart)
    '''
    def checkOut(self, userID):
        pass