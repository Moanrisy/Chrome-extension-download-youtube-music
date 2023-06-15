console.log("Background loaded");

chrome.action.onClicked.addListener(function (tab) {
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