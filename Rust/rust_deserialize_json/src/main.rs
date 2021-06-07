// use serde::{Deserialize, Serialize};
use serde::Deserialize;

// #[derive(Serialize, Deserialize, Debug)]
// struct Point {
//     x: i32,
//     y: i32,
// }

// fn main() {
//     let point = Point { x: 1, y: 2 };

//     // Convert the Point to a JSON string.
//     let serialized = serde_json::to_string(&point).unwrap();

//     // Prints serialized = {"x":1,"y":2}
//     println!("serialized = {}", serialized);

//     // Convert the JSON string back to a Point.
//     let deserialized: Point = serde_json::from_str(&serialized).unwrap();

//     // Prints deserialized = Point { x: 1, y: 2 }
//     println!("deserialized = {:?}", deserialized);
// }

// #[macro_use]
// extern crate serde_derive;
use serde_json::Result;
fn main() -> Result<()> {
    let data = r#"
    [
      {
        "id": 1,
        "type": "personal",
        "details": {
          "firstName": "Juliano",
          "lastName": "Alves",
          "primaryAddress": 7777777
        }
      },
      {
        "id": 2,
        "type": "business",
        "details": {
          "name": "Juliano Business",
          "companyRole": "OWNER",
          "primaryAddress": 8888888
        }
      }
    ]
    "#;
    let profiles: Vec<Profile> = serde_json::from_str(data)?;
    println!("{:#?}", profiles);
    Ok(())
}
#[derive(Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
struct PersonalDetails {
    first_name: String,
    last_name: String,
    primary_address: i32,
}
#[derive(Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
struct BusinessDetails {
    name: String,
    company_role: String,
    primary_address: i32,
}
#[derive(Deserialize, Debug)]
#[serde(tag = "type", rename_all = "camelCase")]
enum Profile {
    Personal { id: i32, details: PersonalDetails },
    Business { id: i32, details: BusinessDetails },
}
