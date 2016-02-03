#!/usr/bin/env python

import os
import sys
import json
import collections
import time

def test():

    #run speedtest-cli
    print 'Test Running....'
    a = os.popen("python ~/git/isp-checkup/speedtest_cli.py --simple").read()
    #split the 3 line result (ping,down,up)
    lines = a.split('\n')
    #print a
    ts = int(time.time())

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
    with open('/home/clark/git/isp-checkup/data/data.js','r') as f:
        dic = json.load(f)
        f.close()

    #add newest values
    update = {ts: { 'ping': p, 'download': d, 'upload': u}}
    dic.update(update)

    #sort values
    for key in dic:
        dic[int(key)] = dic.pop(key)
    od = collections.OrderedDict(sorted(dic.items()))

    #write values to file
    wf = open('/home/clark/git/isp-checkup/data/data.js','w')
    json.dump(od, wf, indent=4)
    wf.close()

    return

if __name__ == '__main__':
    test()
    print 'Test Complete'
