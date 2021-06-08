fn main() {
    let numbers: [i32; 5] = [10, 20, 30, 40, 50];

    for number in numbers.iter() {
        println!("{}", number);
    }

    for i in 0..numbers.len() {
        println!("{}", numbers[i]);
    }

    let array_of_2 = [2; 5];
    for number in array_of_2.iter() {
        println!("{}", number);
    }
}
