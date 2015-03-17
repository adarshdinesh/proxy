#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import os
import sys
from engine import Engine 
from gevent.server import StreamServer
from gevent.socket import create_connection

PUBLIC_ADDR = ''
LOOPBACK = '127.0.0.1'

class Proxy(StreamServer):

    def __init__(self, virtual, actual, **kwargs):
        StreamServer.__init__(self, (PUBLIC_ADDR, virtual), **kwargs)
        self.actual = actual
        self.virtual = virtual

    def handle(self, source, address):
        try:
            dest = create_connection((LOOPBACK, self.actual))
        except IOError, ex:
            print "Failed to connect..", ex
        query = Engine()
        gevent.spawn(forward, dest, source, query)
        gevent.spawn(filter, source, dest, query)

    def close(self):
        if self.closed:
            sys.exit("Aborting..")
        else:
            print "Closing listener socket.."
            StreamServer.close(self)

def forward(dest, source, query):
    try:
        while True:
            try:
                data = dest.recv(1024)
            except:
                dest.close()
                break
            if not data:
                break
            data = query.processRes(data)    
            source.sendall(data)
    finally:
        dest.close()
        source.close()

def filter(source, dest, query):
    try:
        while True:
            try:
                data = source.recv(1024)
            except:
                source.close()
                break
            if not data:
                break
            data = query.processReq(data)
            dest.sendall(data)
    finally:
        dest.close()
        source.close()
                                                                                                
