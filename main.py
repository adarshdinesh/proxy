#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import os
from src import Server
from config import CON

pwd = os.path.dirname(os.path.abspath(__file__))


def start():
    s = Server('', CON, pwd)
    s.Serve()
    return 0

if __name__ == "__main__":
    sys.exit(start())
