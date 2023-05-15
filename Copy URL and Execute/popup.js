chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === "clickButton") {
    var myButton = document.getElementById("copy-url");
    if (myButton) {
      myButton.click();
    }
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var copyUrlButton = document.getElementById("copy-url");

  copyUrlButton.addEventListener("click", function () {
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
});
