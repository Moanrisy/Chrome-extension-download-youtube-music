console.log("Background loaded");

chrome.browserAction.onClicked.addListener(function (tab) {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var url = tabs[0].url;

    var message = {
      url: url,
    };

    // Send the native message
    chrome.runtime.sendNativeMessage(
      "com.moanrisy.gitbash",
      message,
      function (response) {
        console.log("Response:", response);
      }
    );
  });
});

chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  var url = message.url;
  chrome.tabs.executeScript(
    null,
    { code: "window.getSelection().removeAllRanges();" },
    function () {
      chrome.runtime.sendNativeMessage(
        "com.moanrisy.gitbash",
        { url: url },
        function (response) {
          sendResponse(response);
        }
      );
    }
  );
  return true;
});
