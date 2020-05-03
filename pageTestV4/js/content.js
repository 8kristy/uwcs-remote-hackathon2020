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
    xhr.onload = function () {
        if (xhr.status === 200) {
            if (!((window.location.pathname.length < 17))) { //checks that the length of the pathname is not less than 17
                var title = document.title.toLowerCase();
                var newsKeywords = document.getElementsByName('news_keywords')[0];

                if ((title.includes("news")) || (newsKeywords != undefined)) {
                    alert("this is news");
                    makeDiv(xhr.responseText); // takes the answer it got and passes it to make the popup
                } else {
                    var x = document.getElementsByTagName("META");
                    var i;
                    var content;
                    for (i = 0; i < x.length; i++) {
                        content = x[i].content.toLowerCase();
                        if (content.includes("news")) {
                            alert("this is news");
                            makeDiv(xhr.responseText); // takes the answer it got and passes it to make the alert
                            break;
                        }
                    }
                }
            }
        }
    };
    xhr.send(modifyDOM());



// map used to get words based on values; easier than making a case for each one
var dict = { 0: "neutral", 1: "biased", 2: "satire", 3: "fake" };

// main function which creates the div to be displayed; a mess. i'm sorry.
// TODO: add icons next to text, change extension logo to icon
function makeDiv(text) {
    // gets integer values of the warnings for both title and content
    title = parseInt(text.substring(0, 1));
    content = parseInt(text.substring(1));

    var div = document.createElement("DIV");

    // bits to be added to the div later
    var popupTitle = document.createElement("H1");
    var warning = document.createElement("p");
    var moreInfo = document.createElement("p");
    // setting the class for css purposes
    popupTitle.className = "text_of_extension";
    warning.className = "text_of_extension";
    moreInfo.className = "text_of_extension";

    // separately setting the attributes to avoid making more classes
    popupTitle.style.fontSize = "5vh";
    popupTitle.style.fontWeight = "bold";

    warning.style.fontSize = "2.5vh";

    moreInfo.style.fontSize = "1.8vh";

    // close button and it's attributes
    var closeBtn = document.createElement("button");

    closeBtn.innerHTML = "x";
    closeBtn.className = "close_button"
    closeBtn.onclick = function () {
        // removes the div when button is clicked
        document.getElementById("hello_text_id").remove();
    }

    // Adds the appropriate messages into the div
    if (title !== 0 || content !== 0) {
        popupTitle.innerHTML = "Warning";
        if (title === content) {
            warning.innerHTML = "The title and content of this article suggest that it might be " + dict[title].bold();
        }
        else if (content === 0) {
            warning.innerHTML = "The title of this article suggests that it might be " + dict[title].bold();
        }
        else if (title === 0) {
            warning.innerHTML = "The content of this article suggests that it might be " + dict[content].bold();
        }
        else {
            warning.innerHTML = "The title of this article suggests that it might be " + dict[title].bold() + " and the content suggests that it might be " + dict[content].bold();
        }
    }
    else {
        popupTitle.innerHTML = "OK";
        warning.innerHTML = "Everything seems to be " + "okay".bold();
    }

    var infoText  = "";
    var infoText  = "";  // some more text to be useful/fill the space
    var bckColor  = "";  // background colour of the div
    var textColor = "";  // text colour of the div content
    var iconType  = "";  // what icon to display in tab
 
    // determining the popup colours and setting additional messages
    if (title === 0 && content === 0) {
        bckColor = "rgb(235, 255, 234)";
        textColor = "rgb(2, 69, 0)";
        iconType = "good";
        infoText = "The article doesn't seem to be of harmful nature, but you still should use your own judgement to determine if it is valid. It is recommended to check other sources to see if the information matches up."
    }
    if (title === 1 || content === 1) {
        bckColor = "rgb(255, 244, 233)";
        textColor = "rgb(255, 119, 0)";
        iconType = "orange";
        infoText = infoText + "The person who wrote this article may have extreme opinions leaning towards one side of the argument. It is advised to consider the other side to see the full picture and seek out more neutral sources.\n"
    }
    if (title === 2 || content === 2) {
        bckColor = "rgb(255, 244, 233)";
        textColor = "rgb(255, 119, 0)";
        iconType = "orange";
        infoText = infoText + "Satire articles are written as a joke. The information in them is likely untrue and shouldn't be taken seriously.\n"
    }
    if (title === 3 || content == 3) {
        bckColor = "rgb(255, 221, 227)";
        textColor = "rgb(172, 23, 46)";
        iconType = "bad";
        infoText = infoText + "Fake news, stories or hoaxes are created to deliberately misinform or deceive readers. Please do your own research about this topic.\n"
    }

    moreInfo.innerHTML = infoText;

    // adding all of the stuff to the div
    div.appendChild(popupTitle);
    div.appendChild(warning);
    div.appendChild(moreInfo);
    //div.style.position = "fixed";
    div.appendChild(closeBtn);
    div.id = "hello_text_id"
    div.style.backgroundColor = bckColor;

    // changing the colour of all div text boxes at once
    var elements = div.getElementsByClassName("text_of_extension");
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.color = textColor;
    }

    // adding the div to the page
    if (!(title === 0 && content === 0)) {
        document.body.appendChild(div);
    }
    // sends the message to the extension to replace the popup
    // when it gets to python it turns into this weird dictionary thing
    // which messes things up with = so it's temporarily replaced
    chrome.runtime.sendMessage({ text: div.outerHTML.replace(/=/g, "£"), icon: iconType}, function (response) {});
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

