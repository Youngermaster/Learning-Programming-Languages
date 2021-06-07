fn main() {
    let mut x = 10;
    {
        let x = 15;
    }

    let x = "X is a String";
    println!("X: {}", x);
    
    let x = true;

    println!("X: {}", x);

}