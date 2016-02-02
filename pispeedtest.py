#!/usr/bin/python
import os
import sys
import json
import datetime
import time

def test():

    #run speedtest-cli
    print 'Test Running....'
    a = os.popen("python speedtest_cli.py --simple").read()
    print 'Test Complete'
    #split the 3 line result (ping,down,up)
    lines = a.split('\n')
    #print a
    ts = time.time()
    date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    #if speedtest could not connect set the speeds to 0
    if "Cannot" in a:
            p = 100
            d = 0
            u = 0
    #extract the values for ping down and up values
    else:
            p = lines[0][6:11]
            d = lines[1][10:14]
            u = lines[2][8:12]
    update = {date: { 'ping': p, 'download': d, 'upload': u}}
    #save the data to file for local network plotting

    with open('data.json','r') as f:
        dic = json.load(f)
        f.close()
        dic.update(update)
        wf = open('data.json','w')
        json.dump(dic, wf)

    return

if __name__ == '__main__':
    test()
