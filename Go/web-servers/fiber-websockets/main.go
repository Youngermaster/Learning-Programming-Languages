package main

import (
	"log"
	"net/http"

	"github.com/googollee/go-socket.io"
)

func main() {
	server := socketio.NewServer(nil)

	server.OnConnect("/", func(s socketio.Conn) error {
		log.Println("client connected")
		return nil
	})

	server.OnEvent("/", "add", func(s socketio.Conn, item string) {
		log.Println("add:", item)
		server.BroadcastToRoom("/", "room", "add", item)
	})

	server.OnEvent("/", "delete", func(s socketio.Conn, item string) {
		log.Println("delete:", item)
		server.BroadcastToRoom("/", "room", "delete", item)
	})

	server.OnDisconnect("/", func(s socketio.Conn, reason string) {
		log.Println("client disconnected")
	})

	http.Handle("/socket.io/", server)
	http.Handle("/", http.FileServer(http.Dir("./public")))
	log.Println("Server started at :3000")
	log.Fatal(http.ListenAndServe(":3000", nil))
}
