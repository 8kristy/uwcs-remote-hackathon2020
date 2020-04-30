function modifyDOM() {
    //console.log(document.title);
    // console.log(document.body.innerText);
    var pElements = document.getElementsByTagName("P");
    var pageText = document.title + '\n';
    for (index = 0; index < pElements.length; ++index) {
        //console.log(pElements[index].innerText);
        //console.log(pElements[index].innerText.length);
        if (pElements[index].innerText.length > 68 && pElements[index].innerText.split(" ").length > 7) {
            console.log(pElements[index].innerText);
            pageText = pageText + "\n" + pElements[index].innerText;
            console.log(pElements[index].innerText.length)
        }
    }
    return pageText;
}
chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
    // If the received message has the expected format...
    if (msg.text === 'report_back_full') {
        // Call the specified callback, passing
        // the web-page's DOM content as argument
        result = modifyDOM();
        sendResponse(result); //this returns full page of stripped html, need to try and remove certain heading and list parts
    }
});
