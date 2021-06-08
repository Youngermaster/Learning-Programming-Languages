use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::open("25_reading_files.txt").expect("Can't open the file");

    let mut file_content = String::new();

    file.read_to_string(&mut file_content)
        .expect("Can't copy the file content");

    println!("File content -> {}", file_content);
}
