import sqlite3

class User:
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = False
        self.userID = None

    def login(self):
        username = input("Enter email: ")  # Using email as the username since there is no username field in the DB
        password = input("Enter password: ")

        if self.validate_credentials(username, password):
            self.loggedIn = True
            self.userID = self.get_user_id_from_db(username)
            print("Login successful.")
            return True
        else:
            print("Login failed.")
            return False

    def logout(self):
        self.userID = ""
        self.loggedIn = False
        print("You have been logged out.")
        return True

    def viewAccountInformation(self):
        if self.loggedIn:
            account_info = self.get_account_info_from_db(self.userID)
            if account_info:
                print("Account Information:")
                for key, value in account_info.items():
                    print(f"{key}: {value}")
            else:
                print("Account information could not be retrieved.")
        else:
            print("You are not logged in.")

    def createAccount(self):
        email = input("Enter your email: ")
        password = input("Choose a password: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        address = input("Enter your address: ")
        city = input("Enter your city: ")
        state = input("Enter your state: ")
        zip = input("Enter your zipcode: ")
        payment = input("Enter your payment information: ")

        if self.create_account_in_db(email, password, first_name, last_name,address, city, state, zip, payment):
            print("Account created successfully.")
        else:
            print("Account creation failed.")

    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID

    # Actual database interaction methods
    def validate_credentials(self, email, password):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT UserId, Password FROM {self.tableName} WHERE Email = ?", (email,))
        result = cursor.fetchone()
        connection.close()
        return result and result[1] == password

    def get_user_id_from_db(self, email):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT UserId FROM {self.tableName} WHERE Email = ?", (email,))
        result = cursor.fetchone()
        connection.close()
        return result[0] if result else None

    def get_account_info_from_db(self, userID):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.tableName} WHERE UserId = ?", (userID,))
        columns = [column[0] for column in cursor.description]
        account_info = cursor.fetchone()
        connection.close()
        return dict(zip(columns, account_info)) if account_info else None

    def create_account_in_db(self, email, password, first_name, last_name, address, city, state, zip, payment):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO {self.tableName} (Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (email, password, first_name, last_name, address, city, state, zip, payment))
            connection.commit()
            connection.close()
            return True
        except sqlite3.IntegrityError:
            return False

    def set_database_name(self, databaseName):
        self.databaseName = databaseName

    def set_table_name(self, tableName):
        self.tableName = tableName
