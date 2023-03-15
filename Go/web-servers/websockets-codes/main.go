package main

import (
	"log"
	"net/http"

	socketio "github.com/googollee/go-socket.io"
)

func main() {
	server := socketio.NewServer(nil)

	var list []string

	server.OnConnect("/", func(s socketio.Conn) error {
		log.Println("connected:", s.ID())
		return nil
	})

	server.OnEvent("/", "append", func(s socketio.Conn, item string) {
		list = append(list, item)
		log.Println("append:", item)
		s.Emit("list", list)
	})

	server.OnEvent("/", "delete", func(s socketio.Conn, index int) {
		if index >= 0 && index < len(list) {
			item := list[index]
			list = append(list[:index], list[index+1:]...)
			log.Println("delete:", item)
			s.Emit("list", list)
		}
	})

	server.OnError("/", func(s socketio.Conn, e error) {
		log.Println("error:", e)
	})

	server.OnDisconnect("/", func(s socketio.Conn, reason string) {
		log.Println("closed", reason)
	})

	go server.Serve()
	defer server.Close()

	http.Handle("/socket.io/", server)
	http.Handle("/", http.FileServer(http.Dir("./public")))
	log.Println("Server started")
	log.Fatal(http.ListenAndServe(":3000", nil))
}
