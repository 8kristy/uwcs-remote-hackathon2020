chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
    // If the received message has the expected format...
    if (msg.text === 'report_back_full') {
        // Call the specified callback, passing
        // the web-page's DOM content as argument
        sendResponse(document.all[0].innerText); //this returns full page of stripped html, need to try and remove certain heading and list parts
});
