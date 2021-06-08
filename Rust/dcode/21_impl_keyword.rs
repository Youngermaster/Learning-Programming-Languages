struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn print_description(&self) {
        println!("The rectangle is {} x {}", self.width, self.height);
    }

    fn is_square(&self) -> bool {
        self.width == self.height
    }
}

fn main() {
    let my_rectangle = Rectangle {
        width: 100,
        height: 100,
    };

    my_rectangle.print_description();
    println!("Is my rectangle a square? {}", my_rectangle.is_square());
}
