__author__ = 'avastel'
# -*- coding: utf-8 -*-

import subprocess

class Firefox():

    def __init__(self):
        self.setUserAgent()
        self.setAppName()
        self.setAppVersion()
        self.setOscpu()
        self.setPlatform()
        self.setAccept()
        self.setLanguages()
        self.setAcceptEncoding()
        self.setAcceptHttp()
        self.setGreaseMonkey()

        self.setPreferences()

    def setUserAgent(self):
        self.userAgent = 'user_pref("general.useragent.override","Mozilla/5.007 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0");\n'

    def setAppName(self):
        self.appName = 'user_pref("general.appname.override","fake appName py");\n'

    def setAppVersion(self):
        self.appVersion = 'user_pref("general.appversion.override","fake appVersion py");\n'

    #undefined on chrome
    def setOscpu(self):
        self.oscpu = 'user_pref("general.oscpu.override","fake oscpu py 2");\n'

    def setPlatform(self):
        self.platform = 'user_pref("general.platform.override","fake platform py");\n'

    def setAccept(self):
        self.accept= 'user_pref("fake accept py");\n'

    def setLanguages(self):
        self.languages = 'user_pref("intl.accept_languages", "en,fr;q=0.5");\n'

    def setAcceptHttp(self):
        self.acceptHttp = 'user_pref("network.http.accept.default", "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8")\n;'

    def setAcceptEncoding(self):
        self.acceptEncoding = 'user_pref("network.http.accept-encoding", "gzip, deflate")\n;'

    def setGreaseMonkey(self):
        self.greaseMonkey = 'user_pref("extensions.greasemonkey.fileIsGreaseable","true");\n'
    def setPreferences(self):
        #set kwdl11 ... part with a variable
        with open("/home/avastel/.mozilla/firefox/kwdl11go.default/user.js", "w") as prefs:
            prefs.write("\n"+self.userAgent)
            prefs.write(self.appName)
            prefs.write(self.appVersion)
            prefs.write(self.oscpu)
            prefs.write(self.platform)
            prefs.write(self.accept)

            prefs.close()

        with open("/home/avastel/.mozilla/firefox/kwdl11go.default/prefs.js", "w") as prefs:
            prefs.write("\n"+self.languages)
            prefs.write(self.acceptHttp)
            prefs.write(self.acceptEncoding)
            prefs.write(self.greaseMonkey)
            prefs.close()



    def run(self):
        subprocess.Popen('firefox')