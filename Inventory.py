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
    print("Current Inventory:\n\nISBN\t\tTitle\t\tAuthor\t\tGenre\t\tPages\t\tRelease Date\t\tStock\n")
    for item in result:
      print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\t\t{item[3]}\t\t{item[4]}\t\t{item[5]}\t\t\t{item[6]}")
    cursor.close()
    connection.close()

  def searchInventory(self):
    connection = sqlite3.connect(self.databaseName)
    cursor = connection.cursor()
    title = input("\nPlease enter the title of the book you want: ")
    cursor.execute(f'''SELECT * FROM {self.tableName} WHERE Title LIKE "%{title}%"''')
    result = cursor.fetchall()
    print("\nSearch Results:\n\nISBN\t\tTitle\t\tAuthor\t\tGenre\t\tPages\t\tRelease Date\t\tStock\n")
    for item in result:
      print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\t\t{item[3]}\t\t{item[4]}\t\t{item[5]}\t\t\t{item[6]}")
    cursor.close()
    connection.close()

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
