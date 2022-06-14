#==========================================================================================
#                            IMPORTING MODULES BASIC MODULES
#==========================================================================================


import os
import sys
import easygui
import pyttsx3
import subprocess
import pickle
from easygui import *
from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import *

#==========================================================================================
#                             INSTALLING MODULES & PACKAGES
#==========================================================================================


#==========================================================================================
engine = pyttsx3.init()
sound = engine.getProperty('voices')

engine.setProperty('voice',sound[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#==========================================================================================

root=Tk()
root.attributes('-fullscreen', True)
root.title('PROTECHT')
root.geometry("1280x720")
root.configure(background='black')
load=Image.open("C:\\Users\\ganes\\AppData\\Local\\Programs\\Python\\Python38\\bank\\simple1.png")
render=ImageTk.PhotoImage(load)
image=Label(root,image=render)
image.place(x=0,y=0)
Label(root, text = 'TO ENTER INTO APPLICATION', font =( 'Verdana', 15)).pack(side = TOP, pady = 10)
photo = PhotoImage(file = r"C:\Users\ganes\AppData\Local\Programs\Python\Python38\bank\button1.png")
photoimage = photo.subsample(3, 3)
Button(root, text = 'CLICK THIS', image = photoimage,compound = LEFT,command = root.destroy).pack(side = TOP)
speak('WELCOME TO OUR PROTECHT')
root.mainloop()
#==========================================================================================
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

with open('launch.dat','rb+') as f:
    d=pickle.load(f)


if d['firstrun']==True:
    speak("PLEASE CLICK ON START BUTTON TO INSTALL PACKAGES FOR THIS PROGRAM IF THEY ARE NOT PRESENT IN YOUR SYSTEM")
    version = "Package Installation"
    options = ["  START  ","  CANCEL  "]
    button = buttonbox("INSTALL PACKAGES FOR THIS PROGRAM IF THEY ARE NOT PRESENT IN YOUR SYSTEM",title=version,choices=options)

    if button == options[0]:

        install('mysql-connector-python==8.0.22')
        install('tabulate==0.8.7')
        install('pyfiglet==0.8.post1')
        install('termcolor==1.1.0')
        install('stdiomask==0.0.6')
        install('colorama==0.4.4')
        install('easygui==0.98.1')
        install('tkinter')
        install('matplotlib==3.3.0')

        button = "PACKAGES INSTALLED SUCCESSFULLY"
        os.system('cls')    

    else:
        os.system('cls')
    with open('launch.dat','wb') as f:
        d['firstrun']=False
        pickle.dump(d,f)
else:
    pass


#==========================================================================================
#                         IMPORTING MODULES AFTER INSTALLATION
#==========================================================================================

import time                                                               
import stdiomask                                
import string
import csv

import colorama                                 
import pyfiglet                                 
import mysql.connector as mycon                
import matplotlib.pyplot as plt


from tabulate import tabulate
from stdiomask import *


from pyfiglet import figlet_format              
from colorama import init,Back as bg            
init(strip=not sys.stdout.isatty())             
from termcolor import cprint                    

#==========================================================================================
#                                       ABOUT
#==========================================================================================

def about():
    
    a = '''

    About the Project:
    ~~~~~~~~~~~~~~~~~

    Talking about the features of this Protecht, the Admin can create an account by providing the required data of the customer
    along with his/her initial amount which is to be deposited. Admin can also view the statistical representation of amount per person.The admin
    can also view the customer's details, modify the details or delete the details of any customer.

    The Customer can also deposit and withdraw money just by providing the user account number and entering the amount and perform the
    transactions. This simple console-based system provides the simplest management of bank account and transactions.

    All the data's are stored in tabular form in a relational database i.e. MySQL database which is a free and open-source
    software under the terms of the GNU General Public License, and is also available under a variety of proprietary licenses.MySQL was owned
    and sponsored by the Swedish company MySQL AB, which was bought by Sun Microsystems (now Oracle Corporation).
    '''
    b='''    

           +--------------------------------+---------------------------------------------+-----------------------------+
            |   REQUIRED INSTALLATIONS :-    |              REQUIRED HARDWARES :-          |     REQUIRED SOFTWARES :-   |
            |--------------------------------+---------------------------------------------+-----------------------------+
            | 1. pip install mysql.connector | 1. CPU : Inter Pentium 2.20 GHz             | 1. Python IDLE 3.5 or above |
            | 2. pip install tabulate        | 2. OPERATING SYSTEM : Windows 7             | 2. MySQL (DBMS)             |
            | 3. pip install pyfiglet        | 3. RAM : 512 MB                             | 3. Notepad                  |
            | 4. pip install termcolor       | 4. A complete Computer System               |                             |
            | 5. pip install stdiomask       | 5. INTERNET connection for the installation |                             |
            | 6. pip install easygui         |    of packages and modules.                 |                             |
            | 7. pip install tkinter         |                                             |                             |
            | 8. pip install colorama        |                                             |                             |
            | 9. pip install matplotlib      |                                             |                             | 
            | 10.pip install subprocess      |                                             |                             |
            +--------------------------------+---------------------------------------------+-----------------------------+



        
                                                                                                        
'''    

    os.system('cls')

    text = "ABOUT :-"
    cprint(figlet_format(text, font="starwars"), "blue")
  
    cprint(a,'cyan')
    cprint(b,'cyan')

    version = "About The Project"
    options = ["  YES  ","  NO  "]
    button = buttonbox("DO YOU WANT TO LISTEN ABOUT THIS PROJECT",title=version,choices=options)

    if button == options[0]:
        speak('''This project has been created by Ganesh and James Robin Raj of class 12th COMPUTER SCIENCE  under the guidance of MRS S Shanmughapriya and MRS Ananthy''')
        speak(a)
    else:
        pass
    
    while True:
        cprint('DO YOU WANT TO CONTINUE (Y/N) :-','green')
        speak('DO YOU WANT TO CONTINUE')
        ab_input = input('>>>  ').lower()
        
        if ab_input == "":
            cprint('YOUR CHOICE IS OTHER THAN THE GIVEN CHOICE,PLEASE TRY AGAIN','yellow')
            speak('YOUR CHOICE IS OTHER THAN THE GIVEN CHOICE, PLEASE TRY AGAIN')

        elif ab_input == 'y':
            os.system('cls')
            main()
                

        elif ab_input == 'n':
            easygui.msgbox('CLOSING THE APPLICATION . . . !')
            time.sleep(3)
            sys.exit()
    

        else:
            cprint('YOUR CHOICE IS OTHER THAN THE GIVEN CHOICE TRY AGAIN','yellow')


#==========================================================================================
#                                DATABASE CONNECTION
#==========================================================================================

#------------------------------------------------------------------------------------------
#               GETTING PASSWORD FOR AUTHENTICATION AND AUTHORISATION
#------------------------------------------------------------------------------------------

speak("CLICK ON 'YES' BUTTON IF YOUR MySQL USER-NAME IS ROOT")

version = "USER-NAME"
options = ["  YES  ","  NO  "]
button = buttonbox("CLICK ON 'YES' BUTTON IF YOUR MySQL USER-NAME IS ROOT",title=version,choices=options)

if button == options[0]:
    c = 'root'

else:
    speak("PLEASE ENTER YOUR MySQL USERNAME:-")
    c = easygui.enterbox("ENTER YOUR MY-SQL USERNAME:-")
    while True:
        if c=="":
            speak("YOU CAN'T LEAVE it as it is KINDLY FILL it")
            c = easygui.enterbox("ENTER YOUR MY-SQL USERNAME:-")
        else:
            break

speak('PLEASE ENTER YOUR MySQL PASSWORD')
p = passwordbox('ENTER YOUR MySQL PASSWORD :-')
while True:
    if p=="":
        speak("YOU CAN'T LEAVE it AS it IS KINDLY FILL it")
        p = passwordbox('ENTER YOUR MySQL PASSWORD :-')
    else:
        break
    

#==========================================================================================

con = mycon.connect(host="localhost",user=c, password=p)
mycursor=con.cursor()
b="legend"
mycursor.execute("create database if not exists {}".format(b))
mycursor.execute("use {}".format(b))

#==========================================================================================
#                                 CREATING TABLE
#==========================================================================================

mycursor.execute("""create table if not exists bank_master(
                        ID_NO bigint(15) primary key NOT NULL UNIQUE,
                        NAME VARCHAR(20) NOT NULL,
                        DOB DATE NOT NULL,
                        PLACE_ORGIN VARCHAR(35) NOT NULL,
                        PH_NO BIGINT(15) NOT NULL,
                        EMAIL VARCHAR(35),
                        ACC_TYPE VARCHAR(2) NOT NULL,
                        AMOUNT BIGINT(15) NOT NULL);""")

#==========================================================================================
#                               INSERTING DATA/VALUES
#==========================================================================================

speak('DO YOU WANT TO INSERT SOME BY-DEFAULT DATA IN YOUR MySQL DATABASE ?')
version = "DEFAULT-DATA"
options = ["  YES  ","    NO  "]
button = buttonbox("DO YOU WANT TO INSERT SOME BY-DEFAULT DATA IN YOUR MySQL DATABASE ?", title = version, choices = options)
try:
    if button == options[0]:
    
        value0 = '''insert into bank_master
        values(625100200,'GANESH','2002-11-20','CHENNAI',9775766850,'12a.ganesh.k.3029@gmail.com','c',100000)'''    

        value1 = '''insert into bank_master
        values(625100201,'JAMES ROBIN RAJ','2002-05-11','SALEM',9784563210,'12a.jamesrobinraj.p.4190@gmail.com','c',80000)'''

        value2 = '''insert into bank_master
        values(625100202,'KAMAL HAASAN','2003-02-19','PARAMAKUDI',9563244474,'12a.shasankrahul.m.1719@gmail.com','c',75000)'''    

        value3 = '''insert into bank_master
        values(625100203,'RITHVIK','2002-03-21','DINDUGUL',8745691233,'12a.rithvik.g.1679@gmail.com','c',90000)'''

        value4 = '''insert into bank_master
        values(625100204,'ULTRALEGEND','2002-11-20','MADURAI',7884563210,'ULTRALEGEND@gmail.com','c',65000)'''    

        value5 = '''insert into bank_master
        values(625100205,'LEGEND','2001-01-10','AAMBUR',6543219787,'LEGENDthegreat@gmail.com','c',50000)'''

        mycursor.execute(value0)
        mycursor.execute(value1)
        mycursor.execute(value2)
        mycursor.execute(value3)
        mycursor.execute(value4)
        mycursor.execute(value5)
    
        con.commit()

        easygui.msgbox('DATA ADDED SUCCESSFULLY . . . !')
        time.sleep(2)
        os.system('cls')

except:
    easygui.msgbox("""THE DATA'S IN THE TABLE BANK_MASTER IS ALREADY PRESENT IN THE DATABASE. . . !""")
    time.sleep(2)
    os.system('cls')

    
else:
    os.system('cls')

#==========================================================================================
#                                        ADMIN
#==========================================================================================
from tkinter import *
def admin():

#------------------------------------------------------------------------------------------
#                     USERNAME & PASSWORD VERIFICATION USING "TKINTER"
#------------------------------------------------------------------------------------------
    
    window = Tk()
    window.title('BANKING LOGIN PAGE')
    window.configure(background='cyan')

    #FRAME BLUEPRINT
    
    width = 320
    height = 380
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry("%dx%d+%d+%d" % (width, height, x, y))

    #COMMAND FUNCTIONS

    def click():
        
        ent_text=textentry.get()
        pass_text=pw_entry.get()
        user1 = ['GANESH','JAMES_ROBIN_RAJ','ganesh','james_robin_raj']

        if ent_text in user1 and pass_text == '0000':
            speak('YOU ARE A VALID USER')
            output.insert(END,'YOU ARE A VALID USER. . .\n')

        else:
            speak('YOU ARE AN INVALID USER')
            output.insert(END,'YOU ARE AN INVALID USER. . . TRY AGAIN\n')

    def fun1():

        window.destroy()
        cprint('\t\t\t\t\t\t LOGIN SUCCESFULL, CONTINUE\n \t\t\t\t\t\t PRESS ENTER','green')
        os.system('cls')

        cprint('*'*167,'cyan')
        print()

        cprint('\t\t\t\t\t\t WELCOME TO PROTECHT','magenta')
        speak('WELCOME TO PROTECHT')
        print()
        cprint('*'*167,'cyan')
        print()
        

    #LABEL FOR USERNAME
    
    lbl_username = Label(window,text='USERNAME:',bg='cyan',fg='black',font='algerian 15')
    lbl_username.grid(row=2,column=0,sticky=W)
    textentry = Entry(window,width=20,bg='deep sky blue',fg='black')
    textentry.grid(row=2,column=1)

    #LABEL FOR PASSWORD

    lbl_password = Label(window,pady=20,text='PASSWORD:',bg='cyan',fg='black',font='algerian 15')
    lbl_password.grid(row=3,column=0,sticky=W)
    pw_entry = Entry(window,show='*',width=20,bg='tomato',fg='black')
    pw_entry.grid(pady=20,row=3,column=1)

    #OUTPUT BOX TO PRINT VALID OR INVALID

    output = Text(window,width=40,height=4,wrap=WORD,bg = 'black',fg='white')
    output.grid(pady=25,row=5,columnspan=2)

    #SUBMIT BUTTON

    btn_submit = Button(window,text='SUBMIT',width=30,command=click,bg='yellow')
    btn_submit.grid(pady=25,row=4,columnspan=2)

    #LOGIN BUTTON
    
    btn_login = Button(window,text='LOGIN',width=30,command=fun1,bg='green2')
    btn_login.grid(pady=25,row=6,columnspan=2)
    
#------------------------------------------------------------------------------------------

    window.mainloop()

def admin_menu():
    
    text = "ADMIN :-"
    cprint(figlet_format(text, font="starwars"), "cyan")
    speak('ADMIN MENU')
    
    cprint('\t\t\t\t\t\t\t\t\tCURRENT DATE & TIME :- {}'.format(time.asctime()),'red')
    speak(time.asctime())
       
    cprint('''\t\t\t\t\t1.ABOUT CUSTOMER
\t\t\t\t\t2.ACTIONS
\t\t\t\t\t3.STATISTICAL REPRESENTATION
\t\t\t\t\t4.DATA BACKUP''','blue')
    cprint('''\t\t\t\t\t5.LOGOUT AS ADMIN''','green')
    cprint('''\t\t\t\t\t6.CLOSE THE APPLICATION\n''','red')
    cprint('ENTER YOUR CHOICE :','yellow')
    act = input('>>>  ')

    if act == '1':

        os.system('cls')
        cprint('*'*167,'blue')    
        text = "DATA :-"
        cprint(figlet_format(text, font="starwars"), "cyan")
        cprint('*'*167,'blue')

        aview()
        
    if act == '2':
        actions()

    if act == '5':
        os.system('cls')
        main()

    if act == '3':
        os.system('cls')
        graph()

    if act == '4':
        backup()
        
    if act == '6':
        speak('CLOSING THE APPLICATION')
        easygui.msgbox('CLOSING THE APPLICATION . . . !')
        time.sleep(2)
        sys.exit()

def aview():

    speak('PLEASE ENTER THE PIN')
    v_password = passwordbox('PLEASE ENTER PIN :-')
        
    pin = ['0000']

    if v_password in pin:

        mycursor.execute('select * from bank_master')
        result = mycursor.fetchall()
        print(tabulate(result, headers = ['id_no','name','dob','address','ph_no','email','acc_type','amount'], tablefmt=('grid')))
        
    else:
        print('You Are Not An Authorized User')
        
    
def actions():

    os.system('cls')
    cprint('*'*167,'magenta')

    text = "ACTIONS"

    cprint(figlet_format(text, font="starwars"), "cyan")
    cprint('*'*167,'magenta')

    cprint('\t\tWhat You Want To Do...','yellow')
    speak('What You Want To Do')

    b="\n\t\t\t"+"1."+'''INSERT CUSTOMER DETAILS
\t\t\t2.UPDATE CUSTOMER DETAILS
\t\t\t3.DELETE CUSTOMER DETAILS
\t\t\t4.LOGOUT AS ADMIN'''
    cprint(b,'blue')
    speak(b)

    cprint('''\t\t\t5.CLOSE THE APPLICATION''','red')

    print()
    cprint('ENTER YOUR CHOICE :','yellow')
    speak('ENTER YOUR CHOICE')

    ainput = input('>>>  ')

    if ainput == '1':
        insert()

    if ainput == '2':
        update()

    if ainput == '3':
        delete()

    if ainput == '4':
        os.system('cls')
        main()

    if ainput == '5':
        
        time.sleep(3)
        sys.exit()

def insert():

    speak('Enter customer details')
    msg = "Enter Costumer's personal information"
    title = "ENTER CUSTOMER DETAILS"
    fieldNames = ["NAME", "DOB (YYYY-MM-DD)", "PLACE OF ORGIN","PHONE NO.","E-MAIL ID","ACCOUNT TYPE(C/S)","AMOUNT (IN ₹)" ]
    Values = multenterbox(msg, title, fieldNames)

    if Values is None:
        sys.exit(0)

    # MAKE SURE THAT NONE OF THE FIELDS WERE LEFT BLANK

    while 1:

        errmsg = ""
        for i, name in enumerate(fieldNames):

            if Values[i].strip() == "":
              errmsg += "{} Is A Required Field.\n\n".format(name)

        if errmsg == "":
            break                   
        Values = multenterbox(errmsg, title, fieldNames, Values)

        if Values is None:
            break
    try:
        x = Values
        b = tuple(x)
        insert_list = [b]
        
        name = x[0]
        dob = x[1]
        place_orgin=x[2]
        ph_no = x[3]
        email = x[4]
        acc_type = x[5]
        amount = x[6]
        
        count=625100200

        q = "select id_no from bank_master"
        mycursor.execute(q)
        m=mycursor.fetchall()

        for i in m:
            count+=1

        insert_values = 'insert into bank_master() VALUES(%s, %s, %s,%s, %s, %s, %s, %s)'
        row = [(count,name,dob,place_orgin,ph_no,email,acc_type,amount)]
        mycursor.executemany(insert_values, row)
        con.commit()
        id_no=count

        
        msg = "DATA SUCCESSFULLY UPLOADED \nHELLO {} YOUR ID-NUMBER IS {} ".format(name,count)
        
        msgbox(msg)
        speak(msg)

        print(tabulate(insert_list,headers=['name','dob','address','ph_no','email','acc_type','amount'], tablefmt=('grid')))

    except:

        if x == None:
            cprint("No data given","red")
    
    speak('DO YOU WANT TO INSERT MORE DETAILS')
    d=input('DO YOU WANT TO INSERT MORE DETAILS (Y/N) :').lower()

    if d == 'y':
        insert()    

def delete():

    d_no = int(input('IDENTITY CARD NUMBER WHICH YOU WANT TO DELETE :'))
    del_command = 'DELETE FROM bank_master WHERE ID_NO = %s'
    delt = (d_no ,)
    mycursor.execute(del_command, delt)
    con.commit()

    speak('DATA DELETED SUCCESSFULLY')
    easygui.msgbox('DATA DELETED SUCCESSFULLY . . . !')


def update():

    i_input = int(input('ENTER THE IDENTITY CARD NUMBER :'))

    cprint(''' WHAT YOU WANT TO UPDATE
        \n\t1.NAME
        2.ADDRESS
        3.PHONE_NO
        4.EMAIL ''','green')
    cprint('''\t5.RETURN TO PREVIOUS MENU
        6.RETURN TO ADMIN MENU\n''','green')

    cprint('ENTER YOUR CHOICE :','yellow')
    u_input = input('>>>  ')

    if u_input == '1':

        up_name = input('NAME :').upper()
        up_command = 'UPDATE bank_master SET NAME= %s WHERE ID_NO=%s'
        updt = (up_name,i_input)
        mycursor.execute(up_command, updt)
        con.commit()

        easygui.msgbox('NAME UPDATED SUCCESSFULLY')

    if u_input == '2':

        up_name = input('ADDRESS :').upper()
        up_command ='UPDATE bank_master SET ADDRESS= %s WHERE ID_NO=%s'
        updt = (up_name,i_input)
        mycursor.execute(up_command, updt)
        con.commit()

        easygui.msgbox('ADDRESS UPDATED SUCCESSFULLY')
        

    if u_input == '3':

        up_name = int(input('PHONE_NO :'))
        up_command='UPDATE bank_master SET PH_NO= %s WHERE ID_NO=%s'
        updt = (up_name,i_input)
        mycursor.execute(up_command, updt)
        con.commit()

        easygui.msgbox('PHONE NO. UPDATED SUCCESSFULLY')

    if u_input == '4':

        up_name = input('EMAIL :')
        up_command = 'UPDATE bank_master SET EMAIL= %s WHERE ID_NO=%s'
        updt = (up_name,i_input)
        mycursor.execute(up_command, updt)
        con.commit()

        easygui.msgbox('EMAIL UPDATED SUCCESSFULLY')

    if u_input == '5':
        os.system('cls')
        actions()        

    if u_input == '6':
        os.system('cls')
        admin_menu()

#------------------------------------------------------------------------------------------
#                                        GRAPH
#------------------------------------------------------------------------------------------

def graph():

    cprint('*'*167,'blue')
    print()

    text="GRAPH :-"
    cprint(figlet_format(text, font="slant"), "cyan")
    
    cprint('\t\t\t\t\t\t\t\t\t\t\t\t\t\tCURRENT DATE & TIME :- {}'.format(time.asctime()),'red')
    cprint('*'*167,'blue')

    s = 'select name from bank_master'
    mycursor.execute(s)
    data = mycursor.fetchall()
    l = []

    for i in data:
        l.append(i[0])
        
    am = 'select amount from bank_master'    
    mycursor.execute(am)
    amount = mycursor.fetchall()
    m = []

    for j in amount:
        m.append(j[0])
    
    cprint('HOW DO YOU WANT TO ANALYSE ?','yellow')
    cprint('''\n1.BAR GRAPH
2.LINE GRAPH''','green')
    print()

    cprint('ENTER YOUR CHOICE','yellow')
    gr_input=input('>>>  ')

    if gr_input == '1':

        plt.bar(l,m,)
        plt.xticks(fontsize = 6,rotation = 30)
        plt.xlabel('NAMES ---->')
        plt.ylabel('AMOUNT ---->')

        plt.grid(b = True, which = 'major', color = '#666666', linestyle = '-')
        plt.title('CUSTOMER vs AMOUNT graph')

    if gr_input == '2':

        plt.plot(l,m,'c',marker = '*',markersize = 6,markeredgecolor = 'r')
        plt.xticks(fontsize = 6,rotation = 30)
        plt.xlabel('NAMES ---->')
        plt.ylabel('AMOUNT ---->')

        plt.grid(b = True, which = 'major', color = '#666666', linestyle = '-')
        plt.title('CUSTOMER vs AMOUNT graph')

    plt.show()
        
#==========================================================================================
#                                    CUSTOMER
#==========================================================================================
c_accno = 0

def customer():

    mycursor.execute('select * from bank_master')
    a = mycursor.fetchall()

    global c_accno
    
    title = "CUSTOMER ACCOUNT"
    fieldNames = ["ENTER YOUR NAME", "ENTER ID NO" ]

    #speak('Please Enter your name and ID Number')
    msg = "Enter The Required Informations"
    Values = multenterbox(msg, title, fieldNames)
    x = Values
    b = list(x)
    b[0]=b[0].upper()
    b[1]=int(b[1])
    w=0
 
    for i in range (len(a)):
        if w==0:
            if b[0]==a[i][1] and b[1]==a[i][0]:
                c_accno = b[1]
                easygui.msgbox('You Are Valid. . . !')
                time.sleep(2)            
                os.system('cls')
                customer_menu()
                w=1
            else:
                easygui.msgbox('You Are Not Valid. . . !')
                time.sleep(2)
                easygui.msgbox('You Are Not Our Bank Customer. . . !')
                time.sleep(2)
                easygui.msgbox('CLOSING APPLICATION. . . !')
                time.sleep(1)
                sys.exit()
        else:
            pass

        
            
def customer_menu():

    cprint('*'*167,'blue')
    print()
    text ="""
  ______  __    __       _______..___________.  ______   .___  ___.  _______ .______      
 /      ||  |  |  |     /       ||           | /  __  \  |   \/   | |   ____||   _  \     
|  ,----'|  |  |  |    |   (----``---|  |----`|  |  |  | |  \  /  | |  |__   |  |_)  |    
|  |     |  |  |  |     \   \        |  |     |  |  |  | |  |\/|  | |   __|  |      /     
|  `----.|  `--'  | .----)   |       |  |     |  `--'  | |  |  |  | |  |____ |  |\  \----.
 \______| \______/  |_______/        |__|      \______/  |__|  |__| |_______|| _| `._____|
                                                                                          
    """
    cprint(text,"cyan")

    speak("CUSTOMER MENU")

    cprint('\t\t\t\t\t\t\t\t\t\t\t\t\t\tCURRENT DATE & TIME :- {}'.format(time.asctime()),'red')
    speak(time.asctime())

    print()
    
    cprint('*'*167,'blue')

    cprint('''WHAT DO YOU WANT TO DO. . .
                
                1.VIEW AMOUNT 
                2.WITHDRAWAL/DEPOSIT
                3.LOGOUT
                4.CLOSE THE APPLICATION''','green')
    print()

    cprint('ENTER YOUR CHOICE :','yellow')

    c_input=input('>>>  ')

    if c_input == '1':
        
        mycursor.execute("select name,amount from bank_master where ID_NO='"+str(c_accno)+"'")
        result=mycursor.fetchall()
        easygui.msgbox(f'\t\t\tACCOUNT NO :-   {c_accno}\n\t\t\tNAME :-\t\t{result[0][0]}\n\t\t\tAMOUNT :-\t\t₹{result[0][1]}','YOUR AMOUNT','¤¤ DONE ¤¤')
        
    if c_input == '2':
        transaction()

    if c_input == '3':
        os.system('cls')
        main()

    if c_input == '4':
        time.sleep(2)
        sys.exit()


    
#------------------------------------------------------------------------------------------
#                                   TRANSACTION
#------------------------------------------------------------------------------------------
    
def transaction():

    c_accno = input("ENTER THE 'IDENTITY CARD NUMBER' FOR ACCOUNT VALIDATION :")
    
    version= 'TRANSACTIONS'
    options = ["  DEPOSIT MONEY  ","  WITHDRAW MONEY  "]
    button = buttonbox("\t\t\t\tWHAT YOU WANT TO DO :-",title = version,choices = options)
        
    if button == options[0]:

        dp = int(input("Enter Amount To Be Deposited:"))
        mycursor.execute("update bank_master set AMOUNT=AMOUNT+'"+str(dp)+"' where ID_NO='"+c_accno+"'")
        con.commit()
        
        mycursor.execute("select AMOUNT from bank_master where ID_NO='"+c_accno+"'")
        amount = mycursor.fetchall()
        easygui.msgbox('MONEY HAS BEEN DEPOSITED SUCCESSFULLY ! ! !\nYOU HAVE ₹ {} IN YOUR ACCOUNT'.format(amount[0][0]))
        

    
    if button == options[1]:

        wd = int(input("Enter amount to be withdrawn:"))
        mycursor.execute("update bank_master set AMOUNT=AMOUNT-'"+str(wd)+"' where ID_NO='"+c_accno+"'")
        con.commit()

        mycursor.execute("select AMOUNT from bank_master where ID_NO='"+c_accno+"'")
        amount = mycursor.fetchall()
        easygui.msgbox('MONEY HAS BEEN WITHDRAWN SUCCESSFULLY ! ! !\nYOU HAVE ₹ {} IN YOUR ACCOUNT'.format(amount[0][0]))

#------------------------------------------------------------------------------------------
#                                   DATA BACKUP
#------------------------------------------------------------------------------------------

def backup():

    f = open('backup.csv','w+')
    mycursor.execute('select * from bank_master')
    
    fetch_file = mycursor.fetchall()
    w = csv.writer(f)

    for row in fetch_file:

        w.writerow([str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7])])

    easygui.msgbox('DATA BACKED-UP SUCCESSFULLY. . . !')

#==========================================================================================
#                                       MAIN
#==========================================================================================

def admin_main():

    speak('PLEASE ENTER USER-NAME AND PASSWORD')
    admin()    

    while (input('DO YOU WANT TO CONTINUE AS ADMIN (Y/N) :').lower()) == 'y':

        os.system('cls')
        cprint('*'*167,'cyan')
        print()

        cprint('\t\t\t\t\t\t\t\tWelcome To Our PROTECHT  SYSTEM','green')
        print()
        cprint('*'*167,'cyan')

        print()
        admin_menu()

    else:
        easygui.msgbox("""EXITING ADMIN. . . !""")
        time.sleep(2)
        os.system('cls')
        main()
        
        
#------------------------------------------------------------------------------------------

def customer_main():

    text ="""
  ______  __    __       _______..___________.  ______   .___  ___.  _______ .______      
 /      ||  |  |  |     /       ||           | /  __  \  |   \/   | |   ____||   _  \     
|  ,----'|  |  |  |    |   (----``---|  |----`|  |  |  | |  \  /  | |  |__   |  |_)  |    
|  |     |  |  |  |     \   \        |  |     |  |  |  | |  |\/|  | |   __|  |      /     
|  `----.|  `--'  | .----)   |       |  |     |  `--'  | |  |  |  | |  |____ |  |\  \----.
 \______| \______/  |_______/        |__|      \______/  |__|  |__| |_______|| _| `._____|
                                                                                          
    """
    cprint(text,"cyan")

    customer()   

    while input('DO YOU WANT TO CONTINUE TO CUSTOMER MENU (Y/N) :').lower() == 'y':

        os.system('cls')
        customer_menu()

    else:
        easygui.msgbox("""THANK YOU FOR USING OUR SERVICE. . . !""")
        time.sleep(2)
        os.system('cls')
        main()

#==========================================================================================

def main():

    text = "WELCOME"    
    cprint(figlet_format(text, font="starwars"), "cyan")
    speak('welcome')
    time.sleep(2)
    os.system('cls')

    text = "BANKING"
    cprint(figlet_format(text, font="banner3-D"), "cyan")
    
    
    cprint('*'*167,'blue')
    
    print()
    print()
    
    cprint('\t\t\t\t\t\t\t WELCOME TO OUR PROTECHT SYSTEM','green', attrs=['bold'])

    cprint('''\t\t\t\t\t\t\t CREATED BY :- GANESH AND JAMES ROBIN RAJ''',
            'red', attrs=['blink'])

    cprint('*'*167,'blue')

    cprint('\t\t\t\tCURRENT DATE & TIME :- {}'.format(time.asctime()),'magenta')

    print('\t\t\t\tWHAT YOU WANT TO VIEW\n')
    cprint('\t\t\t\t1.ADMIN','yellow')
    cprint('\t\t\t\t2.CUSTOMER','green')
    cprint('\t\t\t\t3.ABOUT','cyan')
    cprint('\t\t\t\t4.CLOSE THE APPLICATION','red')
    print()
    
    cprint('ENTER YOUR CHOICE :','yellow')
    a=input('>>>  ')

    if a == '1':
        admin_main()
    
    elif a == '2':
        customer_main()

    elif a == '3':
        about()

    elif a == '4':
        easygui.msgbox("""THANK YOU. . . . .\nEXITING THE APPLICATION. . . !""")
        time.sleep(3)
        sys.exit()

    else:
        print('YOUR CHOICE IS OTHER THAN THE GIVEN CHOICES')
main()



