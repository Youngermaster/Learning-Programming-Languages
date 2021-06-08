fn main() {
    let mut my_vector: Vec<i32> = Vec::new();
    let mut default_vector = vec![1, 2, 3, 4];

    my_vector.push(69);

    println!("{}", default_vector[3]);
    
    default_vector.remove(1); // removes the number '2'

    for number in default_vector.iter() {
        println!("{}", number);
    }
}