const express = require('express');
const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

app.use(express.static(__dirname + '/public'));

let list = ['AC01', 'AC02', 'AC03'];

io.on('connection', (socket) => {
    console.log('a user connected');

    socket.emit('list', list);

    socket.on('add', (item) => {
        console.log('adding item:', item);
        list.push(item);
        io.emit('list', list);
    });

    socket.on('delete', (index) => {
        console.log('deleting item at index:', index);
        list.splice(index, 1);
        io.emit('list', list);
    });

    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
});

http.listen(3000, () => {
    console.log('listening on *:3000');
});
