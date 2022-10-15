# The_Taj_Hotel SQL Script
# Created by: SAGAR YADAV
/*
Execute this script in your SQL database server first.
*/
#  Creating Database
drop database if exists The_Taj_Hotel;
CREATE database The_Taj_Hotel;
                    -- CREATED BY: SAGAR YADAV
#  Using the database "The_Taj_Hotel"
use The_Taj_Hotel;
                    
#  Creating Tables with thier Structures - Table Rooms
create table Rooms (
  -- RoomID int primary key AUTO_INCREMENT,
  RoomNo int PRIMARY key,
  Room_Type varchar(25) default 'AC',
  Rent float not null default '2500.00',
  Bed_Type varchar(15), 
  Room_Status varchar(15),
  CustomerID int default null)
  ENGINE=InnoDB AUTO_INCREMENT = 101;
                     -- CREATED BY: SAGAR YADAV 
#  Creating Tables with thier Structures - Table Customers
create table Customers (
  CustomerID int primary key AUTO_INCREMENT,
  CustomerName varchar(50) Not Null,
  Address varchar(70) Not null,
  Contact_No bigint default '1234567890',
  Email varchar(50) default 'Not Available',
  ID_Proof varchar(50) not null default 'Aadhar Card',
  Id_Number varchar(20) not null unique,
  Males int default '1', 
  Females int default '0',
  Children int default '0') 
  AUTO_INCREMENT = 101 ENGINE=InnoDB;
                          -- CREATED BY: SAGAR YADAV
#  Creating Tables with thier Structures - Table: Bookings
CREATE TABLE Bookings (
  Book_id int primary key AUTO_INCREMENT,
  RoomNo int references Rooms(RoomNo),
  DateOfBooking date Not null, 
  DateOfLeaving date default null,
  Advance int DEFAULT '00',
  CustomerID varchar(50) Not null references customers.CustomerID,
  CustomerName varchar(50) Not Null)
  AUTO_INCREMENT = 101 ENGINE=InnoDB;
                                -- CREATED BY: SAGAR YADAV
#  Creating Tables with thier Structures - Table Hotel_Details
CREATE TABLE Hotel_Details (
  ID int primary key,
  Field_name varchar(30) Not NULL,
  Entry varchar(100) not NULL)
  ENGINE=InnoDB;
                               -- CREATED BY: SAGAR YADAV
# Dumping data for table `Hotel_Details`
INSERT INTO Hotel_Details (ID, Field_name, Entry) VALUES
(1, 'Hotel_Name', "The Taj Hotel"),
(2, 'Address', 'ABC Sector, Delhi -22'),
(3, 'Phone', '011-8000111,12,13'),
(4, 'Email', 'thetajhotel_delhi@gmail.com'),
(5, 'GST', '42'),
(6, 'ST', '16');

          -- CREATED BY: SAGAR YADAV
# Table structure for table Bills
CREATE TABLE Bills (
  Bill_id int NOT NULL AUTO_INCREMENT,
  Book_id int DEFAULT NULL references Bookings.Book_id,
  RoomNo int DEFAULT Null references rooms.RoomNo,
  Bill_date date DEFAULT NULL,
  GST int DEFAULT 42,
  ST int DEFAULT 26,
  Amount decimal DEFAULT NULL, 
  -- CREATED BY: SAGAR YADAV
  PRIMARY KEY (bill_id))
  ENGINE=InnoDB AUTO_INCREMENT = 101;
  -- CREATED BY: SAGAR YADAV

# DROP database The_Taj_Hotel;
-- CREATED BY: SAGAR YADAV
commit
