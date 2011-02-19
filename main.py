#!/usr/bin/python2

import imaplib
import email
from connect import *

Mailbox = imaplib.IMAP4(imap_server)

# Init IMAP connection
Mailbox.login(username, password)
Mailbox.select()

res, messages = Mailbox.search(None, 'Subject', '**')

# Close IMAP connection
Mailbox.close()
