__author__ = 'avastel'
# -*- coding: utf-8 -*-

from tkinter import *
import webbrowser

class Ui(Frame):
  
    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, width=1768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.gmUninstalled = LabelFrame(self, text="Greasmonkey is not installed", padx=20, pady=20)
        self.gmUninstalled.pack(fill="both", expand="yes")
        self.message = "Click on this link to download and install Greasmonkey"
        self.link =Label(self.gmUninstalled, text=self.message, fg="blue", cursor="hand2")
        self.link.pack()
        self.link.bind("<Button-1>", self.openLink)
    
    def openLink(event, x):
        webbrowser.get('firefox').open_new_tab('https://addons.mozilla.org/fr/firefox/addon/greasemonkey/')



