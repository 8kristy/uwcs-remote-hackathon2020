// sends a post request to the backend so that the popup html file can be changed 
function callPopupPost(div){
      xhr = new XMLHttpRequest();
      xhr.open('POST', 'http://127.0.0.1:5000/popup', true);
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.onload = function () { };
      xhr.send(div);
}

// keeps all the tab ids and div html for each tab so that the popup
// can be changed when the active tab is changed; not the best way to 
// keep track of it but hey it works and i'm not willing to deal with 
// messages for another day
var tabs = {};

// same as tabs but for icons
var icons = {};

// changes the popup and adds the div html to the tabs dict after a new page
// with news in it is opened (message sent from content script)
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  chrome.tabs.query({ currentWindow: true, active: true }, function (tabArray) {
    tabs[tabArray[0].id] = request.text;
    icons[tabArray[0].id] = request.icon;
    callPopupPost(request.text);
    chrome.browserAction.setPopup({ popup: "index.html" });
    chrome.browserAction.setIcon({path: "icons/" + request.icon + "48.png"});
  });
});

// changes the popup html when the active tab is changed.
// if the tab was recorded to have news, changes the popup html
// in backend to the div recorded, otherwise sets it to default "no news"
chrome.tabs.onActiveChanged.addListener(function () {
  chrome.tabs.query({ currentWindow: true, active: true }, function (tabArray) {
    if (!(tabArray[0].id in tabs)) {
      chrome.browserAction.setPopup({ popup: "default.html" });
      chrome.browserAction.setIcon({path: "icons/icon16.png" });
    }
    else {
      callPopupPost(tabs[tabArray[0].id]);
      chrome.browserAction.setPopup({ popup: "index.html" });
      chrome.browserAction.setIcon({path: "icons/" + icons[tabArray[0].id] + "48.png"});
    }
  });
})

