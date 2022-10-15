# Project Name          : Hotel Management System
# Created by            : SAGAR YADAV

'''                 READ ME FIRST
Run this file if you are not able to run "The_Taj_Hotel by Sagar yadav.sql" file.
Then use the another python file named "Hotel_Management_System by Sagar yadav.py" 
Change the password from 'cnx' variable and enter your own password
Change the user if you have imported 'The_Taj_Hotel.sql' file in another user, other than root user.'''

from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'The_Taj_Hotel'
TABLES = {}

#  Creating Tables with thier Structures - Table Rooms
TABLES['Rooms'] = (
 '''create table Rooms (      
        RoomNo int PRIMARY key,
        Room_Type varchar(25) default 'AC',
        -- CREATED BY: SAGAR YADAV
        Rent float not null default '2500.00',
        Bed_Type varchar(15), 
        Room_Status varchar(15),
        CustomerID int default null) ENGINE=InnoDB''')

#  Creating Tables with thier Structures - Table Customers
TABLES['Customers'] = (
'''create table Customers (
        CustomerID int primary key AUTO_INCREMENT,
        CustomerName varchar(50) Not Null,
        Address varchar(70) Not null,
        Contact_No bigint default '1234567890',
        -- CREATED BY: SAGAR YADAV
        Email varchar(50) default 'Not Available',
        ID_Proof varchar(50) not null default 'Aadhar Card',
        Id_Number varchar(20) not null unique,
        Males int default '1', 
        Females int default '0',
        Children int default '0') 
        AUTO_INCREMENT = 101 ENGINE=InnoDB''')
# Created by Sagar Yadav 
#  Creating Tables with thier Structures - Table: Bookings
TABLES['Bookings'] = (
 '''CREATE TABLE Bookings (
        Book_id int primary key AUTO_INCREMENT,
        RoomNo int references Rooms(RoomNo),
        DateOfBooking date Not null, 
        -- CREATED BY: SAGAR YADAV
        DateOfLeaving date default null,
        Advance int DEFAULT '00',
        CustomerID varchar(50) Not null references customers.CustomerID,
        CustomerName varchar(50) Not Null)
        ENGINE=InnoDB AUTO_INCREMENT = 101 ''')

#  Creating Tables with thier Structures - Table Hotel_Details
TABLES['Hotel_Details'] = (
'''CREATE TABLE Hotel_Details (
        ID int primary key,
        -- CREATED BY: SAGAR YADAV
        Field_name varchar(30) Not NULL,
        Entry varchar(100) not NULL) ENGINE=InnoDB''')

# Table structure for table Bills
TABLES['Bills'] = (
'''CREATE TABLE Bills (
  Bill_id int NOT NULL AUTO_INCREMENT,
  Book_id int DEFAULT NULL references Bookings.Book_id,
  RoomNo int DEFAULT Null references rooms.RoomNo,
  Bill_date date DEFAULT NULL,
  GST int DEFAULT 42,
  ST int DEFAULT 26,
  Amount decimal DEFAULT NULL, 
  -- CREATED BY: SAGAR YADAV
  PRIMARY KEY (bill_id))
  AUTO_INCREMENT = 101 ENGINE=InnoDB''')

cnx = mysql.connector.connect(user='root',password = 'SAGAR YADAV')
cursor = cnx.cursor()
# Created by Sagar Yadav 
def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
try:
    cursor.execute("DROP DATABASE IF Exists The_Taj_Hotel;")
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
   # Created by Sagar Yadav 

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Dumping data for table `Hotel_Details`
Hotel_Details = ('''INSERT INTO Hotel_Details (ID, Field_name, Entry) VALUES
        (1, 'Hotel_Name', "The Taj Hotel"),
        (2, 'Address', 'ABC Sector, Delhi -22'),
        (3, 'Phone', '011-8000111,12,13'),
        (4, 'Email', 'thetajhotel_delhi@gmail.com'),
        (5, 'GST', '42'),
        (6, 'ST', '16')''')

cursor.execute(Hotel_Details)
print("Data dumped successfully in Table: Hotel_details")
cnx.commit()
cursor.close()
cnx.close()

