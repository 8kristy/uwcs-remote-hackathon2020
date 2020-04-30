
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

// sends the processes text to the backend (currently using local,
// ideally would be hosted remotely)
xhr = new XMLHttpRequest();
xhr.open('POST', 'http://127.0.0.1:5000/', true);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.onload = function() {
  if (xhr.status === 200) {
      // just to show that something happens for now
      alert(xhr.responseText);
  }
};
xhr.send(modifyDOM());


chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
    // If the received message has the expected format...
    if (msg.text === 'report_back_full') {
        // Call the specified callback, passing
        // the web-page's DOM content as argument
        result = modifyDOM();
        sendResponse(result); //this returns full page of stripped html, need to try and remove certain heading and list parts
    }
})
