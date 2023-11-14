import sqlite3


class Inventory:

  def __init__(self, databaseName, tableName):
    self.databaseName = databaseName
    self.tableName = tableName

  def viewInventory(self):
    connection = sqlite3.connect(self.databaseName)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {self.tableName}")
    result = cursor.fetchall()
    print("Current Inventory:\nTitle\tAuthor\tQuantity\n")
    for item in result:
      print(f"{item[0]}\t{item[1]}\t{item[2]}")
    cursor.close()
    connection.close()

  def searchInventory(self):
    connection = sqlite3.connect(self.databaseName)
    cursor = connection.cursor()
    title = input("Please enter the title of the book you want: ")
    cursor.execute(f'''SELECT * FROM {self.tableName} WHERE Title LIKE "%{title}%"''')
    result = cursor.fetchall()
    print("Search Results:\nTitle\tAuthor\tQuantity\n")
    for item in result:
      print(f"{item[0]}\t{item[1]}\t{item[2]}")
    cursor.close()
    connection.close()
    
  def decreaseStock(self, ISBN):
    connection = sqlite3.connect(self.databaseName)
    cursor = connection.cursor()
    cursor.execute(f"SELECT stock FROM {self.tableName} WHERE ISBN={ISBN}")
    result = cursor.fetchone()
    stock = result
    cursor.execute(f"UPDATE {self.tableName} SET stock={stock-1} WHERE ISBN={ISBN}")
    connection.commit()
    cursor.close()
    connection.close()
