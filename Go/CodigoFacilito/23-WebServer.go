package main

import (
	"net/http"
	"io"
)

func main() {
	http.HandleFunc("/", homeHandler)
	http.HandleFunc("/login", loginHandler)
	http.HandleFunc("/hello", helloHandler)
	http.HandleFunc("/test", testHandler)

	println("Server started at http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "public/index.html")
	println("/ Path requested.")
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	// * This is another way to serve files
	// string := "public/"
	http.ServeFile(w, r, "public/" + r.URL.Path[1:] + ".html")
	println(r.URL.Path[1:])
	println("/login Path requested.")
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hello Web")
	println("/hello Path requested.")
}

func testHandler(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Test")
	println("/test Path requested.")
}