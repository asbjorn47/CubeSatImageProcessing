import sys
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

MY_ADDRESS = 'asbjornmatthiashansen@gmail.com'
PASSWORD = '62776277'


def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def mail(direction, img):
    names, emails = get_contacts('contacts.txt')
    message_template = read_template('message.txt')

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()
        location = "43.6532° N, 79.3832° W"
        message = message_template.substitute(PERSON_NAME=name.title(),FIRE_DIRECTION=direction,FIRE_LOCATION=location)
        #fp = open('images/fire3.jpg', 'rb')
        #msgImage = MIMEImage(fp.read())
        #fp.close()
        #msgImage.add_header('Content-ID', '<image1>')
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="URGENT: Forest Fire Detected!"
        msg.attach(MIMEText(message, 'plain'))
        #msg.attach(msgImage)
        s.send_message(msg)
        del msg

    s.quit()
