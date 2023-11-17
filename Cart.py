import sqlite3
from Inventory import Inventory

class Cart:
    #make constructor with empty default parameters
    def __init__(self, databaseName="", tableName=""):
        self.databaseName = databaseName
        self.tableName = tableName
    
    '''
    Displays all books in the logged in
    User`s cart. Please note: this cooperates with the inventory database to display all the
    correct information on the inventory items - it just selectively shows the books in the
    User`s cart
    '''
    def viewCart(self, userID, inventoryDatabase):
        #connect to DB
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        #get the overlap between the users cart and inventory to return the books info
        cursor.execute(f'''SELECT i.Title, i.Author, c.Quantity 
                        FROM {inventoryDatabase} as i, {self.tableName} as c 
                        WHERE c.UserID=? AND c.ISBN=i.ISBN''', (userID,))
        result = cursor.fetchall()

        if result:
            #print every book in the results
            print("Your Current Shopping Cart:")
            print("Title - Author  xQuantity")
            for listing in result:
                listingRow = f"{listing[0]} - {listing[1]} {listing[2]}"
                print(listingRow)

        else:
            print("Your cart is empty.")

        cursor.close()
        connection.close()

    '''
    This relies on the user viewing the inventory
    previously - from the main. Once they select a book, this ISBN is used to add an item to
    the appropriate cart
    '''
    def addToCart(self, userID, ISBN):
        #connect to the database
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        #select the quantity of the selected book
        cursor.execute(f"SELECT Quantity FROM {self.tableName} WHERE UserID=? AND ISBN=?", (userID, ISBN))
        result = cursor.fetchone()

        if result:
            #if it already exists then update it to plus 1
            cursor.execute(f"UPDATE {self.tableName} SET Quantity='{result[0] + 1}' WHERE UserID=? AND ISBN=?", (userID, ISBN))

        #if it doesn't exist then create the new book entry with a quantity of 1
        else:
            cursor.execute(f"INSERT INTO {self.tableName} (UserID, ISBN, Quantity) VALUES (?, ?, ?)", (userID, ISBN, 1))
        
        #commit the changes then close the db
        connection.commit()

        print("A copy of that book has been added to your cart.")

        cursor.close()
        connection.close()


    
    '''
    This relies on the user viewing the cart
    previous - from the main. Once they select a book to remove, this ISBN is used to
    remove an item from the user`s cart
    '''
    def removeFromCart(self, userID, ISBN):
        #connect to the database
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        #delete the book from cart
        try:
            cursor.execute(f"DELETE FROM {self.tableName} WHERE ISBN=? AND UserId=?", (ISBN, userID))

            #commit the changes then close the db
            connection.commit()

            print("That book has been removed from your cart.")

        except:
            print("That book isn't in your cart.")

        cursor.close()
        connection.close()


    '''
    The user checks out - this removes all their cart items. It also
    calls the Inventory class function to decrease the stock of the books by the correct
    amount the user bought (prior to removing them from the cart)
    '''
    def checkOut(self, userID):
        #connect to the database
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        #get the users cart
        cursor.execute(f'''SELECT ISBN, Quantity FROM {self.tableName}
                        WHERE UserID=?''', (userID,))
        result = cursor.fetchall()

        inventory = Inventory(self.databaseName, "Inventory")
        #remove every book in the from inventory
        for listing in result:
            ISBN = listing[0]
            quantity = listing[1]
            for i in range(quantity):
                inventory.decreaseStock(ISBN)

        #delete the users cart 
        cursor.execute(f"DELETE FROM {self.tableName} WHERE UserId=?", (userID,))

        connection.commit()
        cursor.close()
        connection.close()
