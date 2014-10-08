use std::io::File;

fn main() {
    let path = Path::new("hello.txt");
    let display = path.display();

    let mut file = match File::open(&path) {
        Err(why) => fail!("coundn't open {}: {}", display, why.desc),
        Ok(file) => file,
    };

    match file.read_to_string() {
        Err(why) => fail!("couldn't read {}: {}", display, why.desc),
        Ok(string) => print!("{} contains:\n{}", display, string),
    }
}
