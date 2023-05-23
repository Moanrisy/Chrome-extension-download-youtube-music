import struct
import sys
import os
import json
import subprocess

# On Windows, the default I/O mode is O_TEXT. Set this to O_BINARY
# to avoid unwanted modifications of the input/output streams.
if sys.platform == "win32":
  import msvcrt
  msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
  msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

# Thread that reads messages from the webapp.
def read_thread_func():
  while True:
    # Read the message length (first 4 bytes).
    text_length_bytes = sys.stdin.read(4)
         
    if not text_length_bytes:
      sys.exit(0)
    
    # Unpack message length as 4 byte integer.
    text_length = struct.unpack('=I', text_length_bytes)[0]
    # Read the text (JSON object) of the message.
    text = sys.stdin.read(text_length).encode("utf-8")

    json_object = json.loads(text)

    if (os.path.exists('./data')):
      with open('./data', 'wb') as f:
        f.write(json_object['url'])
        f.close()

        url = json_object['url']
        directory = '/c/users/moanr/music/unrenamed'
        command = 'yt-dlp.exe -o "%(artist)s - %(title)s.%(ext)s" -f 140 ' + url
        
        # Construct the command to be executed by Git Bash
        # this work but git bash didn't auto close when complete
        ## git_bash_command = 'cd "{0}" && {1}; bash'.format(directory, command)
        git_bash_command = 'cd "{0}" && start /WAIT {1} && exit'.format(directory, command)
        
        # Launch Git Bash with the command
        subprocess.Popen(['git-bash.exe', '-c', git_bash_command], shell=True)

    else:
      with open('./data', 'xb') as f:
        f.write(text)
        f.close()

# Helper function that sends a message to the webapp.
def send_message(message):
  # Write message size.
  sys.stdout.write(struct.pack('=I', len(message.encode("utf-8"))))
  
  # Write the message itself.
  sys.stdout.write(struct.pack(str(len(message.encode("utf-8")))+"s", message.encode("utf-8")))
  sys.stdout.flush()

def index():
  # send_message('{"msg": "Hello World!"}')
  read_thread_func()

if __name__ == '__main__':
  index()