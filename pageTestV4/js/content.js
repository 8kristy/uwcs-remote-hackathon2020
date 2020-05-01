
function modifyDOM() {
    var pElements = document.getElementsByTagName("P");
    var pageText = document.title + '\n';
    for (index = 0; index < pElements.length; ++index) {
        if (pElements[index].innerText.length > 68 && pElements[index].innerText.split(" ").length > 7) {
            //console.log(pElements[index].innerText);
            pageText = pageText + "\n" + pElements[index].innerText;
            //console.log(pElements[index].innerText.length)
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
    if (!((window.location.pathname.length < 17))) { //checks that the length of the pathname is not less than 17
        var title = document.title.toLowerCase();
        var newsKeywords = document.getElementsByName('news_keywords')[0];

        if ((title.includes("news")) || (newsKeywords != undefined)) {
            makeDiv(xhr.responseText); // takes the answer it got and passes it to make the alert
        } else {
            var x = document.getElementsByTagName("META");
            var i;
            var content;
            for (i = 0; i < x.length; i++) {
                content = x[i].content.toLowerCase();
                if (content.includes("news")) {
                    makeDiv(xhr.responseText); // takes the answer it got and passes it to make the alert
                    break;
                }
            }
        } 
    }
  }
};
xhr.send(modifyDOM());

var dict = {0: "neutral", 1: "biased", 2: "satire", 3:"fake"};

function makeDiv(text) {
    title = parseInt(text.substring(0,1));
    content = parseInt(text.substring(1));

    var div = document.createElement("DIV");

    var popupTitle = document.createElement("H1");
    var warning = document.createElement("p");
    var moreInfo = document.createElement("p");

    popupTitle.className = "text";
    warning.className = "text";
    moreInfo.className = "text";

    popupTitle.style.fontSize = "5vh";
    popupTitle.style.fontWeight = "bold";

    warning.style.fontSize = "2.5vh";

    moreInfo.style.fontSize = "1.8vh";


    if (title !== 0 || content !== 0){
        popupTitle.innerHTML = "Warning";
        if (title === content){
            warning.innerHTML = "The title and content of this article suggest that it might be " + dict[title];
        }
        else if (content === 0){
            warning.innerHTML = "The title of this article suggests that it might be " + dict[title];
        }
        else if (title === 0){
            warning.innerHTML = "The content of this article suggests that it might be " + dict[content];
        }
        else{
            warning.innerHTML = "The title of this article suggests that it might be " + dict[title] + " and the content suggests that it might be " + dict[content];
        }
    }
    else{
        popupTitle.innerHTML = "OK";
        warning.innerHTML = "Everything seems to be okay"
    }

    var infoText = "";
    if (title === 0 && content === 0){
        infoText = "The article doesn't seem to be of harmful nature, but you still should use your own judgement to determine if it is valid. It is recommended to check other sources to see if the information mathces up."
    }
    if (title === 1 || content === 1){
        infoText = infoText + "The person who wrote this article may have extreme opinions leaning towards one side of the argument. It is advised to consider the other side to see the full picture.\n"
    }
    if (title === 2 || content === 2){
        infoText = infoText + "Satire articles are written as a joke. The information in them is likely untrue and shouldn't be taken seriously.\n"
    }
    if (title === 3 || content == 3){
        infoText = infoText + "Fake news, stories or hoaxes are created to deliberately misinform or deceive readers. Please do your own research about this topic from reputable sources.\n"
    }

    moreInfo.innerHTML = infoText;

    div.appendChild(popupTitle);
    div.appendChild(warning);
    div.appendChild(moreInfo);
    div.style.position = "fixed";
    div.id = "hello_text_id"
    document.body.appendChild(div);
}



chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
    // If the received message has the expected format...
    if (msg.text === 'report_back_full') {
        // Call the specified callback, passing
        // the web-page's DOM content as argument
        result = modifyDOM();
        sendResponse(result); //this returns full page of stripped html, need to try and remove certain heading and list parts
    }
})
