fn main() {
    let x = 10;
    let xr = &x;

    let mut y = 12;

    {
        let mut_y = &mut y;

        *mut_y += 1;
    }

    println!("x is {}", x);
    println!("x is {}", xr);
    println!("y is {}", y);
}
