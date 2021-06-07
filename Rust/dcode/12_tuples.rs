fn main() {
    let tup_1 = (20, 25, 30, 35);
    let tup_2 = (20, "Rust", 3.14, true, (1, 4, 7));

    println!("Tuple 1 -> {}", tup_1.2);
    println!("Tuple 2 -> {}", tup_2.2);
    println!("Tuple 2 -> {}", (tup_2.4).2);

    let tup_3 = ("a", "b", "c");
    let (a, b, c) = tup_3;

    println!("{}, {}, {}", a, b, c);
}