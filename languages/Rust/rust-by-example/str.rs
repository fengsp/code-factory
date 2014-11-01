fn main() {
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("Pangram: {}", pangram);

    println!("Words in reverse");
    for word in pangram.words().rev() {
        println!("> {}", word);
    }

    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    let mut string = String::new();
    for c in chars.into_iter() {
        string.push(c);
        string.push_str(", ");
    }

    let chars_to_trim: &[char] = [' ', ','];
    let trimmed_str: &str = string.as_slice().trim_chars(chars_to_trim);

    let alice = String::from_str("I like dogs");
    let bob: String = alice.replace("dog", "cat");

    println!("Alice says: {}", alice);
    println!("Bob says: {}", bob);
}
