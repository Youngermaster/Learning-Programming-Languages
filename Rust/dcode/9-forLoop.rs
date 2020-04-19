fn main() {
    let range = 30..51;

    for i in range {
        println!("the value is {}", i);
    }

    let animals = vec!["Lion", "Rabbit", "Owl", "Eagle"];
    for animal in animals.iter() {
        println!("The animal is {}", animal);
    }

    for (index, animal) in animals.iter().enumerate() {
        println!("The animal index is {} and the animal name is {}", index, animal);
    }
}