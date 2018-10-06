#!/usr/local/bin/python3

import os
import logging
import time
import datetime
import re
import socket

TCP_IP = '192.168.86.81'
TCP_PORT = 8593
BUFFER_SIZE = 1024
nmealog = "nmea_2018-10-02.txt"

def create_stream():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    return s


def stream_nmea(stream):

    log_start_time = datetime.time()
    with open(nmealog, 'w') as f:
        while stream:
            data = stream.recv(BUFFER_SIZE)
            nmeaout = data.decode()
            f.write(nmeaout)
            print(nmeaout)

def main():
    stream = create_stream()
    stream_nmea(stream)  


if __name__ == '__main__':
    main()
