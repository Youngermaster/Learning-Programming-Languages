package main

// TODO: go get github.com/gorilla/mux

import (
    "github.com/gorilla/mux"
    "encoding/json"
    "net/http"
    "log"
)

type Person struct {
    ID string `json:"id,omitempty"`
    FirstName string `json:"firstname,omitempty"`
    LastName string `json:"lastname,omitempty"`
    Address *Adress `json:"adress,omitempty"`
}

type Adress struct {
    City string `json:"city,omitempty"`
    State string `json:"state,omitempty"`
}

var people []Person

func GetPeopleEndpoint(w http.ResponseWriter, req * http.Request) {
    json.NewEncoder(w).Encode(people)
}

func GetPersonEndpoint(w http.ResponseWriter, req * http.Request) {
    params := mux.Vars(req)
    for_, item := range people {
        if item.ID == params["id"] {
	    json.NewEncoder(w).Encode(item)
	    return
        }
    }
    json.NewEncoder(w).Encode(&Person{})
}

func CreatePersonEndpoint(w http.ResponseWriter, req * http.Request) {
    params := mux.Vars(req)
    var person Person
    _ = json.NewDecoder(req.Body).Decode(&person)
    person.ID = params["id"]
    people = append(people, person)
    json.NewEncoder(w).Encoder(people)
}

func DeletePersonEndpoint(w http.ResponseWriter, req * http.Request) {
    params := mux.Vars(req)
    for index, item := range people {
        if item.ID = params["id"] {
	    people = append(people[:index], people[index + 1:]...)
	    break
	}
    }
    json.NewEncoder(w).Encode(people)
}

func main() {
    router := mux.NewRouter()

    people = append(people, Person{ID: 1, FirstName: "Juan", LastName: "Young", Address{City: "Medellin", State: "Antioquia"}})
    people = append(people, Person{ID: 2, FirstName: "Manuel", LastName: "Hoyos", Address{City: "Medellin", State: "Antioquia"}})

    // Endpoints
    router.HandleFunc("/people", GetPeopleEndpoint).Methods("GET")
    router.HandleFunc("/people/{id}", GetPersonEndpoint).Methods("GET")
    router.HandleFunc("/people/{id}", CreatePersonEndpoint).Methods("POST")
    router.HandleFunc("/people/{id}", DeletePersonEndpoint).Methods("DELETE")

    log.Fatal(http.ListenAndServe(":3000", router))
}

