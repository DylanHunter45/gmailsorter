import os
import imaplib
import json
import email
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def connect_to_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    return mail

def load_json(path):
    email_json = ""
    try:
        with open(f"{path}", "r") as f:
            email_json = json.load(f)
    except:
        print("Cannot load json file, make sure file exists and correct path is given")
    finally:
        return email_json
        
def move_emails(email_json, mail_session):
    email_count = 0
    if not email_json:
        print("Empty or invalid entries in mapping json")
        return
    try:
        for email_address, label in email_json.items():
            status, messages = mail_session.search(None, f'FROM "({email_address})"')
            if status == "OK":
                email_ids = messages[0].split()
                for email_id in email_ids:
                    mail_session.store(email_id, "+X-GM-LABELS", label)
                    mail_session.store(email_id, "+FLAGS", '\\Deleted')
                    email_count += 1
                    print(f'${email_count}: Moved email from {email_address} to {label}')
            else:
                print("Something went wrong with email session")
    except Exception as error:
        print(error.with_traceback)
    finally:
        mail_session.expunge()
        mail_session.logout()

def main():
    mail_session = connect_to_mail()
    email_json = load_json(path="./email_mapping.json")
    move_emails(email_json=email_json, mail_session=mail_session)

if __name__ == "__main__":
    main()