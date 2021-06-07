fn main() {
    print_numbers_to(10);
    let num = 21;
    println!("is {} even? {}", num, is_even(num));
}

fn print_numbers_to(end: u32) {
    for n in 1..end {
        if is_even(n) {
            println!("{} is even", n);
        } else {
            println!("{} is odd", n);
        }
    }
}

fn is_even(num: u32) -> bool {
    num % 2 == 0
}