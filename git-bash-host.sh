#!/usr/bin/env bash

# Read the entire message from the extension
# read -r message

# echo "$message"

# Parse the message as JSON to extract the URL
# url=$(echo "$message" | jq -r '.url')

# Execute the command using Git Bash
# yt-dlp.exe -f 140 "$url"


# Loop forever, to deal with chrome.runtime.connectNative
while IFS= read -r -n1 c; do
    # Read the first message
    # Assuming that the message ALWAYS ends with a },
    # with no }s in the string. Adopt this piece of code if needed.
    if [ "$c" != '}' ] ; then
        continue
    fi

    message='{"message": "Hello world!"}'
    # Calculate the byte size of the string.
    # NOTE: This assumes that byte length is identical to the string length!
    # Do not use multibyte (unicode) characters, escape them instead, e.g.
    # message='"Some unicode character:\u1234"'
    messagelen=${#message}

    # Convert to an integer in native byte order.
    # If you see an error message in Chrome's stdout with
    # "Native Messaging host tried sending a message that is ... bytes long.",
    # then just swap the order, i.e. messagelen1 <-> messagelen4 and
    # messagelen2 <-> messagelen3
    messagelen1=$(( ($messagelen      ) & 0xFF ))               
    messagelen2=$(( ($messagelen >>  8) & 0xFF ))               
    messagelen3=$(( ($messagelen >> 16) & 0xFF ))               
    messagelen4=$(( ($messagelen >> 24) & 0xFF ))               

    # Print the message byte length followed by the actual message.
    printf "$(printf '\\x%x\\x%x\\x%x\\x%x' \
        $messagelen1 $messagelen2 $messagelen3 $messagelen4)%s" "$message"

done