__author__ = 'avastel'
# -*- coding: utf-8 -*-
from Firefox import *
import sqlite3 as lite
import os

def main():
    firefox = Firefox()
    firefoxProcess = firefox.run()
    firefoxProcess.wait()



    con = lite.connect('/home/avastel/.mozilla/firefox/kwdl11go.default/cookies.sqlite')
    cur = con.cursor()

    #we delete all the cookies
    cur.execute('DELETE FROM moz_cookies')
    cur.execute('vacuum')

    #we delete the cache because of cookieless use tracking
    #see this article : http://robertheaton.com/2014/01/20/cookieless-user-tracking-for-douchebags/
    os.system("rm /home/avastel/.cache/mozilla/firefox/kwdl11go.default/cache2/entries/*")


    print("end of execution")

if __name__ == '__main__':
    main()
