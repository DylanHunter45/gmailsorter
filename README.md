#Gmail Email Mover
This script allows you to move emails from your Gmail account based on a mapping defined in a JSON file. The mapping specifies the sender's email address and the corresponding label. The script uses IMAP to interact with Gmail.

#Features:
Move emails to specified. 
Works across all folders, not just the Inbox (e.g., Sent, Trash, etc.).
Supports user-specific credentials through environment variables.
Requirements:
Python 3.x
Install the required Python packages via pip:
imaplib (part of Python standard library)
json (part of Python standard library)
python-dotenv (for reading credentials from the .env file)
Install dependencies:
pip install python-dotenv
Setup Instructions:
Step 1: Set Up Gmail IMAP Access
Enable IMAP in your Gmail account:

Go to Gmail settings.
In the "Forwarding and POP/IMAP" tab, make sure "IMAP access" is enabled.
Create an App-Specific Password (for accounts with 2-Factor Authentication enabled):

Visit Google App Passwords.
Create a new app password for your Gmail account (select "Mail" as the app and "Other" for the device).
Save this password for later use.
Step 2: Create a .env File for Gmail Credentials
Create a .env file in the root of your project directory and add your Gmail credentials:

GMAIL_USERNAME=your_email@gmail.com
GMAIL_PASSWORD=your_app_password
Replace your_email@gmail.com with your actual Gmail address and your_app_password with the app-specific password if you have 2FA enabled.

Step 3: Create a labels.json File
Create a labels.json file that maps email addresses to Gmail labels or specify "delete" to delete emails. The structure of the JSON file is as follows:

{
    "email.address@example.com": "Personal/Trash",
    "another.email@example.com": "Work/ProjectA",
    "third.email@example.com": "delete",
    "fourth.email@example.com": "Social/Newsletter"
}
"email.address@example.com": "Personal/Trash" will move emails from email.address@example.com to the Personal/Trash label.
"third.email@example.com": "delete" will delete emails from third.email@example.com.
The script will loop through all mappings and apply the corresponding actions.
Step 4: Run the Script
Run the Python script to move or delete emails:

python email_mover.py

The script will:

Search for emails from the email addresses in labels.json.
Apply the appropriate label (or delete) based on the mapping.
The script will process emails from all folders (Inbox, Sent, etc.) by selecting [Gmail]/All Mail in Gmail.
Example of Script Execution:
bash
Copy
$ python email_mover.py
Moved 5 emails from email.address@example.com to label Personal/Trash
Moved 3 emails from another.email@example.com to label Work/ProjectA
Deleted 2 emails from third.email@example.com
Moved 4 emails from fourth.email@example.com to label Social/Newsletter
Troubleshooting:
IMAP LOGIN FAILED or NO [AUTH]:
Make sure IMAP is enabled in your Gmail settings.
Double-check your Gmail credentials and ensure you're using an app-specific password if you have 2FA enabled.
Permission Denied Error:
Check the file permissions for the .env and labels.json files.
Ensure your Gmail account is accessible via IMAP (no restrictions).
License:
This project is licensed under the MIT License.
