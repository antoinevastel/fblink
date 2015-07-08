// ==UserScript==
// @name        amiu
// @namespace   amiu
// @description amiu
// @include     *
// @version     1
// @grant       none
// @run-at document-start
// @noframes
// ==/UserScript==
/*
  TODO : change http headers sent by browser
  spoof navigator.mimeTypes
  check the prototype of navigator object because there seems to be mistakes
  check regexp on windows and with different ua
  think about letting getters for properties (which would return "undefined" even though they are not present so that we count the number of access
  find new values for vendor and vendorSub : warning !! seems to be bound with the userAgent
  detect sites which fingerprint to find if they use cookies, localStorage etc 
*/

var seed = 11; var browser = 'chrome'; var mult = -1; var os = 'Windows';var newWidth = 2160; var newHeight = 1344; var availWidth = 2106; var availHeight = 1310; var newColorDepth = 4; var pixelDepth = 4; var timezoneOffset = -60; var productSub = '20030107'; var buildID = '';

//All the following variables will be defined using python
var userAgent = navigator.userAgent;
var language = navigator.language;
var languages = navigator.languages;

console.log("browser is "+browser+", os is : "+os);

//Plugins definition
function Plugin(name, description, filename){
  this.name = name;
  this.description = description;
  this.filename = filename;
}

var listPluginsChrome = [new Plugin("Chrome Remote Desktop Viewer", 'This plugin allows you to securely access other computers that have been shared with you. To use this plugin you must first install the <a href="https://chrome.google.com/remotedesktop">Chrome Remote Desktop</a> webapp.', 'internal-remoting-viewer')
  , new Plugin("Chrome PDF Viewer", '', 'mhjfbmdgcfjbbpaeojofohoefgiehjai')
  , new Plugin("Widevine Content Decryption Module", 'Enables Widevine licenses for playback of HTML audio/video content. (version: 1.4.8.823)', 'libwidevinecdmadapter.so')
  , new Plugin("Chrome PDF Viewer", 'Portable Document Format','internal-pdf-viewer')
  , new Plugin("Google Update", "Google Update", "npGoogleUpdate3.dll")
  , new Plugin("Intel® Identity Protection Technology", "Intel web components for Intel® Identity Protection Technology", "npIntelWebAPIIPT.dll")
  , new Plugin("Java Deployment Toolkit 8.0.310.13", "NPRuntime Script Plug-in Library for JavaTM Deploy", "npDeployJava1.dll")
  , new Plugin("JavaTM Platform SE 8 U31", "Next Generation Java Plug-in 11.31.2 for Mozilla browsers", "npjp2.dll")
  , new Plugin("VLC Web Plugin", "VLC media player Web Plugin 2.1.3", "npvlc.dll")
  , new Plugin("Battlelog Game Launcher", "Battlelog Game Launcher 2.6.2", "npbattlelog.dll")
  , new Plugin("GFACE Plugin", "GFACE Plugin", "npCry39.dll")
  , new Plugin("Google Earth Plugin", "GEPlugin", "npgeplugin.dll")
  , new Plugin("JavaTM Platform SE 8 U25", "Next Generation Java Plug-in 11.25.2 for Mozilla browsers", "npjp2.dll")
  , new Plugin("Pando Web Plugin", "Pando Web Plugin", "npPandoWebPlugin.dll")
  , new Plugin("Google Talk Plugin Video Renderer", "Version 5.41.0.0", "o1dbrowserplugin.plugin")
  , new Plugin("Java Deployment Toolkit 8.0.250.18", "NPRuntime Script Plug-in Library for JavaTM Deploy", "npDeployJava1.dll")
  , new Plugin("JavaTM Platform SE 8 U25", "Next Generation Java Plug-in 11.25.2 for Mozilla browsers", "npjp2.dll")
  , new Plugin("VLC Web Plugin", "VLC media player Web Plugin 2.2.0", "npvlc.dll")
  , new Plugin("Octoshape Streaming Services", "Octoshape embedded video plugin", "sua-1401100-0-npoctoshape.dll")
  , new Plugin("QuickTime Plug-in 7.7.5", 'The QuickTime Plugin allows you to view a wide variety of multimedia content in Web pages. For more information visit the A HREF=http:www.apple.comquicktimeQuickTimeA Web site.', "npqtplugin.dll")
  , new Plugin("JavaTM Platform SE 7 U67", "Next Generation Java Plug-in 10.67.2 for Mozilla browsers", "npjp2.dll")
  , new Plugin("Nokia Suite Enabler Plugin", "Nokia Suite Enabler Plugin", "npNokiaSuiteEnabler.dll")
  , new Plugin("Ace Stream P2P Multimedia Plug-in", "ACE Stream Plug-in Version 2.2.5.1-next Copyright c 2012-2014 Innovative Digital Technologies", "npace_plugin.dll")
  , new Plugin("NVIDIA 3D VISION", "NVIDIA 3D Vision Streaming plugin for Mozilla browsers", "npnv3dvstreaming.dll")
  , new Plugin("iTunes Application Detector", "iTunes Detector Plug-in", "npitunes.dll")
  , new Plugin("Skype Web Plugin", "Skype Web Plugin", "npSkypeWebPlugin.dll")
  , new Plugin("VMware Remote Console Plug-in", "VMware Remote Console Plug-in", "np-vmware-vmrc.dll")
  , new Plugin("WildTangent Games App V2 Presence Detector", "WildTangent Games App V2 Presence Detector", "NP_wtapp.dll")
];

var listPluginsFirefox = [new Plugin("DivX® Web Player", "DivX Web Player version 1.4.0.233", "libtotem-mully-plugin.so")
  , new Plugin("QuickTime Plug-in 7.6.6", 'The <a href="http://www.gnome.org/">Videos</a> 3.10.1 plugin handles video and audio streams.', "libtotem-narrowspace-plugin.so")
  , new Plugin("VLC Multimedia Plugin (compatible Videos 3.10.1)", 'The <a href="http://www.gnome.org/">Videos</a> 3.10.1 plugin handles video and audio streams.', "libtotem-cone-plugin.so")
  , new Plugin("Windows Media Player Plug-in 10 (compatible; Videos)", 'The <a href="http://www.gnome.org/">Videos</a> 3.10.1 plugin handles video and audio streams.', "libtotem-gmp-plugin.so")
  , new Plugin("iTunes Application Detector", 'This plug-in detects the presence of iTunes when opening iTunes Store URLs in a web page with Firefox.', "librhythmbox-itms-detection-plugin.so")
  , new Plugin("Foxit Reader Plugin for Mozilla", "Foxit Reader Plug-In For Firefox and Netscape", "npFoxitReaderPlugin.dll")
  , new Plugin("Java Deployment Toolkit 8.0.250.18", "NPRuntime Script Plug-in Library for JavaTM Deploy", "npdeployJava1.dll")
  , new Plugin("Intel® Identity Protection Technology", "Intel web components updater - Installs and updates the Intel web components", "npIntelWebAPIUpdater.dll")
  , new Plugin("Photo Gallery", "NPWLPG", "NPWLPG.dll")
  , new Plugin("Adobe Acrobat", "Adobe PDF Plug-In For Firefox and Netscape 11.0.10", "nppdf32.dll")
  , new Plugin("ESN Launch Mozilla Plugin", "2.3.0", "npesnlaunch.dll")
  , new Plugin("NVIDIA 3D Vision", "NVIDIA 3D Vision plugin for Mozilla browsers", "npnv3dv.dll")
  , new Plugin("Unity Player", "Unity Player 4.3.5f1", "npUnity3D32.dll")
  , new Plugin("Qualys BrowserCheck Plugin", "Qualys BrowserCheck Plugin 1.5.46.1", "npqbc.dll")
  , new Plugin("Google Talk Plugin Video Renderer", "Version 5.4.2.18903", "o1dbrowserplugin.dll")
  , new Plugin("Google Earth Plugin", "GEPlugin", "npgeplugin.dll"),
  , new Plugin("Google Update", "Google Update", "npGoogleUpdate3.dll")
  , new Plugin("NVIDIA 3D VISION", "NVIDIA 3D Vision Streaming plugin for Mozilla browsers", "npnv3dvstreaming.dll")
  , new Plugin("DivX Browser Plug-In", 'a href=http:kdekorte.googlepages.comgecko-mediaplayerGecko Media Playera 1.0.4brbrVideo Player Plug-in for QuickTime RealPlayer and Windows Media Player streams using a href=http:mplayerhq.huMPlayera', "gecko-mediaplayer-dvx.so")
  , new Plugin("Adobe Acrobat", "Adobe Acrobat Plug-In Version 7.00 for Netscape", "nppdf32.dll")
  , new Plugin("SumatraPDF Browser Plugin", "SumatraPDF Browser Plugin", "npPdfViewer.dll")
  , new Plugin("Java Deployment Toolkit 7.0.710.14", "NPRuntime Script Plug-in Library for JavaTM Deploy", "npdeployJava1.dll")
];

//end of plugins definition

//Navigator definition
var appName = 'Netscape';
var reAppVersionChrome = /[0-9.]+[\w\W]+\/[\w\W]+/;
var reAppVersionFirefox = /[0-9.]+ \([A-Z0-9]*/;
if(browser === "chrome"){
  var appVersion = userAgent.match(reAppVersionChrome)[0];
}else{
  var appVersion = userAgent.match(reAppVersionFirefox)[0]+")";
}

var appCodeName = "Mozilla";
var product = "Gecko";

//Platform
//The platform has to be the same as the one we can find in the userAgent
var rePlatformChrome = /; (Linux|Windows) [\w\W]+[\d]+\) /;
var rePlatformFirefox = /; (Linux|Windows) [\w\W]+[\d]+; /;
var listPlatformsWindows = ["Win32", "Win64"];
if(browser === "chrome"){
  if(os === "Windows"){
    var platform = listPlatformsWindows[seed%listPlatformsWindows.length];
  } else{
    var platform = userAgent.match(rePlatformChrome)[0];
    platform = platform.substring(2, platform.length-2);
  }
} else{
  if(os === "Windows"){
    var platform = listPlatformsWindows[seed%listPlatformsWindows.length];
  } else{
    var platform = userAgent.match(rePlatformFirefox)[0];
    platform = platform.substring(2, platform.length-2);
  }
}
//End platform

//oscpu
//oscpu is only for firefox and is equal to the platform
if(browser === "firefox"){
  var oscpu = platform;
}
//end oscpu

//vendor and vendorSub
if(browser === "chrome"){
  var vendor = "Google Inc.";
} else{
  var vendor = "";
}

var vendorSub = "";
//end vendor and vendorSub
//End of navigator definition


var myController = {
  nbAccess : 0,
  navigatorAccessed : function(){
    this.nbAccess ++;
  },
  fakePlugins : function(){
    var listPlugins;
    if(browser === "chrome"){
      listPlugins = listPluginsChrome;
    } else{
      listPlugins = listPluginsFirefox;
    }

    var nbNewPlugins = seed % 5 + 3; //Max 8 
    var nbPluginsOriginal = navigator.plugins.length;
    var newPlugins = new Array(); 
    var index = nbNewPlugins;
    for(var i = 0; i < nbNewPlugins; i++){
        newPlugins[i] = listPlugins[index];
        if(os === "Windows" && newPlugins[i].filename.indexOf(".so") >= 0){
            newPlugins[i].filename.replace(".so", ".dll");
        } else if(os === "Linux" && newPlugins[i].filename.indexOf(".dll") >= 0){
            newPlugins[i].filename.replace(".dll", ".so");
        }
        listPlugins[index] = -1
        index = (index + nbPluginsOriginal) % listPlugins.length;
        while(listPlugins[index] === -1){
          index++;
        }
    }
    return newPlugins;
  }
};

/* Screen object */
Object.defineProperty(screen, 'width', {
    get: function(){
      myController.navigatorAccessed();
      return newWidth;
    }
});

Object.defineProperty(screen, 'height', {
    get: function(){
      myController.navigatorAccessed();
      return newHeight;
    }
});

Object.defineProperty(screen, 'colorDepth', {
  get: function(){
    myController.navigatorAccessed();
    return newColorDepth;
  }
});

Object.defineProperty(screen, 'availWidth', {
  get: function(){
    myController.navigatorAccessed();
    return availWidth;
  }
});

Object.defineProperty(screen, 'availHeight', {
  get: function(){
    myController.navigatorAccessed();
    return availHeight;
  }
});

Object.defineProperty(screen, 'pixelDepth', {
  get: function(){
    myController.navigatorAccessed();
    return pixelDepth;
  }
});

/* Navigator object */
//App info
Object.defineProperty(navigator, 'appName', {
  get: function(){
    myController.navigatorAccessed();
    return appName;
  }
});

Object.defineProperty(navigator, 'appVersion', {
  get: function(){
    myController.navigatorAccessed();
    return appVersion;
  }
});

Object.defineProperty(navigator, 'appCodeName', {
  get: function(){
    myController.navigatorAccessed();
    return appCodeName;
  }
});

//Language and languages should be set using the value generated in python
Object.defineProperty(navigator, 'language', {
  get: function(){
    myController.navigatorAccessed();
    return language;
  }
});

Object.defineProperty(navigator, 'languages', {
  get: function(){
    myController.navigatorAccessed();
    return languages;
  }
});

Object.defineProperty(navigator, 'platform', {
  get: function(){
    myController.navigatorAccessed();
    return platform;
  }
});

Object.defineProperty(navigator, 'product', {
  get: function(){
    myController.navigatorAccessed();
    return product;
  }
});

Object.defineProperty(navigator, 'productSub', {
  get: function(){
    myController.navigatorAccessed();
    return productSub;
  }
});

Object.defineProperty(navigator, 'vendor', {
  get: function(){
    myController.navigatorAccessed();
    return vendor;
  }
});

Object.defineProperty(navigator, 'vendorSub', {
  get: function(){
    myController.navigatorAccessed();
    return vendorSub;
  }
});

Date.prototype.getTimezoneOffset = function() {
  return timezoneOffset;
};

if(browser === "firefox"){
  Object.defineProperty(navigator, 'buildID', {
    get: function(){
      myController.navigatorAccessed();
      return buildID;
    }
  });
}

//Oscpu : avalaible only on firefox
if(browser === "firefox"){
  Object.defineProperty(navigator, 'oscpu', {
    get: function(){
      myController.navigatorAccessed();
      return oscpu;
    }
  });
}

/*
  Important attributes for plugins :
  - description, name, filename, version
  - typeof navigator.plugins !== "undefined" (be carefull with the type of undefined !)

*/

Object.defineProperty(navigator, 'plugins', {
  enumerable: false,
  configurable: false,
  writable: false,
  value: myController.fakePlugins()
});
 
