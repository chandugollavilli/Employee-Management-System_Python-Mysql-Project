############################ DATABASE ###########################

# import mysql.connector
# emp_project = mysql.connector.connect(

#     host = "localhost",
#     user = "root",
#     password = "Chandu@123",
#     database = "emp_project"

# )

# print(emp_project) 

# emp_data = emp_project.cursor()
# emp_data.execute("CREATE TABLE OFFICE_TABLE (EMP_CODE VARCHAR(50), EMP_NAME VARCHAR(50), EMP_POST VARCHAR(50), EMP_JOINING VARCHAR(50), EMP_BASICPAY INT)")
# emp_data.execute("CREATE TABLE PERSONAL_TABLE (NAME VARCHAR(50), CITY VARCHAR(50), BIRTHDAY VARCHAR(50), PHONE_NO VARCHAR(50))")
# emp_data.execute("CREATE TABLE SALARY_TABLE (EMP_CODE VARCHAR(50), EMP_NAME VARCHAR(50), YEAR VARCHAR(50), MONTH VARCHAR(50), EMP_WORKING_DAYS INT, FINALPAY INT)")


############ Another way to connect database #################

# import mysql.connector as emp_project
# connect = emp_project.connect(
#     host = "localhost", 
#     user = "root", 
#     password = "Chandu@123", 
#     database = "emp_project"

# ) 

# # print(connect)

# sql = """CREATE TABLE OFFICE_TABLE
# (EMP_CODE VARCHAR(50), 
# EMP_NAME VARCHAR(50), 
# EMP_POST VARCHAR(50), 
# EMP_JOINING VARCHAR(50), 
# EMP_BASICPAY INT)"""

# sql = """CREATE TABLE PERSONAL_TABLE 
# (NAME VARCHAR(50), 
# CITY VARCHAR(50), 
# BIRTHDAY VARCHAR(50), 
# PHONE_NO VARCHAR(50))"""

# sql = """CREATE TABLE SALARY_TABLE 
# (EMP_CODE VARCHAR(50), 
# EMP_NAME VARCHAR(50), 
# YEAR VARCHAR(50), 
# MONTH VARCHAR(50), 
# EMP_WORKING_DAYS INT, 
# FINALPAY INT)"""

# emp_data = connect.cursor()
# emp_data.execute(sql)



############## Programming part #############

import mysql.connector as emp_project
connect = emp_project.connect(
    host = "localhost",
    user = "root",
    password = "Chandu@123",
    database = "emp_project"
)

####################################inserting#######################################
def npersonal():
    n = input("Enter Employee Name: ")
    c = input("Enter Employee City Name: ")
    d = input("Enter Employee Date of Birth: ")
    p = input("Enter Employee Phone no: ")
    data = (n,c,d,p)
    sql = "insert into personal_table values(%s,%s,%s,%s)"
    emp_data = connect.cursor()
    emp_data.execute(sql,data)
    connect.commit()
    print("\nData Entered Successfully")
    main()

def personal():
    sql = "SELECT * FROM personal_table"
    emp_data = connect.cursor()
    emp_data.execute(sql)
    data = emp_data.fetchall()
    for i in data:
        print(i)
    main()

def noffice():
    ec = input("Enter Employee Code: ")
    n = input("Enter Employee Name: ")
    ps = input("Enter Employee Post: ")
    j = input("Enter Employee joining date: ")
    bp = int(input("Enter Assigned Salary: "))
    data = (ec,n,ps,j,bp)
    sql = "INSERT INTO office_table values(%s,%s,%s,%s,%s)"
    emp_data = connect.cursor()
    emp_data.execute(sql,data)
    connect.commit()
    print("\nData Entered Successfully")
    main()

def office():
    sql = "SELECT * FROM office_table"
    emp_data = connect.cursor()
    emp_data.execute(sql)
    data = emp_data.fetchall()
    for i in data:
        print(i)
    main()

def nsalary():
    ec = input("\nEnter Employee Code: ")
    v = (ec,)
    sql = "SELECT EMP_BASICPAY from office_table where EMP_CODE = %s"
    emp_data = connect.cursor()
    emp_data.execute(sql,v)
    bs = emp_data.fetchone()
    n = input("Enter Employee Name: ")
    y = input("Enter Year: ")
    m = input("Enter Month: ")
    wd = int(input("Enter Working Days: "))
    td = int(input("Enter Total Days: "))
    fp = bs[0]/td*wd
    data = (ec,n,y,m,wd,fp)
    sql = "INSERT INTO salary_table values(%s,%s,%s,%s,%s,%s)"
    emp_data = connect.cursor()
    emp_data.execute(sql,data)
    connect.commit()
    print("\nData Entered Sucessfully")
    main()

def salary():
    sql = "SELECT * FROM salary_table"
    emp_data = connect.cursor()
    emp_data.execute(sql)
    data = emp_data.fetchall()
    for i in data:
        print(i)
    main()

def finalpay():
    ec = input("Enter Employee Code: ")
    v=(ec,)
    sql = "SELECT FINALPAY FROM salary_table WHERE EMP_CODE = %s"
    emp_data = connect.cursor()
    emp_data.execute(sql,v)
    data = emp_data.fetchone()
    for i in data:
        print('\nFinal pay:',i)
    main()


##########################Delete###################################

def remove():
    print('\npersonal\noffice\nsalary')
    choice = input("\nEnter details to remove: ")
    while True:
        if(choice=='office'):
            office_data()
        elif(choice=='personal'):
            personal_data()
        elif(choice=='salary'):
            return salary_data()
        else:
            print("\nWrong emp_data selected..................................")
        return main()

def office_data():
    ec = input("\nEnter Employee Code: ")
    v = (ec,)
    sql = "delete from office_table where EMP_CODE = %s"
    emp_data = connect.cursor()
    emp_data.execute(sql,v)
    connect.commit()
    print("\nDelete emp data from Office sucessfully")
    main()

def personal_data():
    ec = input("\nEnter Employee name: ")
    v = (ec,)
    sql = "delete from personal_table where NAME = %s"
    emp_data = connect.cursor()
    emp_data.execute(sql,v)
    connect.commit()
    print("\nDelete emp data from Personal sucessfully")
    main()

def salary_data():
    ec = input("\nEnter Employee Code: ")
    v = (ec,)
    sql = "delete from salary_table where EMP_CODE = %s"
    emp_data = connect.cursor()
    emp_data.execute(sql,v)
    connect.commit()
    print("\nDelete emp data from salary sucessfully")
    main()

################################update#####################################

def update():
    print('\npersonal\noffice\nsalary')
    choice = input("\nEnter details to update: ")
    while True:
        if(choice=='office'):
            office_update()
        elif(choice=='personal'):
            personal_update()
        elif(choice=='salary'):
            return salary_update()
        else:
            print("\nWrong emp_data selected..................................")
        return main()

def office_update():
    en = input("Enter your name: ")
    ep = input("Enter your post: ")
    ej = input("Enter joining date: ")
    eb = int(input("Enter basicpay: "))
    ec = input("Enter Employee Code: ")
    v = (en,ep,ej,eb,ec,)
    sql = "UPDATE office_table SET EMP_NAME = %s, EMP_POST = %s, EMP_JOINING = %s, EMP_BASICPAY = %s where EMP_CODE = %s"
    emp_data = connect.cursor()
    emp_data.execute(sql,v)
    connect.commit()
    print("\nupdate emp_data from office sucessfully")
    main()

def personal_update():
    ec = input("Enter your city: ")
    eb = input("Enter birthday: ")
    ep = input("Enter phone no: ")
    en = input("Enter your name: ")
    v = (ec,eb,ep,en)
    sql = "UPDATE personal_table SET CITY = %s, BIRTHDAY = %s, PHONE_NO = %s where NAME = %s"
    emp_data = connect.cursor()
    emp_data.execute(sql,v)
    connect.commit()
    print("\nupdate emp_data from personal sucessfully")
    main()

def salary_update():
    en = input("Enter your name: ")
    y = input("Enter your year: ")
    m = input("Enter joining month: ")
    ewd = int(input("Enter your working days: "))
    fp = int(input("Enter you finalpay: "))
    ec = input("Enter Employee Code: ")
    v = (en,y,m,ewd,fp,ec)
    sql = "UPDATE salary_table SET EMP_NAME = %s, YEAR = %s, MONTH = %s, EMP_WORKING_DAYS = %s, FINALPAY = %s where EMP_CODE = %s"
    emp_data = connect.cursor()
    emp_data.execute(sql,v)
    connect.commit()
    print("\nupdate emp_data from salary sucessfully")
    main()


##################################Task####################################

def main():
    print("""
    1. ADD NEW EMPLOYEE PERSONAL DETAILS
    2. DISPLAY EMPLOYEES PERSONAL DETAILS
    3. ADD NEW EMPLOYEE OFFICE DETAILS
    4. DISPLAY EMPLOYEES OFFICE DETAILS
    5. ENTER SALARY DETAILS OF EMPLOYEE
    6. DISPLAY SALARY DETAILS OF EMPLOYEE
    7. DELETE EMPLOYEES DETAILS
    8. UPDATE DETAILS
    9. FINALPAY""")
    choice = input("\nEnter Task No: ")
    while True:
        if(choice=='1'):
            npersonal()
        elif(choice=='2'):
            personal()
        elif(choice=='3'):
            noffice()
        elif(choice=='4'):
            office()
        elif(choice=='5'):
            nsalary()
        elif(choice=='6'):
            salary()
        elif(choice=='7'):
            remove()
        elif(choice=='8'):
            update()
        elif(choice=='9'):
            finalpay()
        else:
            print("\nWrong choice..................................")
        return main()
main()



