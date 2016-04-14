#! /usr/bin/env python

import subprocess, datetime, sys, struct
from twilio.rest import TwilioRestClient

account_sid = "xxxx"
auth_token = "xxxx"
client = TwilioRestClient(account_sid, auth_token)

class EST(datetime.tzinfo):
    def utcoffset(self, dt):
      return datetime.timedelta(hours=-4)

    def dst(self, dt):
        return datetime.timedelta(0)



# Main to Edit
def main():
	option1 = sys.argv[1]
	option2 = sys.argv[2]
	idk = str(datetime.datetime.now(EST()))

	pnumber = "+1"
	pnumber += option1

	textmsg = """DoorHub at 580 Commonwealth has sent you a temporary key! 
\nHours Active: """	
	textmsg += option2
	textmsg += "\n\nStarting at (EST): \n"
	textmsg += idk
	textmsg += "\n\nLink:\n"
	textmsg += "http://pi.kierk.co/cVepr0rR37821as12lk3/"
	

	message = client.messages.create(to=pnumber, from_="+17162001181", 
		body=textmsg)

#	fp = open( 'itworks.txt', 'w')
	#subprocess.call(['echo', idk, '>', 'itworks.txt'])
#	fp.write(option1)
#	fp.write('\t')
#	fp.write(option2)
#	fp.write('\t')
#	fp.write(idk)
#	fp.write('\n\n')

if __name__ == "__main__":
    main()
