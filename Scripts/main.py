import streamlit as st
import pandas as pd
import mysql.connector
st.title("EMPLOYEE MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("My Menu",("Home","Employee","Admin"))
#st.write(choice)
if (choice=="Home"):
     st.image("https://st2.depositphotos.com/1757635/8830/i/450/depositphotos_88302772-stock-photo-global-business-strategy.jpg")
     st.write("This is a web Application developed by PILLI GOWTHAM")
elif(choice=="Employee"):
    #btn2=st.button("Temporary")
    if 'login' not in st.session_state:
        st.session_state['login']=False
    #login=False
    uid=st.text_input("Enter Employee ID")
    upwd=st.text_input("Enter Employee Name")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
        c=mydb.cursor()
        c.execute("select * from Employees")
        for r in c:
            if(r[0]==uid and r[1]==upwd):
                st.session_state['login']=True
                break
        if(not st.session_state['login']):
             st.write("Incorrct ID or Password")
    if(st.session_state['login']):
        st.write("Login Successfull")
        choice2=st.selectbox("Features",("None","View all employees","Attendance of employees","Leaves of employees"))
        if (choice2=="View all employees"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS")
            df=pd.read_sql("select * from Employees",mydb)
            st.dataframe(df)
        elif(choice2=="Attendance of employees"):
             eid=st.text_input("Enter your Employee ID")
             btn2=st.button("Mark Attendance")
             if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS") 
                stat_present=pd.read_sql(f"select present from Attendance WHERE employee_id='{eid}'",mydb)
                present_value = stat_present['present'].iloc[0]  # Extract the first value
                total_present = int(present_value) + 1
                
                #total_present=int(stat_present)+1
                #st.write(total_present)

                c=mydb.cursor()
                c.execute("UPDATE Attendance SET present = %s WHERE employee_id = %s", (total_present, eid))
                mydb.commit() 
                df2=pd.read_sql(f"select * from Attendance WHERE employee_id='{eid}'",mydb)
                st.dataframe(df2)
                
        elif(choice2=="Leaves of employees"):
             eid=st.text_input("Enter your Employee ID")
             btn2=st.button("Mark Leave")
             if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="EMS") 
                stat_absent=pd.read_sql(f"select absent from Attendance WHERE employee_id='{eid}'",mydb)
                absent_value = stat_absent['absent'].iloc[0]  # Extract the first value
                total_absent = int(absent_value) + 1
                
                #total_present=int(stat_present)+1
                #st.write(total_present)

                c=mydb.cursor()
                c.execute("UPDATE Attendance SET absent = %s WHERE employee_id = %s", (total_absent, eid))
                mydb.commit() 
                df3=pd.read_sql(f"select * from Attendance WHERE employee_id='{eid}'",mydb)
                st.dataframe(df3)                

                
#elif(choice=="Admin"):
 #    st.video("https://youtu.be/MhRhFUzKVBk?si=_PuTckrR6Z5jfnmv")
