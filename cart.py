class Cart:
    def __init__(self, databaseName="", inventoryName=""):
        self.__databaseName = databaseName
        self.__inventoryName = inventoryName
    
    '''
    Displays all books in the logged in
    User`s cart. Please note: this cooperates with the inventory database to display all the
    correct information on the inventory items - it just selectively shows the books in the
    User`s cart
    '''
    def viewCart(userID, inventoryDatabase):
        pass


    '''
    This relies on the user viewing the inventory
    previously - from the main. Once they select a book, this ISBN is used to add an item to
    the appropriate cart
    '''
    def addToCart(userID, ISBN):
        pass

    
    '''
    This relies on the user viewing the cart
    previous - from the main. Once they select a book to remove, this ISBN is used to
    remove an item from the user`s cart
    '''
    def removeFromCart(userID, ISBN):
        pass

    '''
    The user checks out - this removes all their cart items. It also
    calls the Inventory class function to decrease the stock of the books by the correct
    amount the user bought (prior to removing them from the cart)
    '''
    def checkOut(userID):
        pass