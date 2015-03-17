#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Engine(object):
    def __init__(self):
        self.whitelist = []
        self.blacklist = []
    def processReq(self, data):
        # process data here
        return data

    def processRes(self, data):
        # process responce here
        return data
