__author__ = 'avastel'
# -*- coding: utf-8 -*-
from Firefox import *
import time
import sqlite3 as lite
import os

def main():
    firefox = Firefox()
    firefoxProcess = firefox.run()
    print("end of execution")

if __name__ == '__main__':
    main()
