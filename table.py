import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager',database='bank')
if conn.is_connected():
    print('connected succesfully')
cur=conn.cursor()
cur.execute('create table customer_details(acct_noint)
primary key,acct_namevarchar(25) ,phone_nobigint(25)
check(phone_no>11),address varchar(25),cr_amt
float )')
