# Project Name          : Hotel Management System
# Created by            : SAGAR YADAV

"""   ~~~~~~~~~~~~~~~~~~~~~~~~~ HOW TO RUN ~~~~~~~~~~~~~~~~~~~~~~~~~ 
Make sure that you have installed "mysql.connector" library or module.
Also make sure you have imported the sql script, named "The_Taj_Hotel.sql", or
Run the "Creating Table for running HMS file.py" file first 
then use this file "Hotel_Management_System by Sagar yadav.py"
Change the password from every 'conn' variable and enter your own password.
Change the user if you have imported 'The_Taj_Hotel.sql' file in another user, other than root user.
Change the host if you have another host.
Run it on Desktop or Laptop for best results.
For further guidance check out the document.
"""

# Importing Libraries:
import mysql.connector
from datetime import date, datetime

# Global variables:
hotel_name =''
addr =''
phone=''
email =''
gst=42
st =13

# 1. Function for Getting Hotel Details:
def hotelDetails():
  global hotel_name
  global addr
  global phone
  global email
  global gst
  global st
  conn = mysql.connector.connect(
    host='localhost', database='The_Taj_Hotel', 
    user='root', password='SAGAR YADAV')
  cursor = conn.cursor()
  sql = "select * from Hotel_Details;"
  cursor.execute(sql)
  records = cursor.fetchmany(6)
  for record in records: 
    if record[1]=='Hotel_Name':
       hotel_name = record[2]
    if record[1] == 'Address':
       addr = record[2]
    if record[1] == 'Phone':
       phone = record[2]
    if record[1] == 'Email':
       email = record[2]
    if record[1] == 'GST':
       gst = record[2]
    if record[1] == 'ST':
       st = record[2]
  print("\n\n")
  print("\tDATE : ", date.today())
  print("\t ~~~~~~~~~~~~~ HOTEL DETAILS ~~~~~~~~~~~~~ \n")
  print("\tHotel Name     : ", hotel_name)
  print("\tAddress        : ", addr)
  print("\tPhone No.      : ", phone)
  print("\tEmail          : ", email)
  print("\tCurrent GST    : ", gst)
  print("\tCurrent ST     : ", st)
  greet()
  wait = input("\nEnter any key to continue............. >")

# 2. Function for Changing Hotel Details:
def change_hotelDetails():
    conn = mysql.connector.connect(
      host='localhost', database = 'The_Taj_Hotel', 
      user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    clear()
    print('Change Hotel Details : ')
    print('-'*75)
    print('1.Hotel Name')
    print('2.Hotel Address')
    print('3.Phone Number(s)')
    print('4.Email ID')
    print('5.Current GST Rate')
    print('6.Current Service Rate')
    print('7.Return to main menu')
    choice = int(input('Enter your choice :'))
    if choice == 7:
      main_menu()
    else :
      print("\n\n\tInvalid input")
      wait = input('\n\n\n\
        .............Press any key to start again......') 
      main_menu()
    value = input('Enter new value :')
    sql ="update hotel_Details \
      set ENTRY = '{}'\
        WHERE id = {};".format(value, choice)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    greet()
    wait = input('\n\n\n Record Updated \
      .............Press Enter to continue......') 
  
# 3. Function to check whether the room exist
def room_exist(room_no):
    conn = mysql.connector.connect(
      host='localhost', database = 'The_Taj_Hotel', 
      user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    sql ="select * from rooms \
      where RoomNo = {};".format(room_no)
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

# 4. Function to check whether the customer exist
def customer_exist(cust_no):
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    sql = "select * from customers \
      where CustomerID = {};".format(cust_no)
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

# 5. Function to add or create a new room
def add_room():
  conn = mysql.connector.connect(
      host='localhost', database = 'The_Taj_Hotel', 
      user='root', password='SAGAR YADAV')
  cursor = conn.cursor()
  clear()
  print('Add New Room - Screen')
  print('-'*75)
  room_no = input('\n Enter Room No.(Starts from 101) :> ')
  if room_exist(room_no) is not None:
    print("\t\tNOTE: Room No",room_no,
      "already exists in our database")
    room_no = input('\n Enter Another Room No. :> ')
  print("\nFor Room no.", room_no, "-->")
  room_type_choice = int(input('''Available Room Types - 
    1. AC
    2. Non-AC
    3. DELUX
    4. Super Delux
    5. Queen Delight
    6. Kings Special
    7. Super Rich Special
    Select your choice:> '''))
  if room_type_choice == 1:
    room_type = 'AC'
  if room_type_choice == 2:
    room_type = 'Non-AC'
  if room_type_choice == 3:
    room_type = 'Delux'
  if room_type_choice == 4:
    room_type = 'Super Delux'
  if room_type_choice == 5:
    room_type = 'Queen Delight'
  if room_type_choice == 6:
    room_type = 'King Special'
  if room_type_choice == 7:
    room_type = 'Super Rich Special'
  if room_type_choice not in (1,2,3,4,5,6,7):
    print("Invalid Input.....")
  print("\n\t\tBed Selection ------------ Menu")
  print("\nFor Room no.", room_no, "-->")
  room_bed_choice = int(input('''\nAvialable Room Bed Types are:
    1. Single
    2. Double
    3. Triple 
    Select your bed choice :> '''))
  if room_bed_choice == 1:
    room_bed = 'Single bed'
  if room_bed_choice == 2:
    room_bed = 'Double bed'
  if room_bed_choice == 3:
    room_bed = 'Triple bed'
  if room_bed_choice not in (1,2,3,4,5,6,7):
    print("Invalid Input.....")
  print("\n\t\tRent -------------------------------- Menu")
  print('''Available room rents for "Single bed" are:
    1. AC                 : ₹3499/night
    2. Non-AC             : ₹1499/night
    3. Delux              : ₹4799/night
    4. Super Delux        : ₹5499/night
    5. Queen Delight      : ₹6999/night
    6. King Special       : ₹8999/night
    7. Super Rich Special : ₹10499/night
    \t\tNOTE: Rent changes as per bed there is addition of Rs.1000 per bed(type)''')
  wait = input('\n Press Enter to continue....')
  if room_type == 'AC':
    room_rent_selection = 1
  elif room_type == 'Non-AC':
    room_rent_selection = 2
  elif room_type == 'Delux':
    room_rent_selection = 3
  elif room_type == 'Super Delux':
    room_rent_selection = 4
  elif room_type == 'Queen Delight':
    room_rent_selection = 5
  elif room_type == 'King Special':
    room_rent_selection = 6
  elif room_type == 'Super Rich Special':
    room_rent_selection = 7
  else :
    pass
  # 1. AC Room rent
  if room_rent_selection == 1:
    if room_bed == 'Single bed':
      room_rent = 3499
    elif room_bed == 'Double bed':
      room_rent = 3499 + 1000
    elif room_bed == 'Triple bed':
      room_rent = 3499 + 2000
  # 2. Non-AC Room rent
  if room_rent_selection == 2:
    if room_bed == 'Single bed':
      room_rent = 1499
    elif room_bed == 'Double bed':
      room_rent = 1499 + 1000
    elif room_bed == 'Triple bed':
      room_rent = 1499 + 2000
  # 3. Delux Room rent
  if room_rent_selection == 3:
    if room_bed == 'Single bed':
      room_rent = 4799
    elif room_bed == 'Double bed':
      room_rent = 4799 + 1000
    elif room_bed == 'Triple bed':
      room_rent = 4799 + 2000
  # 4. Super delux Room rent
  if room_rent_selection == 4:
    if room_bed == 'Single bed':
      room_rent = 5499
    elif room_bed == 'Double bed':
      room_rent = 5499 + 1000
    elif room_bed == 'Triple bed':
      room_rent = 5499 + 2000
  # 5. Queen delight Room rent  
  if room_rent_selection == 5:
    if room_bed == 'Single bed':
      room_rent = 6999
    elif room_bed == 'Double bed':
      room_rent = 6999 + 1000
    elif room_bed == 'Triple bed':
      room_rent = 6999 + 2000
  # 6. King Special Room rent  
  if room_rent_selection == 6:
    if room_bed == 'Single bed':
      room_rent = 8499
    elif room_bed == 'Double bed':
      room_rent = 8499 + 1000
    elif room_bed == 'Triple bed':
      room_rent = 8499 + 2000
  # 7. Super rich special Room rent  
  if room_rent_selection == 7:
    if room_bed == 'Single bed':
      room_rent = 10499
    elif room_bed == 'Double bed':
      room_rent = 10499 + 1000
    elif room_bed == 'Triple bed':
      room_rent = 10499 + 2000
  if room_rent_selection not in (1,2,3,4,5,6,7):
    print("Invalid Input.....")
    add_room()
  print('\nFor ----->')
  print("Room Number               :", room_no)
  print("Room Bed Type             :", room_bed)
  print("Room Type                 :", room_type)
  print("Your Rent will be (in Rs) :", room_rent)
  room_rent = str(room_rent)
  sql = 'insert into rooms(RoomNo, room_type,\
     rent, bed_type, room_status) values \
        ('+room_no+',"'+ room_type.upper()+'",\
          '+room_rent+',"'+room_bed.upper()+'","Free");'
  cursor.execute(sql)
  conn.commit()
  print("\n Room added successfully....")
  conn.close()
  greet()
  wait = input('\n\n\n Press Enter to continue....')

# 6. Function to modify room's data
def modify_room():
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    clear()
    print(' Change Room Information ')
    print('-'*75)
    print("NOTE: Rooms starts from 101...")
    room_no  = int(input('Enter Room No. :'))
    while True:
      check = room_exist(room_no)
      if check == None:
        print('Room doesn`t exist....')
        print("""Select any one from below -
        1. Want to enter another room no.
        2. Return to main menu
        3. Close application or Exit""")
        choice = int(input("Enter your choice :> "))
        if choice == 1:
          room_no = input('Enter Another Room no to modify :> ')
        elif choice == 2:
          main_menu()
        elif choice == 3:
          greet()
          break
        else:
          print("Invalid Input!")
          print("Exiting..........")
          greet()
          break
      elif check != None:
        print("\n\tAvailable details of Room No.",room_no)
        print('''
        Room Type     : {}
        Room Bedding  : {}
        Room Rent     : {}
        Room Status   : {}'''.format(check[1],
        check[3],check[2],check[4]))
        wait = input("Press Enter to continue.....")
        print("\n\t Choose what you want to modify")
        print()
        print('1.Room Type')
        print('2.Room Rent')
        print('3.Room Bed')
        print('4.Room Status (free/occupied)')
        choice = int(input('Enter your choice : '))
        field_name = ''
        if choice == 1: # Room Type
          print('''Available room types are:
          AC
          Non-AC
          Delux
          Super Delux
          Queen Delight
          King Special
          Super Rich Special''')
          field_name = 'Room_Type'
        if choice == 2: # Room rent
          print('''Available room rents for single bed are:
          AC                 ₹3499/night
          Non-AC             ₹1499/night
          Delux              ₹4799/night
          Super Delux        ₹5999/night
          Queen Delight      ₹6999/night
          King Special       ₹8999/night
          Super Rich Special ₹10499/night''')
          field_name = 'rent'
        if choice == 3: # Room's bed type
          print('''Available Bed Types are:
          Single Bed
          Double Bed
          Triple Bed ''')
          field_name = 'bed_type'
        if choice == 4: # Room's status
          print('''Available Status are:
          Free
          Occupied''')
          field_name = 'Room_Status'
        value = input('Enter new value(Type the new value):> ')
        if value.isdigit():
          sql = "update rooms set {} = {} \
            where RoomNo = {};".format(field_name, value, room_no)
        else:
          sql = "update rooms set {} = '{}' \
            where RoomNo = {};".format(field_name, value.upper(), room_no)
        cursor.execute(sql)
        conn.commit()
        greet()
        wait = input('''\n\n\n Record Updated \n
          .............Press Enter to continue......''')
        break

# 7. Function to add customer
def add_customer():
  conn = mysql.connector.connect(
      host='localhost', database = 'The_Taj_Hotel', 
      user='root', password='SAGAR YADAV')
  cursor = conn.cursor()
  clear()
  print('Add New Customer - Screen')
  print('-'*75)
  name = input('\n Enter Customer Name :> ')
  address = input('\n Enter Customer Address:> ')
  phone = input('\n Enter Customer Contact No. :> ')
  email = input('\n Enter Customer Email ID :')
  id_proof = input('\n Enter Customer ID Proof type\
    (e.g,Aadhar/Passport/DL/VoterID) :> ')
  id_proof_no = input('\n Enter Customer ID proof No. :> ')
  males = input('\n Enter Total Males :>')
  females = input('\n Enter Total Females :> ')
  children = input('\n Enter Total Children :> ')
  noOfRoomMates = males + females + children
  sql1 = 'insert into customers\
    (CustomerName,address,Contact_No,email,id_proof,id_number\
      ,males,females,children) values \
        ("'+name+'","' + address.upper()+'","'+phone+'",\
          "'+email.upper()+'","'+id_proof.upper()+'","'+id_proof_no.upper()+'",\
            '+males+','+females+','+children+');'
  cursor.execute(sql1)
  sql2 = "select * from customers where id_number = '{}' ;".format(id_proof_no)
  cursor.execute(sql2)
  data = cursor.fetchone()
  print('\n\n\nCustomer Added successfully ...............')
  print("Customer Details ---")
  print("Customer No. :", data[0])
  print("Name         :", data[1])
  print("Address      :", data[2])
  print("Contact No.  :", data[3])
  print("Email        :", data[4])
  print("ID Proof     :", data[5])
  print("ID Proof No. :", data[6])
  print("Males        :", data[7])
  print("Female       :", data[8])
  print("Children     :", data[9])
  conn.commit()
  conn.close()
  greet()
  wait = input('\n\n\n Press Enter to continue....')

# 8. Function to modify customer details
def modify_customer():
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    clear()
    print(' Change Customer Information ')
    print('-'*75)
    cust_no = input('Enter Customer No., whoose information you want to change :>')
    while True:
      check = customer_exist(cust_no)
      if check == None:
        print('Customer doesn`t exist for this Customer Number,',cust_no,'....')
        print("""Now, Select any one option from below -
        1. Want to enter another Customer No.
        2. Return to main menu
        3. Close application or Exit""")
        choice = int(input("Enter your choice :> "))
        if choice == 1:
          cust_no = input('Enter Another Customer No. to modify :> ')
        elif choice == 2:
          main_menu()
        elif choice == 3:
          break
        else:
          print("Invalid Input!")
          print("Exiting..........")
          break
      elif check != None:        
        print("\n\tAvailable details of Customer No.",cust_no,'......')
        print('''
        Name            : {}
        Address         : {}
        Phone No.       : {}
        Email           : {}
        ID Proof        : {}
        ID Proof No.    : {}
        No. of males    : {}
        No. of females  : {}
        No. of children : {} '''.format(check[1],check[2],check[3],
        check[4],check[5],check[6],check[7],check[8],check[9]))
        wait = input("\nPress Enter to continue.....")
        print("\n\t Choose what you want to modify")
        print()
        print('1.Name')
        print('2.Address')
        print('3.Phone No')
        print('4.Email ID')
        print('5.ID Proof')
        print('6.ID Proof No')
        print('7.Males')
        print('8.Females')
        print('9.Childeren')
        choice = int(input('Enter your choice :'))
        field_name = ''
        if choice == 1:
          field_name = 'CustomerName'
        if choice == 2:
          field_name = 'Address'
        if choice == 3:
          field_name = 'Contact_No'
        if choice == 4:
          field_name = 'email'
        if choice == 5:
          field_name = 'id_proof'
        if choice == 6:
          field_name = 'ID_Number'
        if choice == 7:
          field_name = 'males'
        if choice == 8:
          field_name = 'females'
        if choice == 9:
          field_name = 'children'
        value = input('Enter new value :')
        if value.isdigit():
          sql = sql = 'update customers set {} = {} where CustomerID ={};'.format(
              field_name, value, cust_no)
        else:
          sql = sql = 'update customers set {} = "{}" where CustomerID ={};'.format(
              field_name, value, cust_no)
        cursor.execute(sql)
        conn.commit()
        greet()
        wait = input(
            '\n\n\n Record Updated .............Press Enter to continue......')
        break

# 9. Function to book room
def room_booking():
    conn = mysql.connector.connect(
        host = 'localhost', database ='the_taj_hotel',
        user = 'root', password = 'SAGAR YADAV')
    cursor = conn.cursor()
    clear()
    print("Room Booking -------- Menu")
    print("*"*20)
    room_no = int(input("\nEnter Room No. :> "))    
    while True:
        query1 = "SELECT * From rooms where roomno = {};".format(room_no)
        cursor.execute(query1)
        data = cursor.fetchone()
        query2 = "Select book_id, roomno, bill_date from bills where roomno = {};".format(room_no)
        cursor.execute(query2)
        record = cursor.fetchone()
        if record == None:
            rmno = 0
            pass
        else:
            book_id, rmno, billdate = record[0], record[1], record[2]                 
        if data != None and data[4] in ('free', 'Free'):
            print("\nDetails for the Room No.", room_no)
            room_no = data[0]
            roomtype = data[1]
            roomrent = data[2]
            roombed = data[3]            
            print("Room No.     :",room_no)
            print("Room Type    :",roomtype)
            print("Room Rent    :",roomrent)
            print("Room Bedding :",roombed)            
            cust_no = int(input("Enter Customer Id or No. :> "))
            query2 = "SELECT * From customers where customerID = {};".format(cust_no)
            cursor.execute(query2)
            data2 = cursor.fetchone()
            cName = data2[1]
            if customer_exist(cust_no) != None :
                if rmno == room_no:
                    print("""The Date of Occupancy should be 
                    equal to or greater than the date :""", billdate)
                    DateOfBooking = datetime.strptime(input('Enter date of occupancy (yyyy-mm-dd) :> '), '%Y-%m-%d')
                    if DateOfBooking.date() >= billdate:
                        pass
                    else :
                        print("Please enter a right date")                
                        DateOfBooking = input('Enter again date of occupancy (yyyy-mm-dd) :> ')
                else:
                    DateOfBooking = input('Enter date of occupancy (yyyy-mm-dd) :> ')
                advance = input('Enter advance amount :> ')
                sql1 = 'update rooms \
                    set Room_status = "Occupied",\
                        CustomerID = {} \
                            where Roomno = {};'.format(cust_no,room_no)
                sql2 = 'insert into bookings\
                    (roomno,customerid,DateOfBooking,advance,customername) \
                        values ({}, {}, "{}", {}, "{}");'.format(room_no, 
                        cust_no, DateOfBooking, advance, cName)
                cursor.execute(sql1)
                cursor.execute(sql2)
                print('\n\n\nRoom no ', room_no, 'a ',roomtype,' Room is booked for---')
                print('Customer No.  :', cust_no)
                print("Customer Name :", cName)
                conn.commit()
                conn.close()
                wait = input('\n Press Enter to continue....')
                break
            else :
                print("\tNOTE:Customer ID you entered is not present in our database.")
        elif data == None:
            print("There is no such room found in our database, Room No.", room_no)
            room_no = int(input("\nEnter Another Room No. :> "))
        else :
            print("NOTE: This room (", room_no,") is not available for booking")
            print("It is Already Booked!.....")
            room_no = int(input("\nEnter Another Room No. :> "))

# 10. Function to generate bill
def bill_generation(): 
    global gst
    global st
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    print("BILL GENERATION ------- SCREEN")
    print(35*'*')
    room_no = input('Enter Room No. for which you want to generate bill :> ')
    while True:
        query1 = "SELECT r.room_type, b.customerid, dateofleaving,\
            dateofbooking, advance, r.rent, b.book_id, r.bed_type, r.roomno \
            FROM bookings b, rooms r \
                WHERE r.roomno = b.roomno and r.roomno = {};".format(room_no)      
        cursor.execute(query1)
        data = cursor.fetchall()
        checkRoomExist = room_exist(room_no)
        if checkRoomExist == None:
            print("\nNOTE: This room doesn't exist in our database,Room no.", room_no)
            print("\tYou have to create a new room")
            print("Exiting Bill Generation Menu........")
            wait = input('\nPress Enter to continue....')
            break
        else :
            pass
        if data == []:
            print("NOTE:Enter Another Room No., there is no booking for this room no.",room_no)
            wait = input('\n Press Enter to continue....')
            choice = int(input('''Select any one option-
            1. Want to enter another room no
            2. Return to Main Menu
            3. Return back
            :> '''))
            if choice == 1:
                room_no = input('Enter Another Room No. for which you want to generate bill :> ')
            elif choice == 2:
                main_menu()
                pass
            elif choice == 3:
                break
            else:
                print("Invalid Input!")
                print("Exiting..........")
                break
        else:
            for rm_t, c_id, dl, db, adv, rent, bookid, bedtype, rmno in data:               
                room_type, cust_id, dolv, roombed, roomno = rm_t, c_id, dl, bedtype, rmno
                doo, advance, rent, book_id = db, adv, rent, bookid
            if dolv != None :
                print("\n\tNOTE: This room has already a bill...")
                wait = input('\n Press Enter to continue....')
                choice = int(input('''Select any one option-
                    1. Want to enter another room id
                    2. Return to Main Menu
                    3. Close application or Exit
                    :> '''))
                if choice == 1:
                    room_no = input('Enter Another Room no. for which you want to generate bill :> ')
                elif choice == 2:
                    main_menu()
                    pass
                elif choice == 3:
                    break
                else:
                    print("Invalid Input!")
                    print("Exiting..........")
                    break
            elif dolv == None:
                query2 = "SELECT customername, address\
                    FROM customers\
                        Where customerid = {};".format(cust_id)
                cursor.execute(query2)
                data = cursor.fetchone()
                cname, caddr = data[0], data[1]
                print('''\tRoom Detail or Booking Details
                \t-----------------------------------------
                Room No.             : {}
                Room Name            : {}
                Room Bedding         : {}
                Room Rent(Per night) : {}
                Customer ID          : {}
                Customer Name        : {}
                Customer Address     : {}
                Advance paid         : {}'''.format(roomno, room_type, roombed, rent, cust_id, cname, caddr, advance))
                wait = input('\nPress Enter to continue....')
                clear()
                print('Bill Generation ')
                print('-'*75)
                print('Room occupied  :',room_no)
                dol = date.today()            
                total_days = (dol-doo).days
                amount = total_days*rent
                gst_amount = amount*int(gst)/100
                st_amount = amount*int(st)/100
                payable_amount = total_days * rent - advance + gst_amount + st_amount
                if dol == doo:
                  if room_type == "SUPER RICH SPECIAL":
                    charge = 1500
                  elif room_type == "KING SPECIAL":
                    charge = 1200
                  elif room_type == "QUEEN DELIGHT":
                    charge = 1000
                  elif room_type == "SUPER DELUX":
                    charge = 800
                  elif room_type == "DELUX":
                    charge = 550
                  elif room_type == "AC":
                    charge = 275
                  elif room_type == "NON-AC":
                    charge = 150
                  payable_amount = rent - advance + gst_amount + st_amount + charge
                  print("You have been for charged by Rs.", charge, 'as you are leaving same day..')
                else:
                  pass
                print('Date of Occupancy :',doo, '\nDate of Leaving :',dol)
                print('Total Payable Days : ', total_days)
                print('Room Rent Per Day : ', rent)
                print('Total Amount  :',amount)
                print('Advance :',advance,'\nGST   : {} '.format(gst,gst_amount), '\nService Tax  : {}'.format(st,st_amount))
                print('Amount Payable :',payable_amount)
                sql1 = 'update rooms set room_status ="free" \
                where roomno ='+room_no +';'
                sql2 = 'update bookings set DateOfLeaving ="'+str(dol)+'" \
                where roomno='+room_no+' and customerid ='+cust_id +';'    
                sql3 = 'insert into bills(book_id,amount,bill_date,gst,st,roomno) \
                values('+str(book_id)+','+str(payable_amount)+',"'+str(dol)+'",'+str(gst)+','+str(st)+','+str(roomno)+');'                
                cursor.execute(sql1)
                cursor.execute(sql2)
                cursor.execute(sql3)
                conn.commit()
                conn.close()
                print("Bill Generated successfully....")
                print('This room is Free now, Room No.:',roomno)
                wait = input('\n\n Press Enter to continue....')
                break

# 11. Function to search rooms
def search_rooms(): 
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    room_no = input('Enter Room No :')
    check = room_exist(room_no)
    if check is not None:
      sql ='select * from rooms where roomno ='+room_no +';'
      cursor.execute(sql)
      record = cursor.fetchone()
      clear()
      print('-'*75)
      print('Room Info ---')
      print('Room No. :',record[0])
      print('Room Type :',record[1])
      print('Room Rent :',record[2])
      print('Room Bed :',record[3])
      print('Room Status :',record[4])
      print('Booked for Customer No. :', record[5])
      conn.close()
    else :
      print("\nThis Room doesn't exist............")
    wait = input('\n\n\nPress Enter to continue......')

# 12. Function to search customer's details
def search_customer():
  while True:
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()    
    clear()
    print('Search Customer DataBase')
    print('-'*75)
    print("\nBy which data you want to search--")
    print('1.by Customer ID')
    print('2.by Customer Name')
    print('3.by Customer Address')
    print('4.by Customer Phone')
    print('5.by Customer Email')
    print('6.by ID Proof')
    print('7.by ID Proof no.')
    print('8.Return to back menu')
    choice = int(input('\n\tEnter your choice by which u want to search : '))
    field_name =''
    if choice ==1:
      field_name = 'CustomerID'
    if choice ==2:
      field_name = 'CustomerName'
    if choice ==3:
      field_name = 'address'
    if choice ==4:
      field_name = 'Contact_No'
    if choice ==5:
      field_name = 'email'
    if choice ==6:
      field_name = 'id_proof'
    if choice ==7:
      field_name = 'id_number'
    if choice ==8:
      break
    value = input('Enter value that you want to search :')
    if field_name =='CustomerID':
      sql = 'select * from customers where '+ field_name +' = '+ value + ';'
    else:
      sql = 'select * from customers where ' + field_name + ' like "%' + value + '%";'
    cursor.execute(sql)
    records = cursor.fetchall()
    # checking for record
    if records == []:
      print('*' * 45)
      print('Search Result for {} = {} : NOT FOUND'.format(field_name,value))
      wait = input('\n\n\nPress Enter to continue......')
      break
    else :
      pass
    clear()
    print('Search Result for {} = {}'.format(field_name,value))
    print('*'*80)
    for record in records:
      print('''
      Customer ID   : {} 
      Customer Name : {} 
      Address       : {} 
      Contact No.   : {} 
      Email         : {} 
      ID Proof      : {} 
      ID Proof No.  : {}'''.format(
          record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
    conn.close()
    greet()
    wait = input('\n\n\nPress Enter to continue......')
    break

# 13. Function to search for bookings
def search_booking():
  while True:
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    cust_no = input('Enter Customer No :')
    sql = 'select book_id,r.roomno,c.Customername,DateOfBooking,advance from bookings b, customers c, rooms r where b.roomno = r.roomno AND b.customerid = '+cust_no+' and DateOfLeaving is NULL;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Booking information for customer ID :{}'.format(cust_no))
    print('*'*50)
    if records == []:
      print("NOTE: There is no booking for this Customer no.",cust_no)
      wait = input('\n Press Enter to continue....')
      choice = int(input('''Select any one option-
      1. Want to enter another room no
      2. Return to Main Menu
      3. Return to Search menu
      :> '''))
      if choice == 1:
        cust_no = input('Enter Another Customer No.:> ')
      elif choice == 2:
        main_menu()
        pass
      elif choice == 3:
        break
      else:
        print("Invalid Input!")
        print("Returning to Search menu.........")
        break
    else:
      for record in records:
        print('''\tCustomer ID :\t{}
        Room Number :\t{}
        Customer`s Name :\t{} 
        Date Of Booking :\t{}
        Advance Payment :\t{}'''.format(
          record[0], record[1], record[2], record[3], record[4]))
      conn.close()
      greet()
      wait = input('\n\n\nPress Enter to continue......')
      break

# 14. Function to search bills
def search_bills():
  while True:
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    bill_no = input('Enter Bill No :')
    sql = ' select bills.bill_id, bills.amount, bill_date, gst, st, b.book_id, DateOfBooking,\
       DateOfleaving, advance, b.CustomerName, address, Contact_No, email, bills.roomno, r.room_type,\
        r.bed_type, r.rent, c.customerid, id_proof, id_number \
         from bills, bookings b, customers c , rooms r \
           where bills.book_id = b.book_id \
             and b.roomno = r.roomno and b.customerid = c.customerid AND NOT DateOfLeaving is NULL AND \
               bill_id = '+bill_no +';'
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print('Bill information for Bill No :{}'.format(bill_no))
    print('*'*140)
    # checking record
    if record == None:
      print("NOTE :There is no record for Bill No. ", bill_no, "in our database.")
      wait = input('\n\n\nPress Enter to continue......')
      greet()
      break
    else :
      pass
    print('Bill Number             : ', record[0])
    print('Bill\'s Total Amount     : ', 'Rs.',record[1])
    print('Bill Date               : ', record[2])
    print('GST Charged             : ', 'Rs.',record[3])
    print('Service Tax Charged     : ', 'Rs.',record[4])
    print('Booking ID              : ', record[5])
    print('Room no. Used           : ', record[13])
    print('Room Name or type       : ', record[14])
    print('Room Bedding            : ', record[15])
    print('Room Rent(per night)    : ', 'Rs.',record[16])
    print('Date of Occupancy       : ', record[6])
    print('Date of Leaving         : ', record[7])
    print('Advance Paid            : ', 'Rs.',record[8])
    print('Customer\'s ID           : ', record[17])
    print('Customer\'s Name         : ', record[9])
    print('Customer\'s Address      : ', record[10])
    print('Customer\'s Phone        : ', record[11])
    print('Customer\'s Email ID     : ', record[12])
    print('Customer\'s ID Proof     : ', record[18])
    print('Customer\'s ID Proof No. : ', record[19])
    conn.close()
    wait = input('\n\n\nPress Enter to continue......')
    break
    
# 15. Function to select what you want to search
def search_menu(): 
    while True:
      clear()
      print(' Search Menu')
      print('-'*75)
      print("\n1.Room Status")
      print('\n2.Booking Status')
      print('\n3.Customer Details')
      print('\n4.Bills')
      print('\n5.Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        search_rooms()
      if choice == 2:
        search_booking()
      if choice == 3:
        search_customer()
      if choice == 4:
        search_bills()
      if choice == 5:
        greet()
        break

# 16. Function to take report of room 
def report_room_status(): 
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    sql = 'select * from rooms'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Rooms Status - Report')
    print('-'*75)
    print('{:15s} {:18s} {:15s} {:15s} {:20s} {:10s}'.format('Room No', 'Room Type', 'Rent','Bedding', 'Room Status', 'Booked for CustomerID'))
    for no,rtype,rent,bed,status,customerid in records:
      print('{:<10d} {:21s} {:<7.2f} {:>18s} {:>12s} {:>20s}'.format(no, rtype, rent, bed, status, str(customerid)))
    conn.close()
    greet()
    wait = input('\n\n\n Press Enter to continue....')

# 17. Function to take report of booking status
def report_booking_status(): 
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    sql = ''' SELECT b.book_id,b.roomno,DateOfBooking,DateOfLeaving,advance, b.Customername,address,Contact_No
    FROM bookings b, customers c 
    WHERE b.customerid = c.customerid;
    '''
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(' Booking Status - Report')
    print('-'*75)
    print('{:9s} {:15s} {:18s} {:10s} {:15s} {:20s} {:15s} {:15s}'.format(
        'BookID', 'RoomNo', 'DOO', 'DOL', 'Advance', 'CustomerName','Address','Phone'))
    for BookID, Rno, doo, dol, advance, Cname, addr, phone in records:
        print('{} {:>10d} {:>20s} {:>12s} {:>14.2f} {:>20s} {:>14s} {:>18d}'.format(
            BookID, Rno, str(doo), str(dol), advance, Cname, addr, phone))
    conn.close()
    greet()
    wait = input('\n\n\n Press Enter to continue....')

# 18. Function for report menu of report functions
def report_menu():
    while True:
      clear()
      print('Report Menu')
      print('*'*35)
      print("\n1.Room Status")
      print('\n2.Booking Status')
      print('\n3.Bill Collections')
      print('\n4.Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        report_room_status()
      if choice == 2:
        report_booking_status()
      if choice == 3:
        reportCollection()      
      if choice == 4:
        break

# 19. Function for Collections
def reportCollection(): 
    conn = mysql.connector.connect(
        host='localhost', database = 'The_Taj_Hotel', 
        user='root', password='SAGAR YADAV')
    cursor = conn.cursor()
    clear()
    print("Bill Collections ------ Menu")
    print('*'*45)
    print("1.Total Bill Collection")
    print("2.Collection from individual customer")
    print("3.Back to Report menu")
    choice = int(input("\nEnter your choice from above (1 or 2) :> "))
   # FOR TOTAL COLLECTION
    if choice == 1:
      print("\nTotal Collection")
      print('-'*35)
      sql = "SELECT sum(Amount) from bills;"
      cursor.execute(sql)
      data = cursor.fetchone()
      print("Total Collections we have, Rs.", data[0])
      wait = input('\n\n\n Press Enter to continue....')
   # FOR INDIVIDUAL CUSTOMER
    if choice == 2:
      print("\nCollection from individual customer")
      print('-'*35)
      custNo = input("Enter Customer No. :> ")
      sql1 = "SELECT DateofLeaving, advance \
        FROM bookings WHere customerID = {};".format(custNo)
      cursor.execute(sql1)
      records = cursor.fetchall()
      count = cursor.rowcount
      print("Rows :", count)
      for record in records:
         dateofleaving = record[0]
         advance = record[1]
         if count == 1 and dateofleaving == None:
            collection = advance
            print("Collection from Customer No.", custNo, ":> Rs. ",collection)
         elif count == 1 and dateofleaving != None :
            sql2 = "SELECT amount\
               From bills bl, bookings bk\
                  WHERE bl.book_id = bk.book_id and customerid ={};".format(custNo)
            cursor.execute(sql2)
            data = cursor.fetchone()
            print("Collections from CustomerNo.", custNo, "we have, Rs.", data[0])
         elif count > 1 and dateofleaving == None:
            sql3 = "SELECT bk.book_id, amount\
               From bookings bk, bills bl\
                  Where bk.book_id = bl.book_id and customerid = {};".format(custNo)
            cursor.execute(sql3)
            records = cursor.fetchall()
            for record in records:
               bill = record[1]               
               collection = bill + advance               
            print("Collection from Customer No.", custNo, ":> Rs. ",collection)   
         elif count > 1 and dateofleaving != None:
            bill = 0
            sql3 = "SELECT bk.book_id, amount\
               From bookings bk, bills bl\
                  Where bk.book_id = bl.book_id and customerid = {};".format(custNo)
            cursor.execute(sql3)
            records = cursor.fetchall()
            for record in records:
               bill += record[1]                             
               collection = bill               
            print("Collection from Customer No.", custNo, ":> Rs. ",collection)
         break                          
      if count == 0 :
         print("No record found for Customer No.", custNo)
      if choice == 3:
        report_menu()
      greet()
      wait = input('\n\n\n Press Enter to continue....')
      
# 20. Function for Main Screen
def main_menu():
    while True:
      clear()
      print(' H O T E L   M A N A G E M E N T   S Y S T E M ')
      print('-'*75)
      print("\n1.   Add New Room")
      print('\n2.   Add Customer')
      print('\n3.   Modify Room Information')
      print('\n4.   Modify Customer Information')
      print('\n5.   Room Booking')
      print('\n6.   Bill Generation')
      print('\n7.   Search Database')
      print('\n8.   Report Menu')
      print('\n9.   Hotel Details')
      print('\n10.  Change Hotel Details')
      print('\n11.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:   # Add New Room
        add_room()
      if choice == 2:   # Add Customer
        add_customer()
      if choice == 3:   # Modify Room Information
        modify_room()
      if choice == 4:   # Modify Customer Information
        modify_customer()
      if choice == 5:   # Room Booking
        room_booking()
      if choice == 6:   # Bill Generation
        bill_generation()
      if choice == 7:   # Search Database
        search_menu()
      if choice == 8:   # Report Menu
        report_menu()
      if choice == 9:   # Hotel Details
        hotelDetails()
      if choice ==10:   # Change Hotel Details
        change_hotelDetails()
      if choice ==11:
        greet()
        break
      
# 21. Function to clear the screen
def clear(): 
  for _ in range(30):
    print()

# 22. Function to greet
greet = lambda : print("\n\t\tThanks for using....\n\t\tCreated by : SAGAR YADAV")

#         __main__
if __name__ == "__main__":
    hotelDetails()
    main_menu()

# END OF PROGRAM
# THANKS FOR USING
# CREATED BY : SAGAR YADAV