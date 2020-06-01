#!/usr/bin/python

import os
import sys
from multiprocessing.connection import Client


address = ('localhost', 6000)
conn = Client(address)
kpa_max = -5095 # 1 1/4 turns

def sendCommand(s):
    print 'sending command'
    if not s:
        conn.send('error')
    else:
        conn.send(s)

def sendCommandAndGetResponse(s):
    print 'sending command'
    if not s:
        conn.send('error')
    else:
        conn.send(s)
    resp = conn.recv()
    print 'response is ' + resp
    return resp

def kpa_interpolate(v):
    ret_val = kpa_max * (v / float(100))
    print(ret_val)
    return ret_val

'''
def loadkPaPositions():
    try:
        f = open(os.path.dirname(os.path.realpath(__file__)) + '/kPaPositions.txt', 'r')
        kPaPositions = {}
        print "In loadkpapositions"
        for line in f:
            parts = line.split(':', 2)
            kPaPositions[parts[0]] = parts[1].strip()
        f.close()
        print "kPaPositions:"
        print kPaPositions
        return kPaPositions
    except:
        conn.send('kpa_file_error')
        print "Error loading KPA file"
        f.close()
'''

if (len(sys.argv) == 1 or sys.argv[1] == 'TMP'):
    print sendCommandAndGetResponse("TMP:0").strip()
elif (sys.argv[1] == 'FAN'):
    sendCommand("FAN:%s" % sys.argv[2])
elif (sys.argv[1] == 'KPQ'):
    sendCommandAndGetResponse("KPQ:")

elif (sys.argv[1] == 'KPA'):
    kPaPositions = loadkPaPositions()
    try:
        sendCommand("KPA:%s" % kPaPositions[str(sys.argv[2])])
    except:
        conn.send('kpa_error')
        print "kpa key does not exist"
elif (sys.argv[1] == 'KPAI'):
    try:
        val = kpa_interpolate(int(sys.argv[2]))
        sendCommand("KPA:%s " % val)
    except:
        conn.send('kpa_error')
        print "kpai value error"

elif (sys.argv[1] == 'close_server'):
    sendCommand('close_server')
else:
    print "Unknown command!"

print "closing connection"
conn.send('close')
conn.close()
