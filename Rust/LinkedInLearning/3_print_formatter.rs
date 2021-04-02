fn main() {
    let a = 10.0;
    let b = 3.0;
    let c = b / a;
    println!("c is {:.3}", c); // Formats the output with just 3 decimal numbers
    println!("c is {:8.3}", c); // Gives some padding to the print, in this case 8 spaces
    println!("c is {:08.3}", c); // Gives some padding to the print with zeros ('0') 
}