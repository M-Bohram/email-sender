from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils import get_contacts, read_template, setup_smtp
from config import configs

names, emails = get_contacts('contacts.txt')  # read contacts
content_template = read_template(configs['message_file'])

for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    content = content_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From'] = configs['address']
    msg['To'] = email
    msg['Subject'] = "This is TEST"

    # add in the message body
    msg.attach(MIMEText(content, 'plain'))

    # send the message via the server set up earlier.
    session = setup_smtp(
        host=configs['host'],
        port=configs['port'],
        address=configs['address'],
        password=configs['password']
    )

    session.send_message(msg)
    
    del msg