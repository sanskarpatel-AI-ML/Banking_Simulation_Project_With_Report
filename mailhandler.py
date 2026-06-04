import gmail

mail_id = ''    #Gmail id
app_pwd = ''    #App Password of gmail

def send_openacn_email(to,name,acn,pasw):
    con = gmail.GMail(mail_id, app_pwd)
    text = f'''Hello,{name},
    We have Successfully opened your account with following credentials
    Account No = {acn}
    Password = {pasw}

    Kindly change your password on first login

    Thanks 
    ABC Bank
    Noida
'''
    msg = gmail.Message(to=to , text=text, subject='Account Opened')
    con.send(msg)


def send_closeacn_email(to,name,otp):
    con = gmail.GMail(mail_id, app_pwd)
    text = f'''Hello,{name},
    Here is the OTP to close Your Account 
    OTP = {otp}

    Kindly share with Bank Admin

    Thanks 
    ABC Bank
    Noida
'''
    msg = gmail.Message(to=to , text=text, subject='Account Closing OTP')
    con.send(msg)

def send_fp_otp_email(to,name,otp):
    con = gmail.GMail(mail_id, app_pwd)
    text = f'''Hello,{name},
    Here is the OTP to recover Your Password 
    OTP = {otp}

    Kindly share with Bank Admin

    Thanks 
    ABC Bank
    Noida
'''
    msg = gmail.Message(to=to , text=text, subject='Password Recover OTP')
    con.send(msg)
