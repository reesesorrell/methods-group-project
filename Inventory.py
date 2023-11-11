import sqlite3

class Inventory:
    def __init__(self):
        pass

    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewInventory(self):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor
        cursor.execute(f"SELECT * FROM {self.tableName}")
        result = cursor.fetchall()
        print("Current Inventory:\nTitle\tAuthor\tQuantity\n")
        for (item in result):
            print(f"{item[0]}\t{item[1]}\t{item[2]}")
        cursor.close()
        connection.close()

    def searchInventory(self):
        pass

    def decreaseStock(ISBN):
        pass
