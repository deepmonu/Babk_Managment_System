import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='Aman@123',database='BANK_MANAGMENT')
def openAcc():
    n=input("Enter the Name:")
    ac=input("Enter the Account No:")
    db=input("Enter the Date of Birth:")
    add=input("Enter the Address:")
    cn=input("Enter the Contact Number: ")
    ob=input("Enter the opening Balance: ")
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1 = ('insert into account values(%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into amount values(%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()
def depoAmo():
    amount=input("Enter the amount you want to Deposite: ")
    ac = input("Enter the Account No:")
    a = 'select Balance from amount where AccNo=%s'

    data=(ac,)

    x=mydb.cursor()

    x.execute(a,data)

    result=x.fetchone()

    t=int(result[0])+int(amount)
    t=str(t)
    print(result, amount,t)
    sql=('update amount set Balance=%s where AccNo=%s')

    d=(t,ac)

    x.execute(sql,d)
    mydb.commit()
    main()
def withdrawAmo():
    amount = input("Enter the amount you want to WithDraw: ")
    ac = input("Enter the Account No:")
    a = 'select Balance from amount where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = int(result[0]) - int(amount)
    t = str(t)
    sql = ('update amount set Balance=%s where AccNo=%s')
    d = (t, ac)
    x.execute(sql, d)
    mydb.commit()
    main()
def balEnq():
    ac = input("Enter the Account No:")
    a = 'select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance for Account: ",ac,"is",result[-1])
    main()
def dispDetails():
    ac = input("Enter the Account No:")
    a = 'select * from account where AccNo=%s'
    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()
def closeAcc():
    ac = input("Enter the Account No:")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor();
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    main()

def main():
    print('''
            1. OPEN NEW ACCOUNT
            2. DEPOSITE AMOUNT
            3. WITHDRAW AMOUNT
            4. BALANCE ENQUIRY
            5. SHOW CUSTOMER DETAILS
            6. CLOSE AN ACCOUNT''')
    choice = input("Enter the task that you want to implement: ")
    if (choice=='1'):
        openAcc()
    elif(choice=='2'):
        depoAmo()
    elif (choice == '3'):
        withdrawAmo()
    elif (choice == '4'):
        balEnq()
    elif (choice == '5'):
        dispDetails()
    elif (choice == '6'):
        closeAcc()
    else:
        print("Invalid Choice")
        main()
main()

