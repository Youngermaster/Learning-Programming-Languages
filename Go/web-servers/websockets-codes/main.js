const WebSocket = require('ws');

const socket = new WebSocket('ws://localhost:6942/ws/123?v=1.0');

socket.on('open', function () {
    console.log('Connection established.');
});

socket.on('message', function (data) {
    console.log('Received message:', data);
});

socket.on('close', function () {
    console.log('Connection closed.');
});
