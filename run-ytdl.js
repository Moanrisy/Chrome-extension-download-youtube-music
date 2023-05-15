const readline = require('readline');
const fs = require('fs');

const logFilePath = 'native_host.log';

// Create an interface to read messages from the extension
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

// Create a write stream to the log file
const logStream = fs.createWriteStream(logFilePath, { flags: 'a' });

// Read messages from the extension
rl.on('line', (message) => {
  try {
    const parsedMessage = JSON.parse(message);

    // Process the received message
    handleMessage(parsedMessage);
  } catch (error) {
    logError('Error processing message:', message);
    logError(error);
  }
});

function handleMessage(message) {
  // Handle the received message as needed
  logInfo('Received message:', message);

  // Example: Sending a response back to the extension
  const response = { status: 'success' };
  sendMessage(response);
}

function sendMessage(message) {
  // Send a message back to the extension
  const responseString = JSON.stringify(message);
  logInfo(responseString);
}

function logInfo(...args) {
  const logMessage = args.join(' ');
  console.log(logMessage);
  logStream.write(`[INFO] ${logMessage}\n`);
}

function logError(...args) {
  const logMessage = args.join(' ');
  console.error(logMessage);
  logStream.write(`[ERROR] ${logMessage}\n`);
}
