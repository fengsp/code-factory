static LANGUAGE: &'static str = "Rust";
static THRESHOLD: int = 10;

fn is_big(n: int) -> bool {
    n > THRESHOLD
}

fn main() {
    let n = 16;

    println!("This is {}", LANGUAGE);
    println!("The threshold is {}", THRESHOLD);
    println!("{} is {}", n, if is_big(n) { "big" } else { "small" });

    {
        let _staitc_string: &'static str = "In read-only memory";
    }
}
