fn main() {
    let long_lived_variable = 1i;
    
    {
        let short_lived_variable = 2i;
        println!("innder short: {}", short_lived_variable);

        let long_lived_variable = 5_f32;
        println!("inner long: {}", long_lived_variable);
    }

    println!("outer long: {}", long_lived_variable);
}
