function doStuffWithDom(domContent) {
    //here will be where we end up sending the content to the backend i think
    return domContent;
}

console.log("in background");
chrome.tabs.onUpdated.addListener( function (tabId, changeInfo, tab) {
  console.log(changeInfo.status);
  if (changeInfo.status == 'complete' && tab.active) {
    console.log("in if statement");
    //chrome.tabs.sendMessage(tab.id, {text: 'report_back_full'}, doStuffWithDom);
    }
  });
