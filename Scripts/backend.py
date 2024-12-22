import mysql.connector
#import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
print(mydb)
'''
#To Retrive data from database
c=mydb.cursor()
c.execute("select * from employees")
for r in c:
    print(r)


c2=mydb.cursor()
c2.execute("select * from departments")
for r in c2:
    print(r)

c3=mydb.cursor()
c3.execute("select * from attendance")
for r in c3:
    print(r)

c4=mydb.cursor()
c4.execute("select * from leaves")
for r in c4:
    print(r)    

'''

#To insert data from database
employee_id=input("Enter Employee ID")
employee_name=input("Enter Employee Name")
employee_department_id=input("Enter employee_department ID")
employee_department_name=input("Enter USer ID")
employee_address=input("Enter employee_address")
employee_contact=input("Enter employee_contact")

#iid=str(datetime.datetime.now())
c=mydb.cursor()
c.execute("insert into Employees values(%s,%s,%s,%s,%s,%s)",(employee_id,employee_name,employee_department_id,employee_department_name,employee_address,employee_contact))
mydb.commit() 
print("Employee Added Succesessfully")
