fn main() {
    print!("January has ");
    println!("{} days", 31i);
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");
    println!("{subject} {verb} {predicate}",
             predicate="over the lazy dog",
             subject="the quick brown fox",
             verb="jumps");
    
    println!("{} of {:t} people know binary, the other half don't", 1i, 2i);
}
