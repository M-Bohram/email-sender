from dotenv import load_dotenv
import os

load_dotenv()

configs = {
    'address': os.environ.get('MY_ADDRESS'),
    'password': os.environ.get('MY_PASSWORD'),
    'host': os.environ.get('SMTP_HOST'),
    'port': os.environ.get('SMTP_PORT'),
    'contacts_file': 'contacts.txt',
    'message_file': 'message.txt',
    'subject': 'Test Email'
}