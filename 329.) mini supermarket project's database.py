#library import
import mysql.connector as sql
import time
import random as rd

#setting connection
mydb = sql.connect(host = "localhost", user = "root", password = "")

#making cursor
cr = mydb.cursor()

#creating database
q = "create database super_markett"
cr.execute(q)
q = "use super_markett"
cr.execute(q)

#medicine shop
q = '''create table medicine(mid integer primary key,
mname varchar(30) not null,
manufacturer varchar(50),
dateofm date,
dateofexp date not null,
mg float,
content varchar(100),
price float,
qty integer)'''
cr.execute(q)

#bakery
q = '''create table bakery(cid integer primary key,
cake varchar(30) not null,
flavour varchar(50),
dateofm date,
weight float,
content varchar(100),
price float)'''
cr.execute(q)

#stationary
q = '''create table stationary(sid integer primary key,
sname varchar(30) not null,
manufacturer varchar(50),
dateofm date,
stype varchar(20) not null,
price float,
qty integer)'''
cr.execute(q)

#grocery
q = '''create table grocery(Pid integer primary key,
gname varchar(30) not null,
manufacturer varchar(50),
dateofm date,
dateofexp date not null,
gtype varchar(15),
content varchar(100),
price float,
quantity integer)'''
cr.execute(q)

#BILLS
q = '''create table bills(store_name varchar(15) not null,
cname varchar(20),
date_of_pur date,
amount float)'''
cr.execute(q)
mydb.commit()

