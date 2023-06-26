#!/usr/bin/env python

import struct
import sys
import json
import os
import subprocess

# Open a file to write the log
log_file = open('native_host.log', 'w')

def read_message():
    raw_length = sys.stdin.buffer.read(4)
    if len(raw_length) == 0:
        sys.exit(0)
    message_length = struct.unpack('@I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode('utf-8')

    json_object = json.loads(message)
    url = json_object['url']
    directory = '/mnt/storage/Music/unrenamed'

    command = 'yt-dlp --no-playlist -o "%(artist)s - %(title)s.%(ext)s" -f 140 ' + url
    konsole_command = f'konsole --workdir {directory} -e \'{command}\''
    subprocess.run(konsole_command, shell=True)

    # git_bash_command = 'cd "{0}" && {1}'.format(directory, command)
    # subprocess.Popen(['bash', '-c', git_bash_command])

    log_file.write(konsole_command)

    return json.loads(message)

def write_message(message_content):
    encoded_message = json.dumps(message_content).encode('utf-8')
    sys.stdout.buffer.write(struct.pack('@I', len(encoded_message)))
    sys.stdout.buffer.write(encoded_message)
    sys.stdout.buffer.flush()

while True:
    received_message = read_message()
    
    # Write the received message to the log file
    # log_file.write("Received message: {}\n".format(received_message))
    
    # Example: Reverse the received message
    reversed_message = received_message[::-1]
    
    response_message = {
        'result': reversed_message
    }
    
    # Write the response to the log file
    log_file.write("Sending response: {}\n".format(response_message))
    
    write_message(response_message)

# Close the log file before exiting
log_file.close()
