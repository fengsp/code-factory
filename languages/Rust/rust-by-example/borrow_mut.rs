#[allow(dead_code)]
struct Book {
    author: &'static str,
    title: &'static str,
    year: uint,
}

fn borrow_book(book: &Book) {
    println!("I borrowed {} {} edition", book.title, book.year);
}

fn new_edition(book: &mut Book) {
    book.year = 2014;
}

fn main() {
    let geb = Book {
        author: "Douglas Hofstadter",
        title: "Gödel, Escher, Bach",
        year: 1979,
    };
    borrow_book(&geb);
    let mut mutable_geb = geb;
    new_edition(&mut mutable_geb);
    borrow_book(&mutable_geb);
}
