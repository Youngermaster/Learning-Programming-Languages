struct Color(u8, u8, u8);

fn main() {
    let red = Color(255, 0, 0);

    println!("The color Red in RGB is: {}, {}, {}.", red.0, red.1, red.2);

    let mut red = Color(255, 0, 0);

    red.2 = 60;

    println!("The mutable Red in RGB is: {}, {}, {}.", red.0, red.1, red.2);
}
