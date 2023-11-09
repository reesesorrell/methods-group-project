import sqlite3

class Cart:
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
                        WHERE c.UserID={userID} AND c.ISBN=i.ISBN''')
        result = cursor.fetchall()

        #print every book in the results
        print("Your Current Shopping Cart:")
        print("Title - Author  xQuantity")
        for listing in result:
            listingRow = f"{listing[0]} - {listing[1]} {listing[2]}"
            print(listingRow)

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
        cursor.execute(f"SELECT Quantity FROM {self.tableName} WHERE UserID={userID} AND ISBN={ISBN}")
        result = cursor.fetchone()

        #if it already exists then update it to plus 1
        if result:
           cursor.execute(f"UPDATE {self.tableName} SET Quantity='{result[0] + 1}' WHERE UserID={userID} AND ISBN={ISBN}")

        #if it doesn't exist then create the new book entry with a quantity of 1
        else:
            cursor.execute(f"INSERT INTO {self.tableName} (UserID, ISBN, Quantity) VALUES ('{userID}', '{ISBN}', '1')")
        
        #commit the changes then close the db
        connection.commit()
        cursor.close()
        connection.close()


    
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