fn main() {
    let number: int = 13;
    println!("Tell me about {}", number);

    match number {
        1 => println!("One!"),
        2 | 3 | 5 | 7 | 11 => println!("This is a prime"),
        13..19 => println!("A teen"),
        _ => println!("Ain't special"),
    }

    let boolean = true;
    let binary: int = match boolean {
        false => 0,
        true => 1,
    };
    println!("{} -> {}", boolean, binary);
}
