#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
import os
import signal
from proxy import Proxy

class Server(object):

    def __init__(self, host, CON, pwd=None):
        self.host = host
        self.CON = CON
        self.confif = os.path.join(pwd, "config.py")
        self.greenlist = []

    def spawn(self, virtual, actual):
        server = Proxy(virtual, actual)
        gevent.signal(signal.SIGTERM, server.close)
        gevent.signal(signal.SIGINT, server.close)
        print "Listening on %d" % virtual
        server.serve_forever()
        
    def Serve(self): 
        for dbname, config in self.CON.iteritems():
            print "[+] %s %d -> %d" % (dbname, 
                config['virtual'], 
                config['actual'])
            gthread = gevent.spawn(self.spawn,
                config['virtual'], 
                config['actual'])
            self.greenlist.append(gthread)
        gevent.joinall(self.greenlist)
