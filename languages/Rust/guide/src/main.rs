fn main() {
    let x: int;
    let y = 5i;
    x = 100;

    println!("Hello world!");
    println!("The value of x is: {}", x);

    if y == 5i {
        println!("y is five!");
    } else {
        println!("y is not five :(");
    }

    let z = if y == 5i {
        10i
    } else {
        15i
    };

    print_number(z);
    print_sum(1, 2);
    println!("{}", add_one(100));
}


fn print_number(x: int) {
    println!("number is: {}", x);
}


fn print_sum(x: int, y: int) {
    println!("sum is: {}", x + y);
}


fn add_one(x: int) -> int {
    x + 1
}
