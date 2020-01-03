package main

import (
	"encoding/json"
	"net/http"
)

type course struct {
	Title          string `json:"title"`
	NumberOfVideos int    `json:"number of videos"`
}

type courses []course

func main() {
	http.HandleFunc("/", homeHandler)
	http.ListenAndServe(":8080", nil)
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	courses := courses{
		course{"Chief Factors Representative", 60293},
		course{"Communications", 60293},
		course{"Quality", 60293},
	}
	json.NewEncoder(w).Encode(&courses)
}
