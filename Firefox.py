__author__ = 'avastel'
# -*- coding: utf-8 -*-

import subprocess
import random
import fileinput
import tkinter as tk
import math
import os
import getpass
import sys
import platform

class Firefox():

    def __init__(self):
        self.nameUser = getpass.getuser()
        print(self.nameUser)
        self.profileName = ""
        if platform.system() == "Windows":
            self.mozFolder = 'C://Users/'+self.nameUser+'/AppData/Roaming/Mozilla/Firefox/Profiles'
            self.filesMoz = os.listdir(self.mozFolder)
            for f in self.filesMoz:
                if ".default" in f:
                    self.profileName = f
                    break

            if self.profileName == "":
                sys.exit(0)

            self.prefsPath = os.path.join(self.mozFolder, self.profileName, "prefs.js")
            self.platformSystem = "Windows"
            self.gmScript = os.path.join(self.mozFolder, self.profileName, "gm_scripts", "amiu", "amiu.user.js")
            self.firefox = os.path.join('C:\\', 'Program Files (x86)', 'Mozilla Firefox', 'firefox.exe')
        else:
            self.mozFolder = "/home/"+self.nameUser+"/.mozilla/firefox"
            self.filesMoz = os.listdir("/home/"+self.nameUser+"/.mozilla/firefox")
            for f in self.filesMoz:
                if ".default" in f:
                    self.profileName = f
                    break

            if self.profileName == "":
                sys.exit(0)

            self.prefsPath = "/home/"+self.nameUser+"/.mozilla/firefox/"+self.profileName+"/prefs.js"
            self.platformSystem ="Linux"
            self.gmScript = self.mozFolder+"/"+self.profileName+"/gm_scripts/amiu/amiu.user.js"
            self.firefox = "firefox"

        self.setUserAgent()
        self.setLanguages()
        self.setAcceptEncoding()
        self.setAcceptHttp()
        self.setSizeScren()
        self.setTimezoneOffset()
        self.setProductSub()
        self.setBuildId()

        self.setPreferences()
        self.setVarJs()

    def setLanguages(self):
        listLanguages = ["en-US", "en","fr","fr-FR","en-GB","en-au","en-CA"]
        choosenLanguages = list()
        for i in range(0,3):
            v = random.randint(0, len(listLanguages)-1)
            if listLanguages[v] != -1:
                choosenLanguages.append(listLanguages[v])
            else:
                while listLanguages[v] == -1:
                    v = (v+1)%len(listLanguages)
                choosenLanguages.append(listLanguages[v])
            listLanguages[v]=-1

        choosenLanguagesStr = choosenLanguages[0]+","
        choosenLanguagesStr += choosenLanguages[1]+";q=0.8,"
        choosenLanguagesStr += choosenLanguages[2]+";q=0.5"

        self.languages = 'user_pref("intl.accept_languages", "'+choosenLanguagesStr+'");\n'

    def setAcceptHttp(self):
        self.acceptHttp = 'user_pref("network.http.accept.default", "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8");\n'

    def setAcceptEncoding(self):
        self.acceptEncoding = 'user_pref("network.http.accept-encoding", "gzip, deflate");\n'

    def setPreferences(self):
        with open(self.prefsPath, "a") as prefs:
            prefs.write(self.languages)
            prefs.write(self.userAgent)
            prefs.write(self.acceptHttp)
            prefs.write(self.acceptEncoding)
            prefs.close()

    def run(self):
        firefoxProcess = subprocess.Popen([self.firefox, "-private", "http://bluecava.com/opt-out/"])
        return firefoxProcess

    def setUserAgent(self):
        self.listUAs =["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (X11; Linux i686; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36 OPR/26.0.1656.32",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36 OPR/26.0.1656.32",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"]

        selectedUA = self.listUAs[random.randint(0, len(self.listUAs) - 1)]
        self.userAgent = 'user_pref("general.useragent.override","'+selectedUA+'");\n'
        print(selectedUA)
        if "Windows" in selectedUA:
            self.os = "Windows"
        else:
            self.os = "Linux"

        if "Firefox" in selectedUA:
            self.browser = "firefox"
        else:
            self.browser = "chrome"

        print(self.os)
        print(self.browser)

    def indexLimitValue(self, value, listValues):
        found = False
        cpt = 0
        while found==False and cpt < len(listValues) and listValues[cpt] <= value:
            cpt += 1

        return cpt

    def setSizeScren(self):
        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()

        if self.os == "firefox":
            self.mult = 1
        else:
            self.mult = -1

        listWidth = [832, 960, 1024, 1120, 1136, 1152, 1280, 1334, 1366, 1400, 1440, 1600, 1680, 1792, 1800, 1856, 1920, 2048, 2160, 2304, 2538, 2560, 2880, 3200, 3440, 3840, 4096, 5120]
        listHeight = [480, 540, 544, 576, 600, 624, 640, 720, 750, 768, 800, 832, 854, 864, 900, 960, 1024, 1050, 1080, 1152, 1200, 1280, 1344, 1392, 1400, 1440, 1536, 1600, 1700, 1728, 1800, 1920, 2048, 2100, 2160, 2304, 2400, 2880, 3072, 3200, 4096]
        listColorDepth = [4, 8, 16, 24, 32]

        indexNewWidth = (self.indexLimitValue(self.width, listWidth) + self.mult*4) % len(listWidth)
        indexNewHeight = (self.indexLimitValue(self.height, listHeight) + self.mult*4) % len(listHeight)
        self.width = listWidth[indexNewWidth]
        self.height = listHeight[indexNewHeight]
        self.availWidth = int(math.floor(0.975 * self.width))
        self.availHeight = int(math.floor(0.975 * self.height))
        self.colorDepth = listColorDepth[self.width % len(listColorDepth)]

    def setTimezoneOffset(self):
        listTimezoneOffset = [-60, 300, -120, 0, 480, -540, 360, 420, 240, -480, -660, -180, 180, 120, -330, -600, -780, -240, -420]
        self.timezoneOffset = listTimezoneOffset[random.randint(0.,200) % len(listTimezoneOffset)]

    def setProductSub(self):
        seed = random.randint(0,50)

        if self.browser == "chrome":
            self.productSub = "20030107"
        else:
            if seed % 3 == 0:
                yearProductSub = "2014"
            else:
                yearProductSub = "2013"

            monthProductSub = str(((seed % 12) +1))

            if (seed % 12) +1 < 10:
                monthProductSub = "0"+monthProductSub

            dayProductSub = str(((seed % 29) +1))
            if (seed % 29) +1 < 10:
                dayProductSub = "0"+dayProductSub

            self.productSub = yearProductSub+monthProductSub+dayProductSub

    def setBuildId(self):
        seed = random.randint(0,50)

        if self.browser =="chrome":
            self.buildID = ""
        else:
            if (seed+1) % 3 == 0:
                yearBuildId = "2014"
            else:
                yearBuildId = "2013"

            monthBuildId = str((((2+seed) % 12) +1))

            if ((2+seed) % 12) +1 < 10:
                monthBuildId = "0"+monthBuildId

            dayBuildId = str((((2+seed) % 29) +1))
            if ((2+seed) % 29) +1 < 10:
                dayBuildId = "0"+dayBuildId

            hourBuildId = str((((2+seed) % 24) +1))
            if ((2+seed) % 24) +1 < 10:
                hourBuildId = "0"+hourBuildId

            self.buildID = yearBuildId+monthBuildId+dayBuildId+hourBuildId

    def setVarJs(self):
        self.seed = random.randint(0, 200)
        vars =""
        #we define the variable seed in javascript file
        for line in fileinput.input(self.gmScript, inplace=True):
            if "var seed = " in line:
                vars += "var seed = "+str(self.seed)+"; var browser = '"+self.browser+"'; var mult = "+str(self.mult)+"; var os = '"+self.os+"';"
                vars += "var newWidth = "+str(self.width)+"; var newHeight = "+str(self.height)+"; var availWidth = "+str(self.availWidth)+"; "
                vars += "var availHeight = "+str(self.availHeight)+"; var newColorDepth = "+str(self.colorDepth)+"; var pixelDepth = "+str(self.colorDepth)+"; "
                vars += "var timezoneOffset = "+str(self.timezoneOffset)+"; var productSub = '"+self.productSub+"'; var buildID = '"+self.buildID+"';"
                print(vars)
            else:
                newLine = line.replace("\n","")
                print(newLine)
