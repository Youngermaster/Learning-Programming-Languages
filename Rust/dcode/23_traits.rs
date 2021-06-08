struct Person {
    name: String,
    age: u8,
}

impl ToString for Person {
    fn to_string(&self) -> String {
        format!("My name is {} and my age is {}.", self.name, self.age)
    }
}

fn main() {
    let juan = Person {
        name: String::from("Juan"),
        age: 20,
    };

    println!("{}", juan.to_string());
}
