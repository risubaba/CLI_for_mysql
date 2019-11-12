import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date

# implement age using bdate


def calculate_age(born):
    born = date(born)
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def fireAnEmployee():
    """
    Function to fire an employee
    """
    print("Not implemented")


def promoteEmployee():
    """
    Function performs one of three jobs
    1. Increases salary
    2. Makes employee a supervisor
    3. Makes employee a manager
    """
    print("Not implemented")


def employeeStatistics():
    """
    Function prints a report containing
    the number of hours per week the employee works,
    hourly pay, projects employee works on and so on
    """
    print("Not implemented")


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
        row['age'] = 10
        row['phone_num'] = input("Phone number: ")
        row['vehicle_license_plate'] = input(
            "Enter vehicle license plate if you wish to enter vehicle information, leave blank otherwise: ")
        if row['vehicle_license_plate']:
            row['vehicle_model'] = input("Vehicle model")

        query = """INSERT INTO customer(customer_id,name,email_address,address_line1,address_line2,age,date_of_birth,employee_id)
        VALUES(%d, '%s', '%s', '%s', '%s', %d , '%s', %d)""" % (row["customer_id"], row["name"], row["email_address"], row["Addressline1"], row["Addressline2"], row["age"], row["Bdate"], row["employee_id"])
        cur.execute(query)
        con.commit()

        query = """INSERT INTO phone_num_cus(customer_id,phone_num) VALUES(%d, '%s')""" % (
            row["customer_id"], row["phone_num"])
        cur.execute(query)
        con.commit()

        if row['vehicle_license_plate']:
            query = """INSERT INTO vehicle(customer_id,vehicle_license_plate,vehicle_model) VALUES(%d, '%s', '%s')""" % (
                row["customer_id"], row["vehicle_license_plate"], row["vehicle_model"])
            cur.execute(query)
            con.commit()

        print("Entered into database")

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
        row['phone_num'] = input("Phone number: ")
        query = """INSERT INTO employee(employee_id,name,email_address,salary,address_line1,address_line2)
        VALUES(%d, '%s', '%s', %d, '%s', '%s')""" % (row["employee_id"], row["name"], row["email_address"], row["salary"], row["Addressline1"], row["Addressline2"])
        cur.execute(query)
        con.commit()
        query = """INSERT INTO phone_num_emp(employee_id,phone_num) VALUES(%d, '%s')""" % (
            row["employee_id"], row["phone_num"])
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


def addProduct():
    try:
        row = {}
        print("Enter new product's details: ")
        row['product_name'] = (input("Product name: "))
        row["product_id"] = int(input("product id: "))
        row["num_in_stock"] = int(input("Number of products in stock: "))
        row["price"] = int(input("Price: "))
        row["store_id"] = int(input("Store ID: "))

        query = """INSERT INTO product(product_id,product_name,num_in_stock, price, store_id)
        VALUES(%d, '%s', %d, %d, %d)""" % (row["product_id"], row["product_name"], row["num_in_stock"], row["price"], row["store_id"])
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

        query = """INSERT INTO store(store_id, name, email_address, website_address, customer_service_website_address, location)
        VALUES(%d, '%s', '%s', '%s', '%s', '%s')""" % (row["store_id"], row["name"], row["email_address"], row["website_address"], row["customer_service_website_address"], row["location"])
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
    ch = int(input("Choose option: "))
    if ch == 1:
        addCustomer()
    if ch == 2:
        addDependent()
    if ch == 3:
        addEmployee()
    if ch == 4:
        addProduct()
    if ch == 5:
        addSells()
    if ch == 6:
        addStore()
    else:
        return


def hireAnEmployee():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new employee's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Minit"] = name[1]
        row["Lname"] = name[2]
        row["Ssn"] = input("SSN: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Address"] = input("Address: ")
        row["Sex"] = input("Sex: ")
        row["Salary"] = float(input("Salary: "))
        row["Dno"] = int(input("Dno: "))

        """
        In addition to taking input, you are required to handle domain errors as well

        For example: the SSN should be only 9 characters long
        Sex should be only M or F

        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied

        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
            row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        addRecord()
    elif(ch == 2):
        fireAnEmployee()
    elif(ch == 3):
        promoteEmployee()
    elif(ch == 4):
        employeeStatistics()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                              user='newuser',
                              password='password',
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
                print("2. Fire an employee")
                print("3. Promote an employee")
                print("4. Employee Statistics")
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
