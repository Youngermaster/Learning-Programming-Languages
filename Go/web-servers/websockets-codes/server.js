const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 3000 });

wss.on('connection', function connection(ws) {
    console.log('WebSocket connection established');

    ws.on('message', function incoming(message) {
        console.log(`Received message: ${message}`);
        ws.send(`Echoing back message: ${message}`);
    });

    ws.on('close', function close() {
        console.log('WebSocket connection closed');
    });
});
