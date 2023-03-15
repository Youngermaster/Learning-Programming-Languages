package main

import (
	"fmt"
	"log"
	"net/http"

	socketio "github.com/googollee/go-socket.io"
)

type Todo struct {
	Name string `json:"name"`
	Done bool   `json:"done"`
}

var todoList []Todo

func main() {
	server := socketio.NewServer(nil)
	// server, err := socketio.NewServer(nil)
	// if err != nil {
	// 	log.Fatal(err)
	// }

	server.OnConnect("/", func(s socketio.Conn) error {
		s.Emit("list", todoList)
		return nil
	})

	server.OnEvent("/", "add", func(s socketio.Conn, todo Todo) {
		todoList = append(todoList, todo)
		server.BroadcastToRoom("/", "", "list", todoList)
	})

	server.OnEvent("/", "delete", func(s socketio.Conn, index int) {
		if index >= 0 && index < len(todoList) {
			todoList = append(todoList[:index], todoList[index+1:]...)
			server.BroadcastToRoom("/", "", "list", todoList)
		}
	})

	server.OnError("/", func(s socketio.Conn, e error) {
		fmt.Println("Error:", e)
	})

	server.OnDisconnect("/", func(s socketio.Conn, reason string) {
		fmt.Println("closed client namespace disconnect")
	})

	go server.Serve()
	defer server.Close()

	http.Handle("/socket.io/", server)
	http.Handle("/", http.FileServer(http.Dir("./public")))

	fmt.Println("Server started at http://localhost:3000")
	log.Fatal(http.ListenAndServe(":3000", nil))
}
