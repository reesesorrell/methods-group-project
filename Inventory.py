#import sqlite3 for database functionality
import sqlite3

#Class for handling everything related to the store inventory
class Inventory:
    #Parametrized constructor which can serve as a zero constructor if no arguments are sent
    def __init__(self, databaseName="", tableName=""):
        self.databaseName = databaseName
        self.tableName = tableName

    #Displays (prints) all of the items in the store's inventory (all attributes for each item in the Inventory relation)
    def viewInventory(self):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.tableName}")
        result = cursor.fetchall()
        print("Current Inventory:\n\nISBN\t\tTitle\t\tAuthor\t\tGenre\t\tPages\t\tRelease Date\t\tStock\n")
        for item in result:
            print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\t\t{item[3]}\t\t{item[4]}\t\t{item[5]}\t\t\t{item[6]}")
        cursor.close()
        connection.close()

    #Asks user for a title to search by and prints all items that have a similar title
        #If search yields no results, informs user of failure
    def searchInventory(self):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        title = input("\nPlease enter the title of the book you want: ")
        cursor.execute(f'''SELECT * FROM {self.tableName} WHERE Title LIKE "%{title}%"''')
        result = cursor.fetchall()
        if result != []:
            print("\nSearch Results:\n\nISBN\t\tTitle\t\tAuthor\t\tGenre\t\tPages\t\tRelease Date\t\tStock\n")
            for item in result:
                print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\t\t{item[3]}\t\t{item[4]}\t\t{item[5]}\t\t\t{item[6]}")
        else:
            print("No results found!\n\n")
        cursor.close()
        connection.close()

    #Decrements the stock attribute of the book whose ISBN is supplied by 1
    def decreaseStock(self, ISBN):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT stock FROM {self.tableName} WHERE ISBN={ISBN}")
        result = cursor.fetchone()
        stock = result[0]
        cursor.execute(f"UPDATE {self.tableName} SET stock={stock-1} WHERE ISBN={ISBN}")
        connection.commit()
        cursor.close()
        connection.close()