import mysql.connector as cnt
import random
from datetime import datetime
import re
from tabulate import tabulate

con = cnt.connect(host="localhost", user="root",password="", database="bank")

def perform(mycur):
    while True:
        print("PRESS 1 TO CREATE A NEW ACCOUNT\nPRESS 2 TO UPDATE YOUR DETAILS\nPRESS 3 TO WITHDRAW\nPRESS 4 TO DEPOSIT\nPRESS 5 TO CHECK BALANCE\nPRESS 6 TO TRACK YOUR TRANSACTIONS\nPRESS 7 TO CLOSE YOUR ACCOUN\nPRESS 8 FOR ADMIN ONLY")
        c = input("--> ")
        if (c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8'):
            break
        else:
            print("INVALID INPUT!!!")
    if (c == '1'):
        newacc(mycur)
    elif (c == '2'):
        update(mycur)
    elif (c == '3'):
        withdrawal(mycur)
    elif (c == '4'):
        deposit(mycur)
    elif (c == '5'):
        balance(mycur)
    elif (c == '6'):
        transaction(mycur)
    elif (c == '7'):
        del_acc(mycur)
    else:
        admin(mycur)


def enter(mycurr, cus, acc, a):
    mycurr.execute(
        "Insert into account(cus_id,acc_no,balance) Values('{}','{}','{}')".format(cus, acc, a))
    con.commit()


def check(x):
    flag = 0
    for i in range(len(x)):
        if (x[i] == '0' or x[i] == '1' or x[i] == '2' or x[i] == '3' or x[i] == '4' or x[i] == '5' or x[i] == '6' or x[i] == '7' or x[i] == '8' or x[i] == '9'):
            flag = 1
            break
    return flag


def dob_check(x):
    flag = 0
    if (len(x) == 10):
        if (check(x) == 1 and ((x[2] == '-' and x[5] == '-') or (x[2] == '/' and x[5] == '/'))):
            flag = 1
    return flag


def name():
    while True:
        n = input("Name(IN BLOCK LETTERS)* : ")
        if (check(n) == 1):
            print("NAME MUST CONTAIN ALPHABETS(A-Z OR a-z)!!!")
        else:
            break
    return n.upper()


def birth():
    while True:
        d = input("Enter your Date of Birth(DD-MM-YYYY)* : ")
        if (dob_check(d) != 1):
            print("INVALID INPUT!!!")
        else:
            break
    return d


def gender():
    while True:
        g = input("Gender:\n1. Male\n2. Female\n--> ")
        if (g == '1' or g == '2'):
            break
        else:
            print("INVALID INPUT!!!")
    if (g == '1'):
        return "MALE"
    else:
        return "FEMALE"


def status():
    while True:
        c = input("Status:\n1. Married\n2. Unmarried\n--> ")
        if (c == '1' or c == '2'):
            break
        else:
            print("INVALID INPUT!!!")
    if (c == '1'):
        return "MARRIED"
    else:
        return "UNMARRIED"


def nation():
    while True:
        k = input("Nationality* : ")
        if (check(k) == 1):
            print("INVALID INPUT!!!")
        else:
            break
    return k.upper()


def pan():
    while True:
        p = input("PAN** : ")
        if (len(p) == 10):
            break
        else:
            print("INVALID INPUT!!!")
    return p


def father():
    while True:
        f = input("Fathers's Name* : ")
        if (check(f) == 1):
            print("INVALID INPUT!!!")
        else:
            break
    return f.upper()


def address():
    a = input("Address(PERMANENT)* : ")
    return a.upper()


def landmark():
    l = input("Landmark* : ")
    return l.upper()


def city():
    b = input("City* : ")
    return b.upper()


def pin():
    while True:
        j = input("Pin code* : ")
        if (check(j) != 1):
            print("INVALID INPUT!!!")
        else:
            break
    return j


def res_type():
    while True:
        x = input(
            "Ressidence type:\n1. Owned\n2. Rented/Leased\n3. Ancestral/Parental\n4. Company Provided\n--> ")
        if (x == '1' or x == '2' or x == '3' or x == '4'):
            break
        else:
            print("INVALID INPUT!!!")
    if (x == '1'):
        return "OWNED"
    elif (x == '2'):
        return "RENTED/LEASEED"
    elif (x == '3'):
        return "ANCESTRAL/PARENTAL"
    else:
        return "COMPANY PROVIDED"


def phn():
    while True:
        v = input("Phone Number* : ")
        if (len(v) == 10):
            if (check(v) == 1):
                break
        else:
            print("INVALID INPUT!!!")
    return v


def email():
    e = input("Email ID : ")
    return e


def occu():
    o = input("Occupation : ")
    return o


def annual():
    while True:
        z = input(
            "Annual Income(ONLY ABSOLUTE AND NUMERIC VALUE TO BE ENTERED)* : ")
        if (check(z) != 1):
            print("ENTER YOUR ANNUAL INCOME IN DIGITS!!!")
        else:
            break
    return int(z)


def newacc(curr):
    i = 1
    while True:
        print(f"**Customer entry {i}**")
        print("-"*30)
        cus_id = str(random.randint(100000000000, 999999999999))
        curr.execute(
            "Select CUS_id from customer")
        d = curr.fetchall()
        for row in d:
            if (cus_id == row[0]):
                cus_id = eval(cus_id)+1
                cus_id = str(cus_id)
            else:
                break
        acc_no = str(random.randint(100000000000, 999999999999))
        curr.execute("Select CUS_id from customer")
        d = curr.fetchall()
        for row in d:
            if (acc_no == row[0]):
                acc_no = eval(acc_no)+1
                acc_no = str(acc_no)
            else:
                break
        n = name()
        date = birth()
        gen = gender()
        m = status()
        k = nation()
        p = pan()
        f = father()
        add = address()
        land = landmark()
        b = city()
        j = pin()
        res = res_type()
        ph = phn()
        e = email()
        o = occu()
        aninc = annual()
        query = "Insert into customer(CUS_id,ACC_no,Name,DOB,Gender,Status,Nationality,PAN,Father,Address,Landmark,City,pin_code,res_type,ph_no,email,occupation,an_inc) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            cus_id, acc_no, n, date, gen, m, k, p, f, add, land, b, j, res, ph, e, o, aninc)
        try:
            curr.execute(query)
            con.commit()
            print("="*30)
            print("ACCOUNT CREATED SUCCESSFULLY...")
            print("Here's your unique customer id and account number:")
            print("Customer ID* : ", cus_id)
            print("Account number* : ", acc_no)
            print("="*30)
        except:
            con.rollback()
            print('Fail to enter the data...')
        print("Minimum amount of 1000 INR must required to be in your account**")
        while True:
            x = input("Enter the amount : ")
            if (check(x) == 1):
                if (int(x) >= 1000):
                    break
                else:
                    print(
                        "MINIMUM AMOUNT OF 1000 INR MUST REQUIRED TO BE IN YOUR ACCOUNT!!!")
            else:
                print("INVALID INPUT!!!")
        enter(curr, cus_id, acc_no, int(x))
        t = input("Want to enter more customers?(Y/N)\n--> ")
        if (t == 'y' or t == 'Y'):
            i = i+1
        elif (t == 'n' or t == 'N'):
            break
        else:
            print("INVALID INPUT!!!")
            break


def update_list():
    l = ["", "Name", "Date of birth", "Gender", "Status", "Nationality", "Fathers' name", "Address", "Landmark",
        "City", "Pincode", "Ressidence type", "Phone number", "Email ID", "Occupation", "Annual Income"]
    for i in range(1, 16, 1):
        print(f"{i}. {l[i]}")


def cus_exist(mycur, c):
    flag = 0
    mycur.execute("Select CUS_id from customer where Cus_id='{}'".format(c))
    d = mycur.fetchall()
    for row in d:
        if (c == row[0]):
            flag = 1
    return flag


def update(curr):
    while True:
        cus_id = input("PLEASE ENTER YOUR CUSTOMER ID : ")
        if (check(cus_id) == 1 and len(cus_id) == 12):
            break
        else:
            print("INVALID INPUT!!!")
    if (cus_exist(curr, cus_id) == 1):
        while True:
            update_list()
            while True:
                c = input("WHAT YOU WANT TO UPDATE? PRESS BUTTON(1-15)\n--> ")
                if (c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or c == "10" or c == "11" or c == "12" or c == "13" or c == "14" or c == "15"):
                    break
                else:
                    print("INVALID INPUT!!!")
            if (c >= "1" and c <= "15"):
                if (c == "1"):
                    n = name()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set Name='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "2"):
                    n = birth()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set DOB='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "3"):
                    n = gender()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set Gender='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "4"):
                    n = status()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set Status='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "5"):
                    n = nation()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set Nationality='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "6"):
                    n = father()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set Father='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "7"):
                    n = address()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set Address='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "8"):
                    n = landmark()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set Landmark='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "9"):
                    n = city()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set City='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "10"):
                    n = pin()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set pin_code='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "11"):
                    n = res_type()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set res_type='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "12"):
                    n = phn()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set ph_no='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "13"):
                    n = email()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set email='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "14"):
                    n = occu()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set occupation='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                elif (c == "15"):
                    n = annual()
                    u = input(
                        "Are you sure you want to update your details?(Y/N)\n")
                    if (u != 'n' or u != 'N'):
                        query = "Update customer set an_inc='{}' where CUS_id='{}'".format(
                            n, cus_id)
                        try:
                            curr.execute(query)
                            con.commit()
                            print("Customer details of CUSTOMER",
                                cus_id, "has been updated...")
                        except:
                            con.rollback()
                            print("ERROR!!!")
                    elif (u != 'y' or u != 'Y' or u != 'n' or u != 'N'):
                        print("INVALID INPUT!!!")
                x = input("WANT TO UPDATE ANY OTHER DETAILS?(Y/N)\n--> ")
                if (x == 'y' or x == 'Y'):
                    continue
                elif (x == 'n' or x == 'N'):
                    break
                else:
                    print("INVALID INPUT")
                    break
            else:
                print("INVALID INPUT!!!")
    else:
        print("There is no data of CUSTOMER", cus_id, "is available...")


def acc_exist(mycur, acc):
    flag = 0
    mycur.execute(
        "Select ACC_no from customer where ACC_no='{}'".format(acc))
    d = mycur.fetchall()
    for row in d:
        if (acc == row[0]):
            flag = 1
    return flag


def details(mycur, acc):
    mycur.execute(
        "Select Name,ph_no from customer where ACC_no='{}'".format(acc))
    d = mycur.fetchall()
    for row in d:
        print("Name :", row[0])
        print("Phone number :", row[1])


def acc_update(mycur, amount, a, acc, process):
    mycur.execute(
        "Update account set balance='{}' where acc_no='{}'".format(a, acc))
    con.commit()
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M")
    mycur.execute("Select CUS_id from customer where ACC_no='{}'".format(acc))
    d = mycur.fetchall()
    for row in d:
        if (process == "DEPOSIT"):
            print(amount, "INR has been successfully credited in your account...\nNow your account balance is", a, "INR")
            mycur.execute("Insert into transaction(cus_id,acc_no,amount,t_method,t_date,t_time) VALUES('{}','{}','{}','{}','{}','{}')".format(
                row[0], acc, amount, "CREDIT", date, time))
            con.commit()
        else:
            print(amount, "INR has been successfully debited from your account...\nNow your account balance is", a, "INR")
            mycur.execute("Insert into transaction(cus_id,acc_no,amount,t_method,t_date,t_time) VALUES('{}','{}','{}','{}','{}','{}')".format(
                row[0], acc, amount, "DEBIT", date, time))
            con.commit()


def withdrawal(curr):
    while True:
        acc = input("Enter your account number : ")
        if (check(acc) == 1):
            break
        else:
            print("INVLID INPUT!!!")
    if (acc_exist(curr, acc) == 1):
        details(curr, acc)
        amt = int(input("Enter the amount you want to withdraw...\n--> "))
        curr.execute(
            "Select balance from account where acc_no='{}'".format(acc))
        d = curr.fetchall()
        for row in d:
            if (row[0] == 0 or amt > row[0] or row[0] <= 1000):
                print("INSUFFICIENT ACCOUNT BALANACE!!!")
            else:
                a = row[0]-amt
                acc_update(curr, amt, a, acc, "WITHDRAWAL")
    else:
        print("YOU HAVEN'T OPEN YOUR ACCOUNT YET!!!")


def deposit(curr):
    while True:
        acc = input("Enter your account number : ")
        if (check(acc) == 1):
            break
        else:
            print("INVLID INPUT!!!")
    if (acc_exist(curr, acc) == 1):
        details(curr, acc)
        amt = int(input("Enter the amount you want to deposit...\n--> "))
        curr.execute(
            "Select balance from account where acc_no='{}'".format(acc))
        d = curr.fetchall()
        for row in d:
            a = row[0]+amt
            acc_update(curr, amt, a, acc, "DEPOSIT")
    else:
        print("YOU HAVEN'T OPEN YOUR ACCOUNT YET!!!")


def balance(curr):
    while True:
        acc = input("Enter your account number : ")
        if (check(acc) == 1):
            break
        else:
            print("INVLID INPUT!!!")
    if (acc_exist(curr, acc) == 1):
        details(curr, acc)
        curr.execute(
            "Select balance from account where acc_no='{}'".format(acc))
        d = curr.fetchall()
        for row in d:
            print("Your account balance is", row[0], "INR")
    else:
        print("YOU HAVEN'T OPEN YOUR ACCOUNT YET!!!")


def date_check(mycur, d):
    flag = 0
    mycur.execute("Select t_date from transaction where t_date='{}'".format(d))
    c = mycur.fetchall()
    for row in c:
        if (d == row[0]):
            flag = 1
    return flag


def transaction(curr):
    while True:
        acc = input("Enter your account number : ")
        if (check(acc) == 1):
            break
        else:
            print("INVLID INPUT!!!")
    if (acc_exist(curr, acc) == 1):
        details(curr, acc)
        while True:
            x = input(
                "1. TRANSCATION HISTORY\n2. TRANSACTIONS BETWEEN PERIODS\n3. TRANSACTION OF A PARTICULAR DATE\n--> ")
            if (x == '1' or x == '2' or x == '3'):
                break
            else:
                print("INVALID INPUT")
        if (x == '1'):
            curr.execute(
                "Select amount,t_method,t_date,t_time from transaction WHERE acc_no='{}'".format(acc))
            d = curr.fetchall()
            print()
            if (d != None):
                print (tabulate(d, headers=["AMOUNT", "TRANSACTION", "DATE", "TIME"]))
            else:
                print("THERE IS NO TRANSACTION HISTORY!!!")
        elif (x == '2'):
            print(
                "Enter two dates from which date to which date you want to see you transaction history")
            while True:
                a = input("Date 1 (DD-MM-YYY) : ")
                if (date_check(curr, a) == 1):
                    break
                else:
                    print("ENTER A VALID TRANSACTION DATE!!!")
            while True:
                c = input(
                    "Date 2 (DD-MM-YYY) : ")
                if (date_check(curr, c) == 1):
                    break
                else:
                    print("ENTER A VALID TRANSACTION DATE!!!")
            curr.execute(
                "Select amount,t_method,t_date,t_time from transaction WHERE acc_no='{}' AND (t_date BETWEEN '{}' AND '{}')".format(acc, a, c))
            d = curr.fetchall()
            print()
            if (d != None):
                print (tabulate(d, headers=["AMOUNT", "TRANSACTION", "DATE", "TIME"]))
            else:
                print("THERE IS NO TRANSACTION HISTORY!!!")
        else:
            while True:
                a = input("Date (DD-MM-YYY) : ")
                if (date_check(curr, a) == 1):
                    break
                else:
                    print("ENTER A VALID TRANSACTION DATE!!!")
            curr.execute(
                "Select amount,t_method,t_date,t_time from transaction WHERE (acc_no='{}' AND t_date='{}')".format(acc, a))
            d = curr.fetchall()
            print()
            if (d != None):
                print (tabulate(d, headers=["AMOUNT", "TRANSACTION", "DATE", "TIME"]))
            else:
                print("THERE IS NO TRANSACTION HISTORY!!!")
    else:
        print("YOU HAVEN'T OPEN YOUR ACCOUNT YET!!!")


def del_acc(curr):
    while True:
        cus_id = input("Enter your customer id : ")
        if (check(cus_id) == 1 and len(cus_id) == 12):
            break
        else:
            print("INVALID INPUT!!!")
    if (cus_exist(curr, cus_id) == 1):
        curr.execute(
            "Select Name,ph_no from customer where CUS_id='{}'".format(cus_id))
        d = curr.fetchall()
        for row in d:
            print("Name :", row[0])
            print("Phone number :", row[1])
        curr.execute(
            "Select balance from account where cus_id='{}'".format(cus_id))
        d = curr.fetchall()
        choice = input(
            "Are you sure you want to delete your account?...(Y/N)\n--> ")
        if (choice == 'y' or choice == 'Y'):
            query = "Delete from customer where CUS_id='{}'".format(cus_id)
            for row in d:
                if (row[0] != 0):
                    try:
                        curr.execute(query)
                        con.commit()
                        print("ACCOUNT OF CUSTOMER", cus_id,
                            "HAS BEEN DELETED SUUCCESSFULLY!!!")
                        print(row[0], "INR HAS BEEN DEBITED!!!")
                    except:
                        con.rollback()
                        print("FAILED TO DELETE THE ACCOUNT OF CUSTOMER", cus_id)
                else:
                    try:
                        curr.execute(query)
                        con.commit()
                        print("ACCOUNT OF CUSTOMER", cus_id,
                            "HAS BEEN DELETED SUUCCESSFULLY!!!")
                    except:
                        con.rollback()
                        print("FAILED TO DELETE THE ACCOUNT OF CUSTOMER", cus_id)
        else:
            print("ACCOUNT DELETION OF CUSTOMER",
                cus_id, "HAS BEEN CANCELED!!!")
    else:
        print("THERE IS NO DATA OF CUSTOMER", cus_id, "EXISTS")


def pass_check(p):
    flag = 0
    while True:
        if (len(p) < 6 or len(p) > 16):
            flag = 1
            break
        elif not re.search("[a-z]", p):
            flag = 1
            break
        elif not re.search("[A-Z]", p):
            flag = 1
            break
        elif not re.search("[0-9]", p):
            flag = 1
            break
        elif not re.search("[#@$]", p):
            flag = 1
            break
        elif re.search("\s", p):
            flag = 1
            break
        else:
            flag = 0
            break
    return flag


def reset_pass(curr, x):
    while True:
        print(
            "VALIDATION:\n1. AT LEAST 1 LETTER BETWEEN [a-z] AND 1 LETTER BETWEEN [A-Z]\n2. AT LEAST 1 NUMBER BETWEEN [0-9]\n3. AT LEAST 1 CHARACTER FROM [$,#,@]\n4. MINIMUM LENGTH 6 CHARACTER\n5. MAXIMUM LENGTH 16 CHARACTERS")
        p = input("Enter the new password : ")
        if (pass_check(p) == 0):
            break
        else:
            print("INVALID PASSWORD!!!")
    curr.execute("Update pass set pas='{}' Where pas='{}'".format(p, x))
    con.commit()
    print("PASSWORD UPDATED SUCCESSFULLY!!!")


def pass_exist(curr, y):
    flag = 0
    curr.execute("Select pas from pass Where pas='{}'".format(y))
    d = curr.fetchall()
    for row in d:
        if (y == row[0]):
            flag = 1
    return flag


def check_cus(cur):
    cur.execute(
        "Select CUS_id,ACC_no,Name,Gender,Address,ph_no,email from customer")
    d = cur.fetchall()
    if (cur.rowcount > 0):
        print("Total number of customers entered :", cur.rowcount)
        print()
        print (tabulate(d, headers=["Customer ID", "Account Number", "Name", "Gender", "Address", "Phone", "Email ID"]))


def admin(curr):
    while True:
        p = input("Enter password : ")
        if (pass_exist(curr, p) == 1):
            break
        else:
            print("INCORRECT PASSWORD!!!")
    while True:
        print(
            "WHAT ACTION YOU WANT TO PERFORM ?\n1. CHECK CUTOMER ENTRY\n2. UPDATE PASSWORD")
        x = input("--> ")
        if (check(x) == 1):
            break
        else:
            print("INVALID INPUT!!!")
    if (x == '1'):
        check_cus(curr)
    else:
        reset_pass(curr, p)


if con.is_connected():
    cur = con.cursor()
    perform(cur)
    while True:
        print()
        while True:
            a = input('Want to perform any other operations?...y/n...')
            if (a == 'y' or a == 'Y' or a == 'n' or a == 'N'):
                break
            else:
                print("INVALID INPUT!!!")
        if (a == 'y' or a == 'Y'):
            perform(cur)
        else:
            print('THANK YOU. HAVE A GREAT DAY :)')
            break
else:
    print('Sorry not able to connect.....')
