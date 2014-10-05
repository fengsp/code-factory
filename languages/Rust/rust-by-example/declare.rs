fn main() {
    let a_variable;

    {
        let x = 2i;
        a_variable = x * x;
    }

    println!("a variable: {}", a_variable);
}
