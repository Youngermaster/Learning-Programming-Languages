const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost:3000');

ws.on('open', function open() {
    console.log('WebSocket connection opened');
    ws.send('Hello, server!');
});

ws.on('message', function incoming(message) {
    console.log(`Received message: ${message}`);
});

ws.on('close', function close() {
    console.log('WebSocket connection closed');
});
