fn main() {
    let ascii = 'a';
    println!("{}", ascii.is_ascii());
    println!("{}", ascii.to_ascii_uppercase());
}

// ! Tests below

// Checks if within the ASCII range.
#[test]
fn is_charachter_ascii() {
    let ascii = 'a';
    let utf8 = '❤';

    assert_eq!(true, ascii.is_ascii());
    assert_eq!(false, utf8.is_ascii());
}

// Makes a copy of the string in ASCII upper case.
// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z', but non-ASCII letters are unchanged.
#[test]
fn uppercase_ascii() {
    let ascii = 'a';
    let utf8 = '❤';

    assert_eq!('A', ascii.to_ascii_uppercase());
    assert_eq!('❤', utf8.to_ascii_uppercase());
}

// Makes a copy of the string in ASCII lower case.
// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z', but non-ASCII letters are unchanged.
#[test]
fn lowercase_ascii() {
    let ascii = 'A';
    let ascii_2 = 'B';
    let utf8 = '❤';

    assert_eq!('a', ascii.to_ascii_lowercase());
    assert_eq!('b', ascii_2.to_ascii_lowercase());
    assert_eq!('❤', utf8.to_ascii_lowercase());
}

// Checks that two strings are an ASCII case-insensitive match.
// Same as to_ascii_lowercase(a) == to_ascii_lowercase(b), but without allocating and copying temporary strings.
#[test]
fn ignore_ascii_case() {
    let ascii1 = 'A';
    let ascii2 = 'a';
    let ascii3 = 'A';
    let ascii4 = 'z';

    assert_eq!(true, ascii1.eq_ignore_ascii_case(&ascii2));
    assert_eq!(true, ascii1.eq_ignore_ascii_case(&ascii3));
    assert_eq!(false, ascii1.eq_ignore_ascii_case(&ascii4));
}

// Converts this type to its ASCII upper case equivalent in-place.
#[test]
fn make_ascii_uppercase() {
    let mut ascii = 'a';

    ascii.make_ascii_uppercase();

    assert_eq!('A', ascii);
}

// Converts this type to its ASCII lower case equivalent in-place.
#[test]
fn make_ascii_lowercase() {
    let mut ascii = 'A';

    ascii.make_ascii_lowercase();

    assert_eq!('a', ascii);
}
