struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    let color = Color {
        red: 255,
        green: 23,
        blue: 255,
    };

    println!("RGB => {}, {}, {}", color.red, color.green, color.blue);

    let mut color = Color {
        red: 255,
        green: 23,
        blue: 255,
    };

    color.green = 255;
    println!("RGB => {}, {}, {}", color.red, color.green, color.blue);
}
