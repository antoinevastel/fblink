__author__ = 'avastel'
# -*- coding: utf-8 -*-
from Firefox import *
import sqlite3 as lite

def main():
    firefox = Firefox()
    firefox.run()

    # con = lite.connect('/home/avastel/.mozilla/firefox/kwdl11go.default/webappsstore.sqlite')
    #
    # cur = con.cursor()
    # cur.execute('select * from webappsstore2 where key ="tempFpContent"')
    #
    # rows = cur.fetchall()
    #
    # for row in rows:
    #     print row

if __name__ == '__main__':
    main()
