import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="your_mysql_password",
  database="grading"
)
mycursor = mydb.cursor()

#Program to modify table

def modtable():
    tr=input('''What you want to modify:
A:Name,
B.Subject,
C.Marks,
D.Grade:''')
    if tr in 'Aa':
        modname()
    elif tr in 'Bb':
        modsub()
    elif tr in 'Cc':
        modmark()
    elif tr in 'Dd':
        modgrade()
    else:
        print('INVALID INPUT')

def modname():
    nm=input('Enter the old name:')
    nnm=input('Enter the new name:')
    sql='UPDATE results SET name=%s WHERE name=%s'
    val=(nnm,nm)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) name changed")

def modsub():
    sn=input('Enter the old subject:')
    nsn=input('Enter the new subject:')
    nm=input('Enter the name:')
    sql='UPDATE results SET subject=%s WHERE subject=%s AND name=%s'
    val=(nsn,sn,nm)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) subject changed")

def modmark():
    mk=int(input('Enter the old marks:'))
    nmk=int(input('Enter the new marks:'))
    nm=input('Enter the name:')
    sql='UPDATE results SET marks=%s WHERE marks=%s AND name=%s'
    val=(nmk,mk,nm)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) marks changed")

def modgrade():
    gd=input('Enter the old grade:')
    ngd=input('Enter the new grade:')
    nm=input('Enter the name:')
    sql='UPDATE results SET grade=%s WHERE grade=%s AND name=%s'
    val=(ngd,gd,nm)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) grade changed")

def insert():
    n=int(input('How many entries do you want to make?'))
    for i in range(n):
        name=input('Enter Name:')
        sub=input('Enter Subject:')
        marks=int(input('Enter Marks:'))
        grade=grading(marks)
        sql="INSERT INTO results (name,subject,marks,grade) VALUES (%s,%s,%s,%s)"
        val=(name,sub,marks,grade)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

def show():
    mycursor.execute("SELECT * FROM results")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def delete():
    nm=input('Enter name of the record to be deleted:')
    sql = "DELETE FROM results WHERE name = %s"
    val = (nm, )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def grading(m):
    if m >= 90:
        a='A1'
    elif m >= 80:
        a='A2'
    elif m >= 70:
        a='B1'
    elif m >= 60:
        a='B2'
    elif m >= 50:
        a='C1'
    else:
        a="F"
    return a

#Main Program

while True:
    if input('ENTER PASSWORD:').lower() == 'your_app_password':
        print('WELCOME TO GRADING APPLICATION!')
        print('''THIS IS HOW THE GRADING IS DONE:
                *THE MARKS HAVE TO BE GIVEN OUT OF HUNDRED
                *IF MARKS ARE EQUAL TO OR ABOVE 90, A1 GRADE IS AWARDED
                *IF MARKS ARE EQUAL TO OR ABOVE 80, A2 GRADE IS AWARDED
                *IF MARKS ARE EQUAL TO OR ABOVE 70, B1 GRADE IS AWARDED
                *IF MARKS ARE EQUAL TO OR ABOVE 60, B2 GRADE IS AWARDED
                *IF MARKS ARE EQUAL TO OR ABOVE 50, C1 GRADE IS AWARDED
                *IF MARKS ARE LESS THAN 50, F GRADE IS AWARDED''')
    else:
        print('SORRY, PASSSWORD IS WRONG. TRY AGAIN!')
        continue

    ask=input('''WHAT DO YOU WANT TO DO?
A.INSERT DATA,
B.SHOW TABLE FROM DATABASE,
C.DELETE DATA FROM DATABASE,
D.MODIFY DATA:''')
    if ask in 'Aa':
        insert()
    elif ask in 'Bb':
        show()
    elif ask in 'Cc':
        delete()
    elif ask in 'Dd':
        modtable()
