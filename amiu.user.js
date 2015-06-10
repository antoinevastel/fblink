// ==UserScript==
// @name        amiu
// @namespace   amiu
// @description amiu
// @include     *
// @version     1
// @grant       none
// @run-at document-start
// ==/UserScript==
/*
  TODO : change http headers sent by browser
*/

console.log("product "+navigator.product);
console.log("platform "+navigator.platform);
//In the future this seed will be generated using python so that it will be constant during a whole session of browsing
var seed = 4;
//All the following variables will be defined using python
var userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36";
var language = "en";
var languages = "en,fr;q=0.5";
var platform = "Linux x86_64";

//We define a new screen resolution
var currentWidth = screen.width;
var currentHeight = screen.height;
var currentColorDepth = screen.colorDepth;

var listWidth = [832, 960, 1024, 1120, 1136, 1152, 1280, 1334, 1366, 1400, 1440, 1600, 1680, 1792, 1800, 1856, 1920, 2048, 2160, 2304, 2538, 2560, 2880, 3200, 3440, 3840, 4096, 5120];
var listHeight = [480, 540, 544, 576, 600, 624, 640, 720, 750, 768, 800, 832, 854, 864, 900, 960, 1024, 1050, 1080, 1152, 1200, 1280, 1344, 1392, 1400, 1440, 1536, 1600, 1700, 1728, 1800, 1920, 2048, 2100, 2160, 2304, 2400, 2880, 3072, 3200, 4096];
var listColorDepth = [4, 8, 16, 24, 32];

function indexLimitValue(value, tab){
  var found = false;
  var cpt = 0;
  while(!found && cpt < tab.length && tab[cpt] <= value){
    cpt++;
  }

  return cpt;
}

if(seed % 2 == 0){
  var mult = -1
  var browser = "chrome"
}else{
  var mult = 1;
  var browser = "firefox";
}

var indexNewWidth = (indexLimitValue(currentWidth, listWidth) + mult*4) % listWidth.length;
var indexNewHeight = (indexLimitValue(currentHeight, listHeight) + mult*4) % listHeight.length;
var indexNewColorDepth = (indexLimitValue(currentColorDepth, listColorDepth) + mult*2) % listColorDepth.length;
var newWidth = listWidth[indexNewWidth];
var newHeight = listHeight[indexNewHeight];
var newColorDepth = listColorDepth[indexNewColorDepth];

var availWidth = Math.floor(0.975*newWidth);
var availHeight = Math.floor(0.975*newHeight);
//screen.pixelDepth and screen.colorDepth should always be the same
var pixelDepth = newColorDepth;

//End of new screen resolution definition

//Plugins definition
function PluginChrome(name, description, filename){
  this.name = name;
  this.description = description;
  this.filename = filename;
}

function PluginFirefox(name, description, filename, version){
  this.name = name;
  this.description = description;
  this.filename = filename;
  this.version = version;
}

var listPluginsChrome = [new PluginChrome("Chrome Remote Desktop Viewer",'This plugin allows you to securely access other computers that have been shared with you. To use this plugin you must first install the <a href="https://chrome.google.com/remotedesktop">Chrome Remote Desktop</a> webapp.', 'internal-remoting-viewer')
  , new PluginChrome("Chrome PDF Viewer",'', 'mhjfbmdgcfjbbpaeojofohoefgiehjai')
  , new PluginChrome("Widevine Content Decryption Module",'Enables Widevine licenses for playback of HTML audio/video content. (version: 1.4.8.823)','libwidevinecdmadapter.so')
  , new PluginChrome("Chrome PDF Viewer",'Portable Document Format','internal-pdf-viewer')
  , new PluginChrome("Shockwave Flash", "Shockwave Flash 17.0 r0", "libpepflashplayer.so")
];

var listPluginsFirefox = [new PluginFirefox('DivX® Web Player', 'DivX Web Player version 1.4.0.233', 'libtotem-mully-plugin.so', '')
  , new PluginFirefox('QuickTime Plug-in 7.6.6', 'The <a href="http://www.gnome.org/">Videos</a> 3.10.1 plugin handles video and audio streams.', 'libtotem-narrowspace-plugin.so', '')
  , new PluginFirefox('Shockwave Flash','Shockwave Flash 11.2 r202','libflashplayer.so','11.2.202.466')
  , new PluginFirefox('VLC Multimedia Plugin (compatible Videos 3.10.1)', 'The <a href="http://www.gnome.org/">Videos</a> 3.10.1 plugin handles video and audio streams.','libtotem-cone-plugin.so','')
  , new PluginFirefox('Windows Media Player Plug-in 10 (compatible; Videos)','The <a href="http://www.gnome.org/">Videos</a> 3.10.1 plugin handles video and audio streams.','libtotem-gmp-plugin.so', '')
  , new PluginFirefox('iTunes Application Detector', 'This plug-in detects the presence of iTunes when opening iTunes Store URLs in a web page with Firefox.','librhythmbox-itms-detection-plugin.so')
];

//end of plugins definition

//Navigator definition
var appName = 'Netscape';

/* Example of user agent and app version on chrome 
  user agent : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"
  /5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36
  appVersion : "5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"

  Example of user agent and app version on firefox
  user agent : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"
  appVersion : "5.0 (X11)"
*/

var reAppVersionChrome = /[0-9.]+[\w\W]+\/[\w\W]+/;
var reAppVersionFirefox = /[0-9.]+ \([A-Z0-9]*/;
if(browser ==="chrome"){
  var appVersion = userAgent.match(reAppVersionChrome)[0];
}else{
  var appVersion = userAgent.match(reAppVersionFirefox)[0]+")";
}

var appCodeName = "Mozilla";
if(seed % 3 == 0){
  var yearBuildId = "2015";
}else{
  var yearBuildId = "2014";
}

var i = 12;
var found = false;
while(i >= 0 && !found){
  if(seed % i == 0){
    var monthBuild = i.toString();
    found = true;
  }
  i--;
}


var i = 29;
var found = false;
while(i >= 0 && !found){
  if(seed % i == 0){
    var dayBuild = i.toString();
    found = true;
  }
  i--;
}

var i = 24;
var found = false;
while(i >= 0 && !found){
  if(seed % i == 0){
    var hourBuild = i.toString();
    found = true;
  }
  i--;
}


///Language and languages :


//End of navigator definition


var myController = {
  nbAccess : 0,
  navigatorAccessed : function(){
    this.nbAccess ++;
    //console.log("Nb access : "+this.nbAccess);
  },
  fakePlugins : function(){

    if(browser === "chrome"){
      var listPlugins = listPluginsChrome;
    }else{
      var listPlugins = listPluginsFirefox;
    }

    var nbNewPlugins = seed % 5; //Max 5 new plugins
    nbPluginsOriginal = navigator.plugins.length;
    newPlugins = new Array();
    
    var index = nbNewPlugins;
    for(i= 0; i < nbNewPlugins; i++){
        newPlugins[i] = listPlugins[index];
        listPlugins[index] = -1
        index = (index + nbPluginsOriginal) % listPlugins.length;
        while(listPlugins == -1){
          index++;
        }
    }
 
    return newPlugins;

  }
};


/* Screen object */
console.log("current width : "+screen.width);
Object.defineProperty(screen, 'width', {
    get: function(){myController.navigatorAccessed();return newWidth;}
});

Object.defineProperty(screen, 'height', {
    get: function(){myController.navigatorAccessed();return newHeight;}
});

Object.defineProperty(screen, 'colorDepth', {
  get: function(){myController.navigatorAccessed();return newColorDepth;}
});

Object.defineProperty(screen, 'availWidth', {
  get: function(){myController.navigatorAccessed();return availWidth;}
});

Object.defineProperty(screen, 'availHeight', {
  get: function(){myController.navigatorAccessed();return availHeight;}
});

Object.defineProperty(screen, 'pixelDepth', {
  get: function(){myController.navigatorAccessed();return pixelDepth;}
});

/* Navigator object */

//App info
Object.defineProperty(navigator, 'appName', {
  get: function(){myController.navigatorAccessed();return appName;}
});

Object.defineProperty(navigator, 'appVersion', {
  get: function(){myController.navigatorAccessed();return appVersion;}
});

Object.defineProperty(navigator, 'appCodeName', {
  get: function(){myController.navigatorAccessed();return appCodeName;}
});

//Language and languages should be set using the value generated in python
Object.defineProperty(navigator, 'language', {
  get: function(){myController.navigatorAccessed();return language;}
});

Object.defineProperty(navigator, 'languages', {
  get: function(){myController.navigatorAccessed();return languages;}
});

Object.defineProperty(navigator, 'platform', {
  get: function(){myController.navigatorAccessed();return platform;}
});

Object.defineProperty(navigator, 'product', {
  get: function(){myController.navigatorAccessed();return 'fake product';}
});

Object.defineProperty(navigator, 'productSub', {
  get: function(){myController.navigatorAccessed();return 'fake productSub';}
});

Object.defineProperty(navigator, 'vendor', {
  get: function(){myController.navigatorAccessed();return 'fake vendor';}
});

Object.defineProperty(navigator, 'vendorSub', {
  get: function(){myController.navigatorAccessed();return 'fake vendorSub';}
});

Object.defineProperty(navigator, 'buildID', {
  get: function(){myController.navigatorAccessed();return 'fake buildID';}
});



//Oscpu : avalaible only on firefox
//Create only if firefox ! 
Object.defineProperty(navigator, 'oscpu', {
  get: function(){myController.navigatorAccessed();return 'fake oscpu';}
});

//cookies enabled
Object.defineProperty(navigator, 'cookieEnabled', {
  get: function(){myController.navigatorAccessed();return 'fake cookie';}
});

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

navigator.javaEnabled = function(){
  return true;
}

//We lie to give the impression that we are on chrome
//We delete navigator properties which are only on firefox
delete Object.getPrototypeOf(navigator).buildID;
delete Object.getPrototypeOf(navigator).battery;
delete Object.getPrototypeOf(navigator).mediaDevices;
delete Object.getPrototypeOf(navigator).mozGetUserMedia;
delete Object.getPrototypeOf(navigator).oscpu;
delete Object.getPrototypeOf(navigator).registerContentHandler;
delete Object.getPrototypeOf(navigator).taintEnabled;

Object.defineProperty(navigator, 'mozPay', {
  get: function(){myController.navigatorAccessed();return "undefined";}
});

Object.defineProperty(navigator, 'mozContacts', {
  get: function(){myController.navigatorAccessed();return "undefined";}
});

Object.defineProperty(navigator, 'mozApps', {
  get: function(){myController.navigatorAccessed();return "undefined";}
});

Object.defineProperty(navigator, 'mozTCPSocket', {
  get: function(){myController.navigatorAccessed();return "undefined";}
});

//we add navigator properties which are on chrome but not on firefox
//navigator.prototype.getBattery = new Object();
navigator.__proto__["getBattery"] =function(){
    return new Object();
}
navigator.getBattery = function(){
    return new Object();
}

navigator.__proto__["getStorageUpdates"] ="getStorageUpdates";
navigator.getStorageUpdates = function(){
    return new Object();
}

navigator.__proto__["maxTouchPoints"] ="maxTouchPoints";
Object.defineProperty(navigator, 'maxTouchPoints', {
  get: function(){myController.navigatorAccessed();return 0;}
});

navigator.__proto__["permissions"] ="permissions";
Object.defineProperty(navigator, 'permissions', {
  get: function(){myController.navigatorAccessed();return new Object();}
});

navigator.__proto__["requestMIDIAccess"] ="requestMIDIAccess";
navigator.requestMIDIAccess = function(){
    return new Object();
}

navigator.__proto__["serviceWorker"] ="serviceWorker";
Object.defineProperty(navigator, 'serviceWorker', {
  get: function(){myController.navigatorAccessed();return new Object();}
});

navigator.__proto__["unregisterProtocolHandler"] ="unregisterProtocolHandler";
navigator.unregisterProtocolHandler = function(a, b){
    return new Object();
}

navigator.__proto__["webkitGetUserMedia"] ="webkitGetUserMedia";
navigator.unregisterProtocolHandler = function(a, b, c){
    return new Object();
}

navigator.__proto__["webkitPersistentStorage"] ="webkitPersistentStorage";
Object.defineProperty(navigator, 'webkitPersistentStorage', {
  get: function(){myController.navigatorAccessed();return new Object();}
});

navigator.__proto__["webkitTemporaryStorage"] ="webkitTemporaryStorage";
Object.defineProperty(navigator, 'webkitTemporaryStorage', {
  get: function(){myController.navigatorAccessed();return new Object();}
});


//navigator.getStorageUpdates()
/*
navigator.getStorageUpdates = function(){
   return new Object();
}
*/
//randomizer auto complete des formulaires
  
 
