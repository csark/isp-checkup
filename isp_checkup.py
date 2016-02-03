#!/usr/bin/env python

import os
import sys
import json
import datetime
import time

def test():

    #run speedtest-cli
    print 'Test Running....'
    a = os.popen("python ~/git/isp-checkup/speedtest_cli.py --simple").read()
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

    #read in old data
    with open('/home/clark/git/isp-checkup/data/data.json','r') as f:
        dic = json.load(f)
        f.close()

    number = len(dic) + 1
    update = {number: { 'date': date, 'ping': p, 'download': d, 'upload': u}}
    dic.update(update)
    for key in dic:
        dic[int(key)] = dic.pop(key)
    sorted(dic)
    wf = open('/home/clark/git/isp-checkup/data/data.json','w')
    json.dump(dic, wf)

    return

if __name__ == '__main__':
    test()
    print 'Test Complete'
