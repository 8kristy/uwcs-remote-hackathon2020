
// I used this news article as an example https://www.bbc.co.uk/news/uk-52462928

document.getElementById("test").addEventListener('click', () => {
    console.log("Popup DOM fully loaded and parsed");

    function modifyDOM() {
        console.log(document.title);
        // console.log(document.body.innerText);
        var pElements = document.getElementsByTagName("P");
        var thisScore = 0;
        for (index = 0; index < pElements.length; ++index) {
            //console.log(pElements[index].innerText);
            //console.log(pElements[index].innerText.length);
            if (pElements[index].innerText.length > 60) {
                console.log(pElements[index].innerText);
                console.log(pElements[index].innerText.length)
            }
        }
        return document.body.innerHTML;
    }

    //We have permission to access the activeTab, so we can call chrome.tabs.executeScript:
    chrome.tabs.executeScript({
        code: '(' + modifyDOM + ')();' //argument here is a string but function.toString() returns function's code
    }, (results) => {
        //Here we have just the innerHTML and not DOM structure
        console.log('Popup script:')
        console.log(results[0]);
    });
});