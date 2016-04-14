#! /usr/bin/env python

#------------------------------------------------------------
#       Script to send text messages
#
#
#------------------------------------------------------------

import struct
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "xxxx"
auth_token = "xxxx"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+17168301181", from_="+17162001181",
                                     body="MSG FROM DOORHUB - ALERT, UNSCHEDULED ENTRY        TO APARTMENT! REPLY 'ALARM' to sound alarm. Do not reply if this entry is expected.")
