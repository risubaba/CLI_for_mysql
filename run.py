import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date
from datetime import datetime
from tabulate import tabulate

# implement age using bdate

options = {
    "0" : "customer",
    "1" : "dependent",
    "2" : "employee",
    "3" : "games",
    "4" : "messages",
    "5" : "phone_num_cus",
    "6" : "phone_num_esp",
    "7" : "product",
    "8" : "sells",
    "9" : "store",
    "10" : "vehicle"
}

def calculate_age(born): 
    # born.replace('-',',') 
    born = born.split("-") 
    born = [ int(i) for i in born ] 
    born = date(born[0],born[1],born[2]) 
    today = date.today() 
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day)) 

def check(row,checkset):
    ind = -1
    for i in row:
        ind +=1
        if checkset[ind] == 0 :
            continue
        if row[i] != '':
            pass
        else:
            return 0
    return 1

def addCustomer():
    try:
        row = {}
        print("Enter new customer's details: ")
        row['name'] = (input("Name (Fname Lname): "))
        row["customer_id"] = int(input("Customer id: "))
        row["email_address"] = input("Email Address: ")
        row["Addressline1"] = input("Address Line1: ")
        row["Addressline2"] = input("Address Line2: ")
        row["employee_id"] = int(input("Employee id: "))
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row['age'] = calculate_age(row['Bdate'])
        row['phone_num'] = input("Phone number(s) in comma separated format: ")
        phonenums=row['phone_num'].split(",")
        row['vehicle_license_plate'] = input(
            "Enter vehicle license plate if you wish to enter vehicle information, leave blank otherwise: ")
        if row['vehicle_license_plate']:
            row['vehicle_model'] = input("Vehicle model:")
        checkset = [1,1,0,1,0,1,1,1,1,0,1]
        if check(row,checkset)==0:
            print("Invalid values")
            return
        query = """INSERT INTO customer(customer_id,name,email_address,address_line1,address_line2,age,date_of_birth,employee_id)
        VALUES('%s', '%s', '%s', '%s', '%s', %d , '%s', '%s')""" % (row["customer_id"], row["name"], row["email_address"], row["Addressline1"], row["Addressline2"], row["age"], row["Bdate"], row["employee_id"])
        cur.execute(query)
        con.commit()

        for i in phonenums:
            query = """INSERT INTO phone_num_cus(customer_id,phone_num) VALUES(%d, '%s')""" % (
                row["customer_id"], int(i))
            cur.execute(query)
            con.commit()


        if row['vehicle_license_plate']:
            query = """INSERT INTO vehicle(customer_id,vehicle_license_plate,vehicle_model) VALUES(%d, '%s', '%s')""" % (
                row["customer_id"], row["vehicle_license_plate"], row["vehicle_model"])
            cur.execute(query)
            con.commit()

        print("Entered into database")
        return

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def addEmployee():
    try:
        row = {}
        print("Enter new employee's details: ")
        row['name'] = (input("Name (Fname Lname): "))
        row["employee_id"] = int(input("employee id: "))
        row["email_address"] = input("Email Address: ")
        row['salary'] = int(input("salary: "))
        row["Addressline1"] = input("Address Line1: ")
        row["Addressline2"] = input("Address Line2: ")
        row['phone_num'] = input("Phone number(s) in comma separated format: ")
        phonenums=row['phone_num'].split(",")
        checkset = [1,1,1,1,1,0,1]
        if check(row,checkset)==0:
            print("Invalid values")
            return
        query = """INSERT INTO employee(employee_id,name,email_address,salary,address_line1,address_line2)
        VALUES(%d, '%s', '%s', %d, '%s', '%s')""" % (row["employee_id"], row["name"], row["email_address"], row["salary"], row["Addressline1"], row["Addressline2"])
        cur.execute(query)
        con.commit()

        for i in phonenums:
            query = """INSERT INTO phone_num_emp(employee_id,phone_num) VALUES(%d, '%s')""" % (
                row["employee_id"], int(i))
            cur.execute(query)
            con.commit()

        print("Entered into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addProduct():
    try:
        row = {}
        print("Enter new product's details: ")
        row['product_name'] = (input("Product name: "))
        row["product_id"] = int(input("product id: "))
        row["num_in_stock"] = int(input("Number of products in stock: "))
        row["price"] = int(input("Price: "))
        row["store_id"] = int(input("Store ID: "))
        row["genre"] = input(
            "If product is a game, enter genre. leave blank otherwise: ")
        if row["genre"]:
            row["developer"] = input("Game developer: ")
            row["platform"] = input("Game platform: ")
            row["release_date"] = input("Game release date: (YYYY-MM-DD) ")
            row["ESRB_rating"] = input("Game ESRB rating: ")

        checkset=[1,1,0,1,1,0]
        if row["genre"]:
            checkset=[1,1,0,1,1,1,1,1,1,1]
        if check(row,checkset)==0:
            print("Invalid values")
            return
        query = """INSERT INTO product(product_id,product_name,num_in_stock, price, store_id)
        VALUES(%d, '%s', %d, %d, %d)""" % (row["product_id"], row["product_name"], row["num_in_stock"], row["price"], row["store_id"])
        cur.execute(query)
        con.commit()

        if row["genre"]:
            query = """INSERT INTO games(product_id, developer, genre, platform, release_date, esrb_rating)
            VALUES(%d, '%s', '%s', '%s', '%s', '%s')""" % (row["product_id"], row["developer"], row["genre"], row["platform"], row["release_date"], row["ESRB_rating"])
            cur.execute(query)
            con.commit()
        print("Entered into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addDependent():
    try:
        row = {}
        print("Enter new dependent's details: ")
        row['name'] = (input("Name (Fname Lname): "))
        row["employee_id"] = int(input("employee id: "))
        row["relationship_type"] = input("Relationship type: ")
        checkset = [1,1,1]  
        if check(row,checkset)==0:
            print("Invalid values")
            return      
        query = """INSERT INTO dependent(employee_id,name,relationship_type)
        VALUES(%d, '%s', '%s')""" % (row["employee_id"], row["name"], row["relationship_type"])
        cur.execute(query)
        con.commit()
        print("Entered into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addSells():
    try:
        row = {}
        print("Enter new product's details: ")
        row["employee_id"] = int(input("employee id: "))
        row["customer_id"] = int(input("customer id: "))
        row["store_id"] = int(input("store id: "))
        row["product_id"] = int(input("product id: "))
        row["total_price"] = int(input("Total price: "))
        checkset = [1,1,1,1,1]
        if check(row,checkset)==0:
            print("Invalid values")
            return
        stock="""SELECT num_in_stock from product where product_id=(%d)""" %(row["product_id"])
        print(stock )
        query = """INSERT INTO sells(employee_id,customer_id,store_id, product_id, total_price)
        VALUES(%d, %d, %d, %d, %d)""" % (row["employee_id"], row["customer_id"], row["store_id"], row["product_id"], row["total_price"])
        cur.execute(query)
        con.commit()
        print("Entered into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addStore():
    try:
        row = {}
        print("Enter new store's details: ")
        row['name'] = (input("Store name: "))
        row["store_id"] = int(input("Store id: "))
        row["email_address"] = input("Email Address: ")
        row["website_address"] = input("Website Address: ")
        row["customer_service_website_address"] = input(
            "Customer service website address: ")
        row["location"] = input("Location: ")
        checkset = [1,1,1,0,0,1]
        if check(row,checkset)==0:
            print("Invalid values")
            return
        query = """INSERT INTO store(store_id, name, email_address, website_address, customer_service_website_address, location)
        VALUES(%d, '%s', '%s', '%s', '%s', '%s')""" % (row["store_id"], row["name"], row["email_address"], row["website_address"], row["customer_service_website_address"], row["location"])
        cur.execute(query)
        con.commit()
        print("Entered into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def addMessage():
    try:
        row = {}
        print("Enter message details: ")
        row['e1'] = (input("Employee ID 1 (from): "))
        row['e2'] = (input("Employee ID 2 (to): "))
        row["message"] = input("Message: ")
        checkset = [1,1,1]
        if check(row,checkset)==0:
            print("Invalid values")
            return
        query = """INSERT INTO messages(e_id1, e_id2, timestamp, message)
        VALUES('%s', '%s', '%s', '%s')""" % (row["e1"], row["e2"], datetime.now(), row["message"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Entered into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

def addRecord():
    print("1. Add to table customer")
    print("2. Add to table dependent")
    print("3. Add to table employee")
    print("4. Add to table product")
    print("5. Add to table sells")
    print("6. Add to table store")
    print("7. Add to table messages")
    ch = int(input("Choose option: "))
    if ch == 1: addCustomer()
    if ch == 2: addDependent()
    if ch == 3: addEmployee()
    if ch == 4: addProduct()
    if ch == 5: addSells()
    if ch == 6: addStore()
    if ch == 7: addMessage()
    else:
        return

def delete():
    try:
        cur.execute('show tables;')
        tables = cur.fetchall()
        for i in range(len(tables)):
            print("{}. {}".format(i, tables[i]['Tables_in_Franchise']))
        table = input("Choose the required table: ")
        table = options[table]
        display(table)
        cur.execute('show keys from {} where Key_name = "PRIMARY"'.format(table))
        keys = []
        for row in cur.fetchall():
            keys.append(row['Column_name'])
        vals = input("Enter the values of the following keys (comma separated) for the row to be deleted ( " + ", ".join(keys) + "): ")
        if(len(keys) != len(vals.split(','))):
            print("Incorrect number of values")
            return
        for i in range(len(keys)):
            keys[i] = keys[i] + " = '" + vals.split(',')[i].strip() + "'"
        cur.execute("select * from {}".format(table))
        count = len(cur.fetchall())
        query = ("DELETE FROM {} WHERE ".format(table) + " and ".join(keys) + ";")
        # print(query)
        cur.execute(query)
        con.commit()
        count2 = cur.execute("select * from {}".format(table))        
        count2 = len(cur.fetchall())        
        if count == count2: 
            print("Error: No such row exists!")
        else:
                print("Successfully Deleted!")
    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)


def update():
    try:
        cur.execute('show tables;')
        tables = cur.fetchall()
        for i in range(len(tables)):
            print("{}. {}".format(i, tables[i]['Tables_in_Franchise']))
        table = input("Choose the required table: ")
        table = options[table]
        display(table)
        cur.execute('show keys from {} where Key_name = "PRIMARY"'.format(table))
        keys = []
        for row in cur.fetchall():
            keys.append(row['Column_name'])
        vals = input("Enter the values of the following keys (comma separated) for the row to be updated (" + ", ".join(keys) + "): ")
        if(len(keys) != len(vals.split(','))) or vals == '':
            print("Incorrect number of values")
            return
        for i in range(len(keys)):
            keys[i] = keys[i] + " = '" + vals.split(',')[i].strip() + "'"
        cur.execute("SELECT * FROM {} WHERE ".format(table) + " and ".join(keys)+";")
        if len(cur.fetchall()) == 0 :
            print("Required record does not exist")
            return
        column = input("Enter the field you want to update (Only one field at a time): ")
        if column == '':
            print("Please enter field name")
            return
        new_val = input("Enter the new value : ")
        query = "UPDATE {} SET {} = '{}' WHERE ".format(table, column, new_val) + " and ".join(keys) + ";"
        cur.execute(query)
        con.commit()
        print("Successfully Updated!")
    except Exception as e:
        con.rollbacl()
        print("Failed to update in the database")
        print(">>>>>>>>>>>>>>", e)

def show():
    cur.execute('show tables;')
    tables = cur.fetchall()
    for i in range(len(tables)):
        print("{}. {}".format(i, tables[i]['Tables_in_Franchise']))
    table = input("Choose the required table: ")
    display(table)

def display(table):
    try:
        table=options[table]
    except Exception as e:
        pass
    query = ("select * from {};".format(table))
    cur.execute(query)
    data = cur.fetchall()
    print(tabulate(data, tablefmt = 'grid', headers = 'keys'))

def dispatch(ch):
    if ch == 1: addRecord()
    if ch == 2: delete()
    if ch == 3: update()
    if ch == 4: show()

while(1):
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='Franchise',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Add record")
                print("2. Delete a record")
                print("3. Update a record")
                print("4. Display records")
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")
    except:
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

