fn main() {
    let mut x = 0b1111_0101;
    println!("x is {}", x);
    println!("x is {:08b}", x);

    x = !x; // NOT
    println!("x is {:08b}", x);

    x = x & 0b1111_0101; // AND
    println!("x is {:08b}", x);

    x = x | 0b1111_0101; // OR
    println!("x is {:08b}", x);

    x = x ^ 0b1111_0101; // XOR
    println!("x is {:08b}", x);

    // SHIFT
    x = x << 4;
    println!("x is {:08b}", x);
    
    x = x >> 2;
    println!("x is {:08b}", x);
}