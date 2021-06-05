mod something;
// the content of the module was here

use crate::something::a::*;
use crate::something::b::*;

fn main() {
    let first = A { a: 42 };
    let second = B { b: 52 };
    println!("A -> {}, B -> {}", first.a, second.b);
}
