package main

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
  Address *Address `json:"address,omitempty"`
}

type Address struct {
  City string `json:"city,omitempty"`
  State string `json:"state,omitempty"`
}

var people []Person

// EndPoints
func GetPersonEndpoint(w http.ResponseWriter, req *http.Request){
  params := mux.Vars(req)
  for _, item := range people {
    if item.ID == params["id"] {
      json.NewEncoder(w).Encode(item)
      return
    }
  }
  json.NewEncoder(w).Encode(&Person{})
}

func GetPeopleEndpoint(w http.ResponseWriter, req *http.Request){
  json.NewEncoder(w).Encode(people)
}

func CreatePersonEndpoint(w http.ResponseWriter, req *http.Request){
  params := mux.Vars(req)
  var person Person
  _ = json.NewDecoder(req.Body).Decode(&person)
  person.ID = params["id"]
  people = append(people, person)
  json.NewEncoder(w).Encode(people)

}

func DeletePersonEndpoint(w http.ResponseWriter, req *http.Request) {
  params := mux.Vars(req)
  for index, item := range people {
    if item.ID == params["id"] {
      people = append(people[:index], people[index + 1:]...)
      break
    }
  }
  json.NewEncoder(w).Encode(people)
}

func main() {
  router := mux.NewRouter()
  
  // adding example data
  people = append(people, Person{ID: "1", FirstName:"Juan", LastName:"Young", Address: &Address{City:"Medellín", State:"Antioquia"}})
  people = append(people, Person{ID: "2", FirstName:"Manuel", LastName:"Hoyos"})

  // endpoints
  router.HandleFunc("/people", GetPeopleEndpoint).Methods("GET")
  router.HandleFunc("/people/{id}", GetPersonEndpoint).Methods("GET")
  router.HandleFunc("/people/{id}", CreatePersonEndpoint).Methods("POST")
  router.HandleFunc("/people/{id}", DeletePersonEndpoint).Methods("DELETE")

  log.Fatal(http.ListenAndServe(":3000", router))
}