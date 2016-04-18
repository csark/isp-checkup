#!/usr/bin/env python

#2016 Clark Hatch
#Provide simple way to monitor provided internet bandwidth


import os, json, collections, time

def test():

    #run speedtest-cli
    a = os.popen("python /path/to/repo/isp-checkup/speedtest_cli.py --simple").read()

    #split the 3 line result (ping,down,up)
    lines = a.split('\n')

    #create timestamp
    ts = int(time.time())

    #if speedtest could not connect set the speeds to 0
    if "Could not" in a:
            p = 100
            d = 0
            u = 0
    #extract the values for ping down and up values
    else:
            p = lines[0][6:11]
            d = lines[1][10:14]
            u = lines[2][8:12]

    json_location = '/path/to/repo/isp-checkup/data/data.json'
    javascript_data = '/path/to/repo/isp-checkup/js/data.js'
    #read in old data
    with open(json_location,'r') as f:
        dic = json.load(f)
        f.close()

    #add newest values to dictionary
    update = {ts: { 'ping': p, 'download': d, 'upload': u}}
    dic.update(update)

    #Magic number refers to the amount of datapoints you want to show in your graph
    #I like to generate a sample every 15 minutes. With a magic number of 48 that
    #displays 12 hours of data.
    magic_number = 48

    #sort and delete oldest value. Keep only a magic number's worth of data
    od = {}
    if len(dic) > magic_number:
        for key in dic:
            dic[int(key)] = dic.pop(key)
        od = collections.OrderedDict(sorted(dic.items()))
        od.popitem(last=False)
    else:
        for key in dic:
            dic[int(key)] = dic.pop(key)
        od = collections.OrderedDict(sorted(dic.items()))

    #write values to file
    wf = open(json_location,'w')
    json.dump(od, wf, indent=4)
    wf.close()

    #create valid javascript json object
    js_data = open(javascript_data, 'w')
    jsonfile = open(json_location,'r')
    jf = jsonfile.read()
    data = ''
    for line in jf:
        data += line.strip('\n')
    js_data.write('data = \'')
    js_data.write(data)
    js_data.write('\';')
    js_data.close()

    return

if __name__ == '__main__':
    test()
