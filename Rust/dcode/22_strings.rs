fn main() {
    let mut my_string = String::from("How is it going? My name is Juan.");

    // Length
    println!("Length -> {}", my_string.len());
    // Is empty?
    println!("Is empty? {}", my_string.is_empty());

    // Separate by white spaces
    for (index, token) in my_string.split_whitespace().enumerate() {
        println!("{} - {}", index, token);
    }

    // Contains some value?
    println!(
        "Does the string contains Juan? {}",
        my_string.contains("Juan")
    );

    // Push a String onto the String
    // ! Make sure to have the string as mutable
    my_string.push_str(" Welcome to this tutorial.");

    println!("{}", my_string);
}
