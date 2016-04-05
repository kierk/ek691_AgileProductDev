#! /usr/bin/env python

import subprocess, datetime, sys

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
	fp = open( 'itworks.txt', 'w')
	#subprocess.call(['echo', idk, '>', 'itworks.txt'])
	fp.write(option1)
	fp.write('\t')
	fp.write(option2)
	fp.write('\t')
	fp.write(idk)
	fp.write('\n\n')

if __name__ == "__main__":
    main()
