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


        self.setPreferences()

    def setUserAgent(self):
        self.userAgent = 'user_pref("general.useragent.override","Mozilla/5.007 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0");\n'

    def setAppName(self):
        self.appName = 'user_pref("general.appname.override","fake appName py");\n'

    def setAppVersion(self):
        self.appVersion = 'user_pref("general.appversion.override","fake appVersion py");\n'

    #undefined on chrome
    def setOscpu(self):
        self.oscpu = 'user_pref("general.oscpu.override","fake oscpu py");\n'

    def setPlatform(self):
        self.platform = 'user_pref("general.platform.override","fake platform py");\n'

    def setAccept(self):
        self.accept= 'user_pref("fake accept py");\n'

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

    def run(self):
        subprocess.Popen('firefox')