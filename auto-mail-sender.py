import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'From name'
email['to'] = input("Enter email address seperated by commas: ")
email['Subject'] = 'Subject'

email.set_content("mail Body")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('username', 'password') #username is your gmail and password is your gmail password
    smtp.send_message(email)
    print('Email send successfully!!!!')
