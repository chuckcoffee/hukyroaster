#!/usr/bin/python

import sys
import serial
import os
import serial.tools.list_ports
from multiprocessing.connection import Listener


ports = serial.tools.list_ports.comports()
arduinoPort = None
for p in ports:
    if 'Arduino' in p[1]:
        arduinoPort = p[0]
        print p[1] + ' found at ' + p[0]
        break

if (arduinoPort is None):
    print "Arduino not connected?"
    sys.exit(-1)

arduino = serial.Serial(arduinoPort, 9600, timeout=2)

def sendToArduino(str):
    arduino.write(str)

def readFromArduino():
    l = arduino.readline()
    print("Got response: '" + l.strip() + "'")
    return l

def readkPa():
    return open('kpa.txt').read().strip()

def parseCmd(cmd):
    print "Got command: '%s'" % cmd
    try:
        cmd, val = cmd.split(':')
    except ValueError:
        print "Bad command!";
        return

    if (cmd == 'FAN'):
        val = int(int(val) * 2.54)
        sendToArduino("FAN:%d\n" % val)
    elif (cmd == 'TMP'):
        sendToArduino("TMP:0\n")
        conn.send(readFromArduino().strip() + ',' + readkPa() + ',0.0\n')
    elif (cmd == 'KPA'):
        sendToArduino("KPA:%s\n" % val)
    elif (cmd == 'MTR'):
        sendToArduino("MTR:%s\n" % val)
    elif (cmd == 'MZR'):
        sendToArduino("MZR:0\n")
    elif (cmd == 'KPQ'):
        sendToArduino('KPQ:0\n')
        response = readFromArduino().strip()
        print "Current position %s" % response
        conn.send(response)

address = ('localhost', 6000)   
listener = Listener(address)
while True:
    conn = listener.accept()
    print 'connection accepted from', listener.last_accepted
    exit_flag=0
    while True:
        msg = conn.recv()
        if not msg:
            break
        print 'got line: ' + msg
        if msg == 'close':
            conn.close()
            break
        elif msg == 'close_server':
            print 'about to close server'
            conn.close()
            exit_flag=1
            break
        elif msg == 'kpa_error':
            print 'error in command being sent, check KPA position is mapped'
            conn.close()
            break
        elif msg == 'kpa_file_error':
            print 'error loading kpa file, ensure format like a:b'
            conn.close()
            break
        else:
            parseCmd(msg)
    if exit_flag:
        print "Closing server"
        break
    
listener.close()
