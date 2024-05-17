import mysql.connector
from prettytable import PrettyTable
print("Welcome to the Bank of Voldigoads")
adm=int(input("are you an admin or a viewer \n 1 for admin \n 2 for user"))
if adm==1:
    ap=int(input("pls enter your password"))  #grants all privilages to select database
    if ap==1245:
        host = "localhost"
        user = "root"
        password="deco"
        database="bankdb"
        try:
            connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database )
            print("Connection established!")
        except mysql.connector.Error as err:
            print("Error:", err)
        cursor=connection.cursor()
        im=int(input("pls enter the users id"))    
        f=int(input("Please press the given keys to select the function you would like to perform \n 1.Display all records for given user \n 2.Alter certain records \n 3.Delete records for a certain user"))    
        if f==1:
            rquery="SELECT * FROM userdetails NATURAL JOIN financial_details WHERE userdetails.person_id = %s"
            cursor.execute(rquery,(im,))
            result=cursor.fetchall()
            table = PrettyTable([column[0] for column in cursor.description])
            for row in result:
                table.add_row(row)
                print(table)
        if f==2:
            al=int(input("what operation would you like to perform \n 1 for updating Saved balance \n 2 for updating loan borrowed \n 3 for updating loan left \n 4 update credit limit"))
            if al==1:
                try:
                    uquery="""
                            UPDATE financial_details
                            SET saving_balance = %s
                            WHERE person_id = %s
                    """
                    sbalance=int(input("enter updated saving balance"))
                    cursor.execute(uquery,(sbalance,im))
                    connection.commit()
                    print("changes done succesfully")
                except:
                    print("error occured pls recheck your permissions")    
            if al==2:
                try:
                    ulquery=""" 
                               UPDATE financial_details
                               SET loan_taken = %s
                               WHERE person_id = %s
                    """
                    ltaken=int(input("PLS ENTER THE UPDATED LOAN AMOUNT"))
                    cursor.execute(ulquery,(ltaken,im))
                    connection.commit()
                    print("changes commited successfully")
                except:
                    print("error occured pls try again")   
            if al==3:
                try:
                    ullquery=""" 
                               UPDATE financial_details
                               SET loan_left = %s
                               WHERE person_id = %s
                    """
                    lleft=int(input("PLS ENTER THE REMAINING LOAN AMOUNT"))
                    cursor.execute(ullquery,(lleft,im))
                    connection.commit()
                    print("changes commited succesfully")
                except:    
                    print("ERROR OCCURED")
            if al==4:
                try:
                    uclquery=""" 
                               UPDATE financial_details
                               SET credit_limit = %s
                               WHERE person_id = %s
                    """
                    climit=int(input("PLS ENTER THE UPDATED CREDIT LIMIT"))
                    cursor.execute(uclquery,(climit,im))
                    connection.commit()
                    print("changes commited succesfully")
                except:
                    print("ERROR OCCURED")
        if f==3:
            delete=int(input("Pls press the following keys for the following delete operations \n 1 delete a certain users records \n 2 delete all records"))
            if delete==1:
                try:
                    connection.start_transaction()
                    delquery="""  
                               DELETE FROM userdetails WHERE person_id= %s                   
                    """
                    del2query=""" DELETE FROM financial_details WHERE person_id= %s """

                    cursor.execute(del2query,(im,))
                    cursor.execute(delquery,(im,))
                    connection.commit()
                    print("DELETED SUCCESSFULLY") 
                except:
                    print("ERROR PLS CHECK IF YOU HAVE ADMIN PERMISSIONS")
            if delete==2:
                try:
                    connection.start_transaction()
                    delequery=""" DELETE FROM userdetails  """
                    dele2query=""" DELETE FROM financial_details """
                    cursor.execute(dele2query)
                    cursor.execute(delequery)
                    connection.commit()
                    print("DELETED SUCCESFULLY")
                except:
                    print("ERROR PLS CHECK IF YOU HAVE ADMIN PERMISSIONS")        
if adm==2:
    host="localhost"        #grants only select and update priviledges to database
    user="deco"
    password="hola"
    database="bankdb"
    try:
        connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database )
        print("Connection established!")
        cursor=connection.cursor()
    except mysql.connector.Error as err:
        print("Error:", err)
    hel=int(input("DO YOU HAVE AN ACC WITH US PRESS 1 FOR YES AND 2 TO CREATE A NEW ACC"))
    if hel==1:
        idu=int(input("Pls enter your id"))
        op=int(input("which operations would you like to perform \n 1 View all your details \n 2 Change your personal Details \n 3 take new loan \n 4 repay previous loan \n 5 deposit money into savings \n 6 pay credit card bills \n 7 deposit money into Fixed Deposit "))    
        if op==1:
            rquery="SELECT * FROM userdetails NATURAL JOIN financial_details WHERE userdetails.person_id = %s"
            cursor.execute(rquery,(idu,))
            result=cursor.fetchall()
            table = PrettyTable([column[0] for column in cursor.description])
            for row in result:
                table.add_row(row)
                print(table)
        if op==2:
            per=int(input("which details would you like to change \n 1 Phone number \n 2 City \n 3 Address"))
            if per==1:
                try:
                    upquery=""" UPDATE userdetails
                                SET phone_number= %s                
                                WHERE person_id = %s;"""
                    phno=int(input("Enter updated phone number"))
                    cursor.execute(upquery,(phno,idu))
                    connection.commit()
                    print("changes made succesfully")
                except:
                    print("ERROR OCCURED")
            if per==2:
                try:
                    ucquery="""UPDATE userdetails
                             SET city = %s
                             WHERE person_id = %s ;"""
                             
                    cit=input("enter updated city")
                    cursor.execute(ucquery,(cit,idu))
                    connection.commit()
                    print("changes made successfully")
                except:
                    print("ERROR OCCURED")
            if per==3:
                try:
                    uaquery="""UPDATE userdetails
                            SET address = %s
                            WHERE person_id = %s;"""
                            
                    newadd=input("enter updated address")
                    cursor.execute(uaquery,(newadd,idu))
                    connection.commit()
                    print("changes made succesfully")
                except:        
                    print("ERROR OCCURED")
        if op==3:
            loan=int(input("How much loan would you like to take?"))
            try:
                loantquery=""" SELECT loan_taken FROM financial_details WHERE person_id = %s;"""
                cursor.execute(loantquery,(idu,))
                result1=cursor.fetchone()
                new_loan=loan+result1[0]
                ultquery=""" UPDATE financial_details
                             SET loan_taken = %s
                             WHERE person_id = %s;"""
                             
                print("your total loan stands out to be",new_loan)
                cursor.execute(ultquery,(new_loan,idu))
                connection.commit()
                print("LOAN GRANTED SUCCESSFULLY")               
            except Exception as e:
                print(e)
        if op==4:
            loanr=int(input("how much loan would you like to return"))
            try:
                loanrquery=""" SELECT loan_left FROM financial_details WHERE person_id = %s;"""
                cursor.execute(loanrquery,(idu,))
                result2=cursor.fetchone()
                new_loanleft=result2[0]-loanr
                ulrquery=""" UPDATE financial_details
                             SET loan_left = %s
                             WHERE person_id = %s;
                """ 
                print("your remaining loan turns out to be",new_loanleft)
                cursor.execute(ulrquery,(new_loanleft,idu))
                connection.commit()
                print("LOAN PAID SUCCESSFULLY")
            except Exception as e:
                print(e)
        if op==5:
            depsav=int(input("how much money would you like to deposit"))
            try:
                print(idu)
                savquery="SELECT saving_balance FROM financial_details WHERE person_id = %s ;"
                cursor.execute(savquery,(idu,))
                result3=cursor.fetchone()
                new_sav=result3[0]+depsav
                usquery="""  UPDATE financial_details
                             SET saving_balance = %s
                             WHERE person_id = %s;
                """ 
                print("your new savings out to be",new_sav)
                cursor.execute(usquery,(new_sav,idu))
                connection.commit()
                print("SAVINGS DEPOSITED SUCCESFULLY")
            except Exception as e:
                print(e)
        if op==6:
            crebill=int(input("pls enter the bill amount you want to pay"))
            try:
                credquery=""" SELECT credit_card_bill FROM financial_details WHERE person_id = %s;"""
                cursor.execute(credquery,(idu,))
                result4=cursor.fetchone()
                new_bill=result4[0]-crebill
                ucbquery="""  UPDATE financial_details
                              SET credit_card_bill = %s
                              WHERE person_id = %s;
                """ 
                print("your new bill is",new_bill)
                cursor.execute(ucbquery,(new_bill,idu))
                connection.commit()
                print("CREDIT CARD BILL PAID SUCCESSFULLY")
            except:
                print("ERROR OCCURED")
        if op==7:
            fd_dep=int(input("enter the amount of money you want to deposit"))
            try:
                fdquery=""" SELECT fd_balance FROM financial_details WHERE person_id = %s;"""
                cursor.execute(fdquery,(idu,))
                result5=cursor.fetchone()
                new_fd_bal=fd_dep+result5[0]
                ufdquery="""  UPDATE financial_details
                              SET fd_balance = %s
                              WHERE person_id = %s;
                """ 
                print("your new balance is",new_fd_bal)
                cursor.execute(ufdquery,(new_fd_bal,idu))
                connection.commit()       
                print("BALANCE UPDATED SUCCESSFULLY")
            except:
                print("ERROR OCCURED")
    #ACCOUNT CREATION
    if hel==2:
        person_id = int(input("Enter Person ID: "))
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        phone_number = input("Enter Phone Number: ")

        loan_taken = float(input("Enter Loan Taken: "))
        loan_left = float(input("Enter Loan Left: "))
        saving_balance = float(input("Enter Saving Balance: "))
        fd_balance = float(input("Enter FD Balance: "))
        interest_percent = float(input("Enter Interest Percent: "))
        overdraft = float(input("Enter Overdraft: "))
        fd_current = float(input("Enter FD Current: "))
        credit_card_bill = float(input("Enter Credit Card Bill: "))
        credit_limit = float(input("Enter Credit Limit: "))
        
        try:
            userdetail_query="""INSERT INTO userdetails (person_id, name, address, city, phone_number)
            VALUES (%s, %s, %s, %s, %s)"""
            userdetail_values=(person_id,name,address,city,phone_number)
            cursor.execute(userdetail_query,userdetail_values)
            
            
            # Insert into financial_details table
            financial_query = """
            INSERT INTO financial_details (person_id, loan_taken, loan_left, saving_balance, fd_balance,
                                    interest_percent, overdraft, fd_current, credit_card_bill, credit_limit)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            financial_values = (person_id, loan_taken, loan_left, saving_balance, fd_balance,interest_percent, overdraft, fd_current, credit_card_bill, credit_limit)
            cursor.execute(financial_query, financial_values)
            connection.commit()
            print("data registered successfully")
            print("your account has been succesfully created")
        except mysql.connector.Error as err:
            print("error occured",err)