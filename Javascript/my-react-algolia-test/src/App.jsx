import React from "react";
import ReactDOM from "react-dom";
import "./App.css";
import algoliasearch from "algoliasearch/lite";
import { InstantSearch, SearchBox, Hits } from "react-instantsearch";

// Change the appId and apiKey to the values of your Algolia account
const searchClient = algoliasearch("appId", "apiKey");

const App = () => (
  // Change the indexName to the name of your index on Algolia
  <InstantSearch indexName="products" searchClient={searchClient}>
    <SearchBox />
    <Hits />
  </InstantSearch>
);

export default App;
