import sqlite3

class User:
    # Initializer or constructor method to create an instance of the User class
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = False
        self.userID = None

    # Method to handle user login
    def login(self):
        username = input("Enter email: ")  # Using email as the username for login
        password = input("Enter password: ")

        # Validate credentials with the database
        # If validation is successful, update login status and user ID
        if self.validate_credentials(username, password):
            self.loggedIn = True
            self.userID = self.get_user_id_from_db(username)
            print("Login successful.")
            return True
        else:
            print("Login failed.")
            return False

    # Method to handle user logout
    # Reset user ID and update login status
    def logout(self):
        self.userID = ""
        self.loggedIn = False
        print("You have been logged out.")
        return True

    # Method to view account information
    def viewAccountInformation(self):
        # Check if the user is logged in
        if self.loggedIn:
            # Retrieve account information from the database
            account_info = self.get_account_info_from_db(self.userID)
            if account_info:
                print("Account Information:")
                # Display the account information
                for key, value in account_info.items():
                    print(f"{key}: {value}")
            else:
                print("Account information could not be retrieved.")
        else:
            print("You are not logged in.")

    # Method to handle creation of a new account
    def createAccount(self):
        # Prompt user for account details
        email = input("Enter your email: ")
        password = input("Choose a password: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        address = input("Enter your address: ")
        city = input("Enter your city: ")
        state = input("Enter your state: ")
        zip = input("Enter your zipcode: ")
        payment = input("Enter your payment information: ")

        # Insert the new account details into the database
        if self.create_account_in_db(email, password, first_name, last_name,address, city, state, zip, payment):
            print("Account created successfully.")
        else:
            print("Account creation failed.")

    # Getter method to check if a user is logged in
    def getLoggedIn(self):
        return self.loggedIn

    # Getter method to retrieve the current user ID
    def getUserID(self):
        return self.userID

    # Method to validate user credentials against the database
    def validate_credentials(self, email, password):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        # Query to check if the email and password combination exists in the database
        cursor.execute(f"SELECT UserId, Password FROM {self.tableName} WHERE Email = ?", (email,))
        result = cursor.fetchone()
        connection.close()
        # Returns True if credentials match, otherwise False
        return result and result[1] == password

    # Method to retrieve the user ID from the database using the email
    def get_user_id_from_db(self, email):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT UserId FROM {self.tableName} WHERE Email = ?", (email,))
        result = cursor.fetchone()
        connection.close()
        # Return user ID if found, else return None
        return result[0] if result else None

    # Method to retrieve the account information for a given user ID
    def get_account_info_from_db(self, userID):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.tableName} WHERE UserId = ?", (userID,))
        columns = [column[0] for column in cursor.description]
        account_info = cursor.fetchone()
        connection.close()
        # Return a dictionary of the account info if found, else None
        return dict(zip(columns, account_info)) if account_info else None

    # Method to insert a new account record into the database
    def create_account_in_db(self, email, password, first_name, last_name, address, city, state, zip, payment):
        try:
            connection = sqlite3.connect(self.databaseName)
            cursor = connection.cursor()
            # SQL query to insert the new account data
            cursor.execute(f"INSERT INTO {self.tableName} (Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (email, password, first_name, last_name, address, city, state, zip, payment))
            connection.commit()
            connection.close()
            return True
        except sqlite3.IntegrityError:
            # If insertion fails due to an integrity error (like duplicate email), return False
            return False

    # Setter method to change the database name
    def set_database_name(self, databaseName):
        self.databaseName = databaseName

    # Setter method to change the table name
    def set_table_name(self, tableName):
        self.tableName = tableName
