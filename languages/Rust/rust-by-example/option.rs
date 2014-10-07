fn checked_division(dividend: int, divisor: int) -> Option<int> {
    if divisor == 0 {
        None
    } else {
        Some(dividend / divisor)
    }
}

fn try_division(dividend: int, divisor: int) {
    match checked_division(dividend, divisor) {
        None => println!("{} / {} failed!", dividend, divisor),
        Some(quotient) => {
            println!("{} / {} = {}", dividend, divisor, quotient)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    let none: Option<int> = None;
    let _equivalent_none = None::<int>;

    let optional_float = Some(0f32);
    
    println!("{} unwraps to {}", optional_float, optional_float.unwrap());
    println!("{} unwraps to {}", none, none.unwrap());
}
