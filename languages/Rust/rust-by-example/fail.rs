fn division(dividend: int, divisor: int) -> int {
    if divisor == 0 {
        fail!("division by zero");
    } else {
        dividend / divisor
    }
}

fn main() {
    let _x = box 0i;
    division(3, 0);
    println!("This point won't be reached!");
}
