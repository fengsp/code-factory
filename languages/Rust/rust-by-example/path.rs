use std::io::fs::PathExtensions;

fn main() {
    let path = Path::new(".");

    let display = path.display();

    if path.exists() {
        println!("{} exists", display);
    }

    if path.is_file() {
        println!("{} is a directory", display);
    }

    let stat = match path.stat() {
        Err(why) => fail!("{}", why.desc),
        Ok(stat) => stat,
    };

    println!("{} size is {} bytes", display, stat.size);

    let new_path = path.join("a").join("b");
    match new_path.as_str() {
        None => fail!("new path is not a valid UTF-8 sequence"),
        Some(s) => println!("new path is {}", s),
    }
}
