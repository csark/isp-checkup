#!/usr/bin/env python
#Setup.py
#Clark Hatch 2016
#
#Setup isp-checkup in one easy script

import re
import os
import sys

def definePath():
    f = open('scripts/isp_checkup.py', 'r+')
    output = ''
    for line in f:
        match = re.search(r'path_to_repo =',line)
        if match:
            path = os.popen('pwd').read().replace('\n','')
            output += 'path_to_repo = \'' + path + '\'\n'
        else:
            output += line

    f.seek(0)
    f.write(output)
    f.truncate()
    f.close()

def defineCron():
    path = os.popen('pwd').read().replace('\n','')
    tmp = os.popen('crontab -l > tmpfile; echo "*/10 * * * * /usr/bin/python ' + path + '/scripts/isp_checkup.py" >> tmpfile; crontab tmpfile; rm tmpfile').read()

def runHttpServer():
    if sys.version_info[0] < 3:
        print("\nActions taken:")
        print("-Set default path in isp_checkup.py")
        print("-Created a cron job to check internet speeds every 10 minutes")
        print("\nAll that is left do to:")
        print("-As sudo run this command 'python -m SimpleHTTPServer 80 >> logs/pyHTTP.log &; disown'")
        #print("\tand then 'disown'")


def setup():
    definePath()
    defineCron()
    runHttpServer()

if __name__ == '__main__':
    setup()
