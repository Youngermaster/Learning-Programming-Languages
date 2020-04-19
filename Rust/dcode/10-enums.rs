enum Direction {
    Up,
    Down,
    Left,
    Right
}

fn main() {
    let player_direction:Direction = Direction::Up;
    matches! player_direction {
        Direction::Up => println!("Up"),
        Direction::Down => println!("Down"),
        Direction::Right => println!("Right"),
        Direction::Left => println!("Left"),
    }
}