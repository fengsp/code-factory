fn main() {
    for name in ["Peter", "Paul", "Mary"].iter() {
        println!("Hello {:s}!", *name);
    }
}
