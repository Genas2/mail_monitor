#!/usr/bin/python2

import imaplib, email
import re, sys
from connect import *

Mailbox = imaplib.IMAP4(imap_server)

# Init IMAP connection
try:
    Mailbox.login(username, password)
except:
    sys.exc_info()
    raise

Mailbox.select()

res, messages = Mailbox.search(None, 'Subject', '**')

try:
    for num in messages[0].split():
        res, message = Mailbox.fetch(num, '(RFC822)')
        message_body = message[0][1]
    
        mail = email.message_from_string(message_body)
        subject = mail['Subject']

        if re.match('\*\*[ ]+PROBLEM', subject):
            print(mail['Subject'])
 
except (KeyboardInterrupt, SystemExit):
    # Close IMAP connection
    Mailbox.close()
    raise
