# Automating Sending Emails

This is a project to automate sending emails to different users with the same content and subject and different names and emails.

## Setup

After cloning this project, follow the below steps:

1. create virtual environment, one way is using virtualenv `pip install virtualenv` then run `virtualenv .venv`
2. activate the virtual environment `source .venv/Scripts/activate` "Windows", for Linux/MacOS, run `source .venv/bin/activate`
3. add the users names and emails in `contacts.txt` file
4. change the content of the message in `message.txt` file
5. rename the `.env.example` file to `.env`
6. add your specific data "SMTP server and Email info"
7. install the dependencies `pip install -r requirements.txt`
8. after the above changes, execute the script `python app.py`
