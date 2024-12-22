create database EMS;
use EMS;

create table Employees(employee_id varchar(255),employee_name varchar(255),employee_department_id varchar(255),employee_department_name varchar(255),employee_address varchar(255),employee_contact varchar(255),primary key(employee_id));
#drop table Employees;
insert into Employees values("E001","Gowtham","D001","R&D","5th Street","905283475");
insert into Employees values("E002","Kiran","D002","Testing","6th Street","905433475");
insert into Employees values("E003","Rahul","D003","Management","7th Street","955433475");
select * from Employees;

update Employees set employee_address="7th Street" where employee_id="E003";

#delete from Employees where employee_id="0001";

create table Departments(department_id varchar(255),department_name varchar(255),primary key(department_id));
#drop table Departments;
insert into Departments values("D001","R&D");
insert into Departments values("D002","Testing");
insert into Departments values("D003","Management");
select * from Departments;

create table Attendance(employee_id varchar(255),employee_name varchar(255),department_id varchar(255),primary key(employee_id));
#drop table Attendance;
insert into Attendance values("E001","Gowtham","D001");
insert into Attendance values("E002","Kiran","D002");
insert into Attendance values("E003","Rahul","D003");
select * from Attendance;

create table Leaves(employee_id varchar(255),employee_name varchar(255),department_id varchar(255),leaves_used varchar(255),leaves_balance varchar(255),primary key(employee_id));
#drop table Leaves;
insert into Leaves values("E001","Gowtham","D001","3","5");
insert into Leaves values("E002","Kiran","D002","6","2");
insert into Leaves values("E003","Rahul","D003","4","3");
select * from Leaves;