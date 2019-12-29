package main

import (
	"encoding/json"
	"net/http"
)

type Course struct {
	Title          string `json:"title"`
	NumberOfVideos int    `json:"number of videos"`
}

type Courses []Course

func main() {
	http.HandleFunc("/", homeHandler)
	http.ListenAndServe(":8080", nil)
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	courses := Courses{
		Course{"Chief Factors Representative", 60293},
		Course{"Communications", 60293},
		Course{"Quality", 60293},
	}
	json.NewEncoder(w).Encode(&courses)
}
