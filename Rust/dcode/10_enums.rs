enum Direction {
    Up,
    Down,
    Left,
    Right
}

fn main() {
    let player_direction:Direction = Direction::Up;
    match player_direction {
        Direction::Up => println!("We are heading Up"),
        Direction::Down => println!("We are going all the way Down"),
        Direction::Right => println!("Moving towards the Right"),
        Direction::Left => println!("Left is right"),
    }
}