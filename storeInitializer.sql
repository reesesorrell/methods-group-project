CREATE TABLE "Inventory" (
	"ISBN" INT NOT NULL,
	"Title" TEXT NOT NULL,
	"Author" TEXT NOT NULL,
	"Genre" TEXT NOT NULL,
	"Pages" INT NOT NULL,
	"ReleaseDate" TEXT NOT NULL,
	"Stock" INT NOT NULL,
	PRIMARY KEY ("ISBN")
);
CREATE TABLE "User" (
	"UserID" TEXT NOT NULL,
	"Email" TEXT NOT NULL,
	"Password" TEXT NOT NULL,
	"FirstName" TEXT NOT NULL,
	"LastName" TEXT NOT NULL,
	"Address" TEXT NOT NULL,
	"City" TEXT NOT NULL,
	"State" TEXT NOT NULL,
	"Zip" INT NOT NULL,
	"Payment" TEXT NOT NULL,
	PRIMARY KEY ("UserID")
);
CREATE TABLE "Cart" (
	"UserID" TEXT NOT NULL,
	"ISBN" INT NOT NULL,
	"Quantity" INT NOT NULL,  
	PRIMARY KEY ("UserID"),
	FOREIGN KEY (UserID) REFERENCES User(UserID),
	FOREIGN KEY (ISBN) REFERENCES Inventory(ISBN)
);
INSERT INTO Inventory (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) values (1, "Example Book1", "Author1", "Genre1", 100, "10/23/2016", 10);
INSERT INTO Inventory (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) values (2, "Example Book2", "Author2", "Genre2", 200, "10/24/2016", 20);
INSERT INTO Inventory (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) values (3, "Example Book3", "Author3", "Genre3", 300, "10/25/2016", 30);
INSERT INTO Inventory (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) values (4, "Example Book4", "Author4", "Genre4", 400, "10/26/2016", 40);
INSERT INTO Inventory (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) values (5, "Example Book5", "Author5", "Genre5", 500, "10/27/2016", 50);
INSERT INTO User (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) values ("username1", "username1@mail.com", "password1", "First1", "Last1", "101 Example Rd", "Starkville", "Mississippi", 10101, "PayPal");
INSERT INTO User (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) values ("username2", "username2@mail.com", "password2", "First2", "Last2", "102 Example Rd", "Starkville", "Mississippi", 10101, "Amex");
INSERT INTO User (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) values ("username3", "username3@mail.com", "password3", "First3", "Last3", "103 Example Rd", "Starkville", "Mississippi", 10101, "Chase");
SELECT * FROM Inventory;
SELECT * FROM User;
SELECT * FROM Cart;