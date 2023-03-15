const socket = require('socket.io-client')('http://localhost:3000');

socket.on('connect', () => {
    console.log('Connected to server');

    socket.on('list', (todoList) => {
        console.log('Todo list:', todoList);
    });

    socket.on('disconnect', () => {
        console.log('Disconnected from server');
    });

    socket.emit('add', { name: 'Task 1', done: false });
    socket.emit('add', { name: 'Task 2', done: true });

    setTimeout(() => {
        socket.emit('delete', 0);
    }, 2000);
});

socket.on('connect_error', (err) => {
    console.log('Connection error:', err);
});
