fn is_divisible_by(lhs: uint, rhs: uint) -> bool {
    if rhs == 0 {
        return false;
    }
    lhs % rhs == 0
}

fn fizzbuzz(n: uint) -> () {
    if is_divisible_by(n, 15) {
        println!("fizzbuzz");
    } else if is_divisible_by(n, 3) {
        println!("fizz");
    } else if is_divisible_by(n, 5) {
        println!("buzz");
    } else {
        println!("{}", n);
    }
}

fn fizzbuzz_to(n: uint) {
    for n in range(1, n + 1) {
        fizzbuzz(n);
    }
}

fn main() {
    fizzbuzz_to(100);
}
