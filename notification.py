import sys
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

MY_ADDRESS = 'asbjornmatthiashansen@gmail.com'
PASSWORD = '62776277'


def get_contacts(filename):#function to read recipients from contacts list
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:#opens contact file
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])#extract name
            emails.append(a_contact.split()[1])#extract email
    return names, emails

def read_template(filename):#Function to read email template
    with open(filename, 'r', encoding='utf-8') as template_file:#opens template
        template_file_content = template_file.read()#extracts template
    return Template(template_file_content)

def mail(direction):#function to send email
    names, emails = get_contacts('contacts.txt')
    message_template = read_template('message.txt')

    s = smtplib.SMTP(host='smtp.gmail.com', port=587) #create SMPT server object
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)#connect to googles SMTP server

    for name, email in zip(names, emails):
        msg = MIMEMultipart()
        location = "43.6532° N, 79.3832° W"#filler for fire location
        message = message_template.substitute(PERSON_NAME=name.title(),FIRE_DIRECTION=direction,FIRE_LOCATION=location)#add template to message object and insert direction and name
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="URGENT: Forest Fire Detected!"
        msg.attach(MIMEText(message, 'plain'))#attach sender email,recipient email, subject, and message body to email
        s.send_message(msg)#sends email
        del msg#clears msg object

    s.quit()#closes SMTP server connection
