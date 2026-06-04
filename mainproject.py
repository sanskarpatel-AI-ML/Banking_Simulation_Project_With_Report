from tkinter import Tk, Label, Frame, Entry, Button, messagebox, simpledialog,filedialog
from tkinter.ttk import Combobox
import random
import mygenerator
import dbhandler
import mailhandler
import time
import sqlite3
from PIL import Image, ImageTk
import shutil
import os
import re

def update_time():
    t = time.strftime("%A,%b %d %Y ⏰%r")
    lbl_dt.configure(text=t)
    lbl_dt.after(1000,update_time)

def customer_screen():
    frm = Frame(root, highlightbackground='black', highlightthickness=1)
    frm.configure(bg='powder blue')
    frm.place(relx=0, rely=.17, relwidth=1, relheight=.78)

    def logout_click():
        frm.destroy()
        main_screen()

    def viewdetail_screen():
        ifrm = Frame(frm, highlightbackground='black', highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2, rely=.2, relwidth=.73, relheight=.7)

        lbl_ititle = Label(ifrm, text="This is View Details Screen",
                  font=('arial',20,'bold'), bg='White', fg='purple')
        lbl_ititle.pack(pady=.05)

        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query = 'select * from users where acn = ?'
        curobj.execute(query, (user_acn))
        row = curobj.fetchone()
        conobj.close()
        details = f'''Name = {row[1]}
        ACN = {row[0]}
        Bal = {row[7]}
        Open Date = {row[9]}'''

        lbl_details = Label(ifrm, text=details,
                  font=('arial',20,'bold'), bg='White', fg='blue')
        lbl_details.place(x=200, y=100)

    def updatedetail_screen():
        ifrm = Frame(frm, highlightbackground='black', highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2, rely=.2, relwidth=.73, relheight=.7)

        def up_details():
            name = e_name.get()
            email = e_email.get()
            mob = e_mob.get()
            pasw = e_pasw.get()

            conobj = sqlite3.connect(database='bank.sqlite')
            curobj = conobj.cursor()
            query = 'update users set name=?, email=?, mob=?, pass=? where acn =?'
            curobj.execute(query, (name,email,mob,pasw,user_acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update Details", "Details are updated")
            customer_screen()

        lbl_ititle = Label(ifrm, text="This is Update Details Screen",
                  font=('arial',20,'bold'), bg='White', fg='purple')
        lbl_ititle.pack(pady=.05)

        lbl_name = Label(ifrm, text="Name",
                  font=('arial',20,'bold'), bg='white')
        lbl_name.place(relx=.1, rely=.12)

        e_name = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_name.place(relx=.1, rely=.2)

        lbl_email = Label(ifrm, text="Email",
                  font=('arial',20,'bold'), bg='white')
        lbl_email.place(relx=.1, rely=.32)

        e_email = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_email.place(relx=.1, rely=.40)

        lbl_mob = Label(ifrm, text="Mob No.",
                  font=('arial',20,'bold'), bg='white')
        lbl_mob.place(relx=.6, rely=.12)

        e_mob = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_mob.place(relx=.6, rely=.2)

        lbl_pasw = Label(ifrm, text="Pass",
                  font=('arial',20,'bold'), bg='white')
        lbl_pasw.place(relx=.6, rely=.32)

        e_pasw = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_pasw.place(relx=.6, rely=.40)

        up_btn = Button(frm, text="Update", bd=2,command=up_details,
                    font=('arial',20,'bold'), bg='grey')
        up_btn.place(relx=.5, rely=.65)

        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query = 'select name, email, mob, pass from users where acn = ?'
        curobj.execute(query, (user_acn))
        tup = curobj.fetchone()
        conobj.close()

        e_name.insert(0, tup[0])
        e_email.insert(0, tup[1])
        e_mob.insert(0, tup[2])
        e_pasw.insert(0, tup[3])



    def deposit_screen():
        ifrm = Frame(frm, highlightbackground='black', highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2, rely=.2, relwidth=.73, relheight=.7)

        lbl_ititle = Label(ifrm, text="This is Deposit Screen",
                  font=('arial',20,'bold'), bg='White', fg='purple')
        lbl_ititle.pack(pady=.05)

        amt = simpledialog.askfloat("Deposit", "Enter Amount")
        if amt == None:
            return
        
        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query = 'update users set bal=bal+?where acn =?'
        curobj.execute(query, (amt,user_acn))
        conobj.commit()
        conobj.close()
        messagebox.showinfo("Deposit", "Amount Deposited")

    def withdraw_screen():
        ifrm = Frame(frm, highlightbackground='black', highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2, rely=.2, relwidth=.73, relheight=.7)

        lbl_ititle = Label(ifrm, text="This is Withdraw Screen",
                  font=('arial',20,'bold'), bg='White', fg='purple')
        lbl_ititle.pack(pady=.05)

        amt = simpledialog.askfloat("Withdraw Amount", "Enter Amount")
        if amt == None:
            return
        
        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query = 'select bal from users where acn =?'
        curobj.execute(query, (user_acn,))
        bal = curobj.fetchone()[0]
        conobj.close()
        
        if amt > bal:
             messagebox.showerror("Withdraw", "Insufficient Fund")
             return

        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query = 'update users set bal=bal-?where acn =?'
        curobj.execute(query, (amt,user_acn))
        conobj.commit()
        conobj.close()
        messagebox.showinfo("Withdraw", "Amount Withdrawn")


    def Transfer_screen():
        ifrm = Frame(frm, highlightbackground='black', highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2, rely=.2, relwidth=.73, relheight=.7)

        lbl_ititle = Label(ifrm, text="This is Transfer Screen",
                  font=('arial',20,'bold'), bg='White', fg='purple')
        lbl_ititle.pack(pady=.05)
        
        to_acn = simpledialog.askfloat("Transfer Amount", "Enter To ACN")
        if to_acn == None:
            return

        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query = 'select * from users where acn =?'
        curobj.execute(query, (to_acn,))
        row = curobj.fetchone()
        conobj.close()
        if row == None:
            messagebox.showerror("Transfer Account", "To Acn ACN does not Exist")
            return
        
        amt = simpledialog.askfloat("Withdraw Amount", "Enter Amount")
        if amt == None:
            return
        
        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query = 'select bal from users where acn =?'
        curobj.execute(query, (user_acn,))
        bal = curobj.fetchone()[0]
        conobj.close()
        
        if amt > bal:
             messagebox.showerror("Transfer Amount", "Insufficient Fund")
             return

        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query1 = 'update users set bal=bal-? where acn =?'
        query2 = 'update users set bal=bal+? where acn =?'

        curobj.execute(query1, (amt,user_acn))
        curobj.execute(query2, (amt,to_acn)) 

        conobj.commit()
        conobj.close()
        messagebox.showinfo("Transfer Amount", f"{amt} Amount Transfered to ACN {to_acn} from ACN {user_acn} ")

    def dp():
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        shutil.copy(filepath, f'{user_acn}.jpg')

        imgc = Image.open(f'{user_acn}.jpg').resize((200,180))
        imgctk = ImageTk.PhotoImage(imgc, master=root)
        dp_lbl = Label(frm, image=imgctk)
        dp_lbl.image=imgctk
        dp_lbl.place(relx=.01, rely=.05)

    logout_btn = Button(frm, text="logout", bd=2,
                    font=('arial',20,'bold'), bg='grey', command=logout_click)
    logout_btn.place(relx=.93, rely=0)

    conobj = sqlite3.connect(database='bank.sqlite')
    curobj = conobj.cursor()
    query = 'select name from users where acn =?'
    curobj.execute(query, user_acn)
    name = curobj.fetchone()[0]
    conobj.close()

    lbl_wel = Label(frm, text=f"Welcome, {name}",
                  font=('arial',20,'bold'), bg='powder blue')
    lbl_wel.place(relx=0, rely=0)

    if os.path.exists(f'{user_acn}.jpg'):
        filepath = f'{user_acn}.jpg'
    else:
        filepath = 'default.jpg'
    imgc = Image.open(filepath).resize((200,180))
    imgctk = ImageTk.PhotoImage(imgc, master=root)
    dp_lbl = Label(frm, image=imgctk)
    dp_lbl.image=imgctk
    dp_lbl.place(relx=.01, rely=.05)

    updatedp_btn = Button(frm, text="Update Photo", bd=2,command=dp,
                    font=('arial',10,'bold'), bg='white')
    updatedp_btn.place(relx=.05, rely=.34)

    view_btn = Button(frm, text="View Details", bd=5, width=15,
                    font=('arial',18,'bold'), bg='yellow', fg='white', command=viewdetail_screen)
    view_btn.place(relx=0, rely=.4)

    update_btn = Button(frm, text="Update Details", bd=5, width=15,
                    font=('arial',18,'bold'), bg='green', fg='white', command=updatedetail_screen)
    update_btn.place(relx=0, rely=.5)

    deps_btn = Button(frm, text="Deposit", bd=5, width=15,
                    font=('arial',18,'bold'), bg='purple', fg='white', command=deposit_screen)
    deps_btn.place(relx=0, rely=.6)

    witd_btn = Button(frm, text="Withdraw", bd=5, width=15,
                    font=('arial',18,'bold'), bg='blue', fg='white', command=withdraw_screen)
    witd_btn.place(relx=0, rely=.7)

    trans_btn = Button(frm, text="Transfer", bd=5, width=15,
                    font=('arial',18,'bold'), bg='brown', fg='white', command=Transfer_screen)
    trans_btn.place(relx=0, rely=.8)

    lbl_footer = Label(frm, text="© 2026 ABC Bank | Secure Banking Solutions ",
                  font=('Calibri',20), bg='powder blue', fg='Navy Blue')
    lbl_footer.pack(side='bottom', pady=5)


def admin_screen():
    frm = Frame(root, highlightbackground='black', highlightthickness=1)
    frm.configure(bg='powder blue')
    frm.place(relx=0, rely=.17, relwidth=1, relheight=.78)

    def logout_click():
        frm.destroy()
        main_screen()

    def openacn_screen():
        ifrm = Frame(frm, highlightbackground='black', highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.15, rely=.17, relwidth=.73, relheight=.7)

        def reset():
            e_name.delete(0,'end')
            e_email.delete(0,'end')
            e_mob.delete(0,'end')
            e_adhar.delete(0,'end')
            e_age.delete(0,'end')
            cb_gender.current(0)

        def create_acn():
            name = e_name.get()
            email = e_email.get()
            adhar = e_adhar.get()
            mob = e_mob.get()
            age = e_age.get()
            gender = cb_gender.get()

            if len(name) == 0:
                messagebox.showerror("Open Account", "Name is required")
                return
            if len(email) == 0:
                messagebox.showerror("Open Account", "Email is required")
                return
            
            match = re.fullmatch(r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+",email)
            if match == None:
                messagebox.showerror("Open Account", "Invalid Email")
                return
            
            if len(mob) == 0:
                messagebox.showerror("Open Account", "Mob is required")
                return
            match = re.fullmatch(r"[6-9]\d{9}", mob)
            if match == None:
                messagebox.showerror("Open Account", "Invalid Mob")
                return
            
            if len(adhar) == 0:
                messagebox.showerror("Open Account", "Adhaar is required")
                return
            
            if len(age) == 0:
                messagebox.showerror("Open Account", "age is required")
                return
            
            bal = 0
            opendate = time.strftime("%d-%m-%Y %r")
            pasw = mygenerator.generate_password()

            conobj = sqlite3.connect(database='bank.sqlite')
            curobj = conobj.cursor()
            query = 'insert into users values(null,?,?,?,?,?,?,?,?,?)'
            curobj.execute(query,(name,pasw,email,mob,adhar,age,bal,gender,opendate))
            conobj.commit()
            conobj.close()

            conobj = sqlite3.connect(database='bank.sqlite')
            curobj = conobj.cursor()
            query = 'select max(acn) from users'
            curobj.execute(query)
            acn = curobj.fetchone()[0]
            conobj.close()
            mailhandler.send_openacn_email(email,name,acn,pasw)

            messagebox.showinfo('Create Account', "Account Opened and Credentials are sent to email")

        lbl_ititle = Label(ifrm, text="This is Open Account Screen",
                  font=('arial',20,'bold'), bg='White', fg='purple')
        lbl_ititle.pack(pady=.05)

        lbl_name = Label(ifrm, text="Name",
                  font=('arial',20,'bold'), bg='white')
        lbl_name.place(relx=.1, rely=.12)

        e_name = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_name.place(relx=.1, rely=.2)

        lbl_email = Label(ifrm, text="Email",
                  font=('arial',20,'bold'), bg='white')
        lbl_email.place(relx=.1, rely=.32)

        e_email = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_email.place(relx=.1, rely=.40)

        lbl_mob = Label(ifrm, text="Mob No.",
                  font=('arial',20,'bold'), bg='white')
        lbl_mob.place(relx=.1, rely=.52)

        e_mob = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_mob.place(relx=.1, rely=.6)

        lbl_adhar = Label(ifrm, text="Aadhar",
                  font=('arial',20,'bold'), bg='white')
        lbl_adhar.place(relx=.6, rely=.12)

        e_adhar = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_adhar.place(relx=.6, rely=.2)

        lbl_age = Label(ifrm, text="Age",
                  font=('arial',20,'bold'), bg='white')
        lbl_age.place(relx=.6, rely=.32)

        e_age = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_age.place(relx=.6, rely=.40)

        lbl_gender = Label(ifrm, text="Gender",
                  font=('arial',20,'bold'), bg='white')
        lbl_gender.place(relx=.6, rely=.52)

        cb_gender = Combobox(ifrm, values=['Male','Female','Others'],
                            font=('arial',19,'bold'))
        cb_gender.current(0)
        cb_gender.place(relx=.6, rely=.6)

        submit_btn = Button(ifrm, text="Submit", bd=5,command=create_acn,
                       font=('arial',20,'bold'), bg='blue', fg='white')
        submit_btn.place(relx=.35, rely=.8)

        reset_btn = Button(ifrm, text="Reset", bd=5, command=reset,
                           font=('arial',20,'bold'), bg='blue', fg='white')
        reset_btn.place(relx=.55, rely=.8)

    def viewacn_screen():
        ifrm = Frame(frm, highlightbackground='black', highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.15, rely=.17, relwidth=.73, relheight=.7)

        def search():
            acn = int(e_acn.get())
            conobj = sqlite3.connect(database='bank.sqlite')
            curobj = conobj.cursor()
            query = 'select name, bal, opendate, email, adhar from users where acn =?'
            curobj.execute(query,(acn,))
            row = curobj.fetchone()
            conobj.close()
            if row == None:
                messagebox.showerror('search', "Account doesn't exits")
            else:
                #messagebox.showinfo('Account Details', row)
                details = f'''              Name = {row[0]}

                Bal = {row[1]}
                
                Open date = {row[2]}
                
                Email = {row[3]}'''
                messagebox.showinfo('Account Details', details) 

        lbl_ititle = Label(ifrm, text="This is View Account Screen",
                  font=('arial',20,'bold'), bg='White', fg='purple')
        lbl_ititle.pack(pady=.05)

        lbl_acn = Label(ifrm, text="ACN",
                  font=('arial',20,'bold'), bg='white')
        lbl_acn.place(relx=.25, rely=.1)

        e_acn = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_acn.place(relx=.35, rely=.1)

        search_btn = Button(ifrm, text="Search", bd=3, command=search,
                            font=('arial',15), bg='green', fg='white')
        search_btn.place(relx=.65, rely=.1)

    def closeacn_screen():
        ifrm = Frame(frm, highlightbackground='black', highlightthickness=1)
        ifrm.configure(bg='white')
        ifrm.place(relx=.15, rely=.17, relwidth=.73, relheight=.7)

        def close():
            acn = int(e_acn.get())
            conobj = sqlite3.connect(database='bank.sqlite')
            curobj = conobj.cursor()
            query = 'select name, email from users where acn =?'
            curobj.execute(query,(acn,))
            row = curobj.fetchone()
            conobj.close()
            if row == None:
                messagebox.showerror('Close Account', "Account doesn't exist")
            else:
                gen_otp = random.randint(1000,9999)
                mailhandler.send_closeacn_email(row[1], row[0],gen_otp)
                user_otp =simpledialog.askinteger('Close Account', "Enter OTP")
                if user_otp == gen_otp:
                    conobj = sqlite3.connect(database='bank.sqlite')
                    curobj = conobj.cursor()
                    query = 'delete from users where acn=?'
                    curobj.execute(query,(acn,))
                    conobj.commit()
                    conobj.close()
                    messagebox.showinfo('Close Account', "Account Closed")
                else:
                    messagebox.showwarning('Close Account', "Invalid OTP")

        lbl_ititle = Label(ifrm, text="This is Close Account Screen",
                  font=('arial',20,'bold'), bg='White', fg='purple')
        lbl_ititle.pack(pady=.05)

        lbl_acn = Label(ifrm, text="ACN",
                  font=('arial',20,'bold'), bg='white')
        lbl_acn.place(relx=.25, rely=.1)

        e_acn = Entry(ifrm, font=('arial',20,'bold'), bd=5)
        e_acn.place(relx=.35, rely=.1)

        close_btn = Button(ifrm, text="Close", bd=3, command=close,
                            font=('arial',15), bg='red', fg='white')
        close_btn.place(relx=.65, rely=.1)

    logout_btn = Button(frm, text="logout", bd=2,
                    font=('arial',20,'bold'), bg='grey', command=logout_click)
    logout_btn.place(relx=.93, rely=0)

    lbl_wel = Label(frm, text="Welcome.., Admin",
                  font=('arial',20,'bold'), bg='powder blue')
    lbl_wel.place(relx=0, rely=0)

    open_acn_btn = Button(frm, text="Open Account", bd=5,
                    font=('arial',18,'bold'), bg='blue', fg='white', command=openacn_screen)
    open_acn_btn.place(relx=.15, rely=.06)

    view_acn_btn = Button(frm, text="View Account", bd=5,
                    font=('arial',18,'bold'), bg='green', fg='white', command=viewacn_screen)
    view_acn_btn.place(relx=.45, rely=.06)

    close_acn_btn = Button(frm, text="Close Account", bd=5,
                    font=('arial',18,'bold'), bg='red', fg='white', command=closeacn_screen)
    close_acn_btn.place(relx=.75, rely=.06)

    lbl_footer = Label(frm, text="© 2026 ABC Bank | Secure Banking Solutions ",
                  font=('Calibri',20), bg='powder blue', fg='Navy Blue')
    lbl_footer.pack(side='bottom', pady=5)

def fp_screen():
    frm = Frame(root, highlightbackground='black', highlightthickness=1)
    frm.configure(bg='powder blue')
    frm.place(relx=0, rely=.17, relwidth=1, relheight=.78)

    def back_click():
        frm.destroy()
        main_screen()

    def fp_otp():
        user_acn = e_acn.get()
        user_email = e_email.get()

        conobj = sqlite3.connect(database='bank.sqlite')
        curobj = conobj.cursor()
        query = 'select name, pass from users where acn=? and email=?'
        curobj.execute(query,(user_acn,user_email))
        tup = curobj.fetchone()
        conobj.close()
        
        if tup == None:
            messagebox.showerror('forgot password', "ACN does not exist")
            return
        
        gen_otp = random.randint(1000,9999)
        mailhandler.send_fp_otp_email(user_email,tup[0],gen_otp)
        user_otp = simpledialog.askinteger('Forgot password', "OTP")
        if user_otp == None:
            return
        if gen_otp == user_otp:
            messagebox.showinfo('Forgot Password', f'Your Pass = {tup[1]}')

    back_btn = Button(frm, text="Back", bd=5,
                    font=('arial',10,'bold'), bg='grey', command=back_click)
    back_btn.place(relx=0, rely=0)

    lbl_acn = Label(frm, text="User ACN",
                  font=('arial',20,'bold'), bg='powder blue')
    lbl_acn.place(relx=.3, rely=.2)

    e_acn = Entry(frm, font=('arial',20,'bold'), bd=5)
    e_acn.place(relx=.45, rely=.2)

    lbl_email = Label(frm, text="User Email",
                  font=('arial',20,'bold'), bg='powder blue')
    lbl_email.place(relx=.3, rely=.3)

    e_email = Entry(frm, font=('arial',20,'bold'), bd=5)
    e_email.place(relx=.45, rely=.3)

    otp_btn = Button(frm, text="Validate & Send OTP", bd=5,
                    font=('arial',20,'bold'), bg='pink',command=fp_otp)
    otp_btn.place(relx=.45, rely=.4)

    lbl_footer = Label(frm, text="© 2026 ABC Bank | Secure Banking Solutions ",
                  font=('Calibri',20), bg='powder blue', fg='Navy Blue')
    lbl_footer.pack(side='bottom', pady= 5)

def main_screen():
    frm = Frame(root, highlightbackground='black', highlightthickness=.5)
    frm.configure(bg='gold')
    frm.place(relx=0, rely=.17, relwidth=1, relheight=.78)

    def fp_click():
        frm.destroy()
        fp_screen()

    def reset():
        e_acn.delete(0, 'end')
        e_pasw.delete(0, 'end')
        e_capt.delete(0, 'end')
        cb_user.current(0)

    def login_click():
        global user_acn
        user_type = cb_user.get()
        user_acn = e_acn.get()
        user_pasw = e_pasw.get()
        user_captcha = e_capt.get()
        if user_type == "Admin" and user_acn == '0' and user_pasw =="Admin" and user_captcha == captcha.replace('  ',''):
            frm.destroy()
            admin_screen()
        elif user_type == "Customer" and user_captcha == captcha.replace('  ',''):
            conobj = sqlite3.connect(database='bank.sqlite')
            curobj = conobj.cursor()
            query = 'select * from users where acn =? and pass=?'
            curobj.execute(query,(user_acn,user_pasw))
            row = curobj.fetchone()
            conobj.close()
            if row == None:
                messagebox.showerror("Login", "Invalid ACN/Pasw")
            else:
                frm.destroy()
                customer_screen()
        else:
            messagebox.showerror("User Type", "Invalid credentials")

    lbl_user = Label(frm, text="User Type",
                  font=('arial',20,'bold'), bg='Gold')
    lbl_user.place(relx=.3, rely=.1)

    cb_user = Combobox(frm, values=['--Select--','Admin','Customer'],
                       font=('arial',20,'bold'))
    cb_user.current(0)
    cb_user.config(state='readonly')
    cb_user.place(relx=.45, rely=.1)

    lbl_acn = Label(frm, text="User ACN",
                  font=('arial',20,'bold'), bg='Gold')
    lbl_acn.place(relx=.3, rely=.2)

    e_acn = Entry(frm, font=('arial',20,'bold'), bd=5)
    e_acn.place(relx=.45, rely=.2)

    lbl_pasw = Label(frm, text="User Pass",
                  font=('arial',20,'bold'), bg='Gold')
    lbl_pasw.place(relx=.3, rely=.3)

    e_pasw = Entry(frm, font=('arial',20,'bold'), bd=5, show='*')
    e_pasw.place(relx=.45, rely=.3)

    captcha = mygenerator.generate_captcha()

    lbl_show_capt = Label(frm, text=captcha,
                  font=('Segoe Print Bold',20,'bold'), bg='white', fg='royal blue', width=10)
    lbl_show_capt.place(relx=.5, rely=.4)

    def refresh_captcha():
        nonlocal captcha
        captcha = mygenerator.generate_captcha()
        lbl_show_capt.configure(text=captcha)

    ref_btn = Button(frm, text="refresh", bd=5, font=('arial',10), command=refresh_captcha)
    ref_btn.place(relx=.62, rely=.4)

    lbl_capt = Label(frm, text="Captcha",
                  font=('arial',20,'bold'), bg='Gold')
    lbl_capt.place(relx=.3, rely=.5)

    e_capt = Entry(frm, font=('arial',20,'bold'), bd=5)
    e_capt.place(relx=.45, rely=.5)
   
    login_btn = Button(frm, text="LOGIN", bd=5,command=login_click,
                       font=('arial',20,'bold'), bg='navy blue', fg='gold')
    login_btn.place(relx=.46, rely=.6)

    reset_btn = Button(frm, text="RESET", bd=5,command=reset,
                        font=('arial',20,), bg='pink')
    reset_btn.place(relx=.57, rely=.6)

    fp_btn = Button(frm, text="Forgot Password..?", command=fp_click,
                    font=('arial',20,), bg='grey')
    fp_btn.place(relx=.47, rely=.72)


root = Tk()
root.state('zoomed')
root.configure(bg='white')
root.resizable(width=False, height=False)

lbl_title = Label(root, text="BANKING SIMULATION",
                  font=('Brevis',50), bg='white',fg='Navy Blue')
lbl_title.pack()

lbl_dt = Label(root, text=time.strftime("%A,%b %d %Y ⏰%r"),
               font=('arial',20,'bold'), bg='white', fg='Royal blue')
lbl_dt.pack(pady=10)

update_time()

img = Image.open('ABC_bank_logo.png').resize((250,150))
imgtk = ImageTk.PhotoImage(img, master=root)

lbl_bank_logo = Label(root, image=imgtk, bg='white')
lbl_bank_logo.place(relx=0, rely=0)

img2 = Image.open('rbi_logo.png').resize((200,150))
imgtk2 = ImageTk.PhotoImage(img2, master=root)

lbl_rbi_logo = Label(root, image=imgtk2, bg='white')
lbl_rbi_logo.place(relx=.85, rely=0)


lbl_footer = Label(root, text="Developed by SANSKAR PATEL",
                  font=('Calibri',20), bg='white', fg='Navy Blue')
lbl_footer.pack(side='bottom')

main_screen()

root.mainloop()