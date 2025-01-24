import sqlite3

def createTables():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  CREATE TABLE IF NOT EXISTS Users (
    User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    Email VARCHAR(50)
    );
  """
  SQL_statement1 = """
  CREATE TABLE IF NOT EXISTS Clients (
    Client_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Company_name VARCHAR(150) NOT NULL,
    Description VARCHAR(150) 
    );
  """
  SQL_statement2 = """
  CREATE TABLE IF NOT EXISTS Products (
    Product_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_name VARCHAR(50) NOT NULL,
    Price DOUBLE,
    Description VARCHAR(150)
    );
  """
  SQL_statement3 = """
  CREATE TABLE IF NOT EXISTS Warehouse (
    Warehouse_NR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_ID INTEGER,
    Amount INTEGER
    );
  """
  SQL_statement4 = """
  CREATE TABLE IF NOT EXISTS Orders (
    Order_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_ID INTEGER,
    Client_ID INTEGER,
    User_ID INTEGER,
    Amount INTEGER,
    Date_purchased DATETIME,
    Date_shipped DATETIME
    );
  """
  c.execute(SQL_statement)
  c.execute(SQL_statement1)
  c.execute(SQL_statement2)
  c.execute(SQL_statement3)
  c.execute(SQL_statement4)
  conn.commit()
  c.close()
  conn.close()
  return True

def populateUsers():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  INSERT INTO Users (Username, Password, Email) VALUES ('user', 'user', 'tzirw@example.com');
  """
  SQL_statement1 = """
  INSERT INTO Users (Username, Password, Email) VALUES ('admin', 'admin', 'tzirw@example.com');
  """
  c.execute(SQL_statement)
  c.execute(SQL_statement1)
  conn.commit()
  c.close()
  conn.close()
  return True

def populateClients():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  INSERT INTO Clients (Company_name, Description) VALUES ('Client 1', 'Description 1');
  """
  SQL_statement1 = """
  INSERT INTO Clients (Company_name, Description) VALUES ('Client 2', 'Description 2');
  """
  c.execute(SQL_statement)
  c.execute(SQL_statement1)
  conn.commit()
  c.close()
  conn.close()
  return True
  
def populateProducts():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  INSERT INTO Products (Product_name, Price, Description) VALUES ('Zeķes sarkanas', 1, 'Description 1');
  """
  SQL_statement1 = """
  INSERT INTO Products (Product_name, Price, Description) VALUES ('Zilas zeķes', 2, 'Description 2');
  """
  c.execute(SQL_statement)
  c.execute(SQL_statement1)
  conn.commit()
  c.close()
  conn.close()
  return True

def populateWarehouse():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  INSERT INTO Warehouse (Product_ID, Amount) VALUES (1, 100);
  """
  SQL_statement1 = """
  INSERT INTO Warehouse (Product_ID, Amount) VALUES (1, 300);
  """
  c.execute(SQL_statement)
  c.execute(SQL_statement1)
  conn.commit()
  c.close()
  conn.close()
  return True

def populateOrders():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  INSERT INTO Orders (Product_ID, Client_ID,User_ID,Amount,Date_purchased,Date_shipped) VALUES (1,1,1,50,'2023-01-01','2023-01-01');
  """
  SQL_statement1 = """
  INSERT INTO Orders (Product_ID, Client_ID,User_ID,Amount,Date_purchased,Date_shipped) VALUES (2,2,2,10,'2023-01-01','2023-01-01');
  """
  c.execute(SQL_statement)
  c.execute(SQL_statement1)
  conn.commit()
  c.close()
  conn.close()
  return True

def checkIfUserExists(username,password):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  SELECT * FROM Users WHERE Username = ? AND Password = ?
  """
  c.execute(SQL_statement,(username,password))
  result = c.fetchone()
  c.close()
  conn.close()
  if result == None:
    return False
  else:
    return True

def selectAllUsers():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  SELECT * FROM Users
  """
  c.execute(SQL_statement)
  result = c.fetchall()
  c.close()
  conn.close()
  return result
  
def selectAllProducts():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  SELECT * FROM Products
  """
  c.execute(SQL_statement)
  result = c.fetchall()
  c.close()
  conn.close()
  return result

def selectAllClients():
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  SELECT * FROM Clients
  """
  c.execute(SQL_statement)
  result = c.fetchall()
  c.close()
  conn.close()
  return result

def selectUserById(userid):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  SELECT * FROM Users WHERE User_ID = ?
  """
  c.execute(SQL_statement,(userid))
  result = c.fetchone()
  c.close()
  conn.close()
  return result

def selectProductById(productid):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  SQL_statement = """
  SELECT * FROM Products WHERE Product_ID = ?
  """
  c.execute(SQL_statement,(productid))
  result = c.fetchone()
  c.close()
  conn.close()
  return result

def updateUser(userid,username,password,email):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  c.execute("UPDATE Users SET Username = ?, Password = ?, Email = ? WHERE User_ID = ?",(username,password,email,str(userid)))
  conn.commit()
  c.close()
  conn.close()
  return True
  
def updateProduct(productid,productname,price,description):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  c.execute("UPDATE Products SET Product_name = ?, Price = ?, Description = ? WHERE Product_ID = ?",(productname,price,description,productid))
  conn.commit()
  c.close()
  conn.close()
  return True

def addUser(username,password,email):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  c.execute("INSERT INTO Users (Username, Password, Email) VALUES (?,?,?)",(username,password,email))
  conn.commit()
  c.close()
  conn.close()
  return True

def addProduct(productname,price,description):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  c.execute("INSERT INTO Products (Product_name, Price, Description) VALUES (?,?,?)",(productname,price,description))
  conn.commit()
  c.close()
  conn.close()
  return True

def deleteUser(userid):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  c.execute("DELETE FROM Users WHERE User_ID = ?",(str(userid)))
  conn.commit()
  c.close()
  conn.close()
  return True

def deleteProduct(productid):
  conn = sqlite3.connect('database.sql',timeout=10)
  c = conn.cursor()
  c.execute("DELETE FROM Products WHERE Product_ID = ?",(str(productid)))
  conn.commit()
  c.close()
  conn.close()
  return True