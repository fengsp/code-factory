fn eat_box(boxed_int: Box<int>) {
    println!("destroying box that contains {}", boxed_int);
}

fn peep_inside_box(borrowed_box: &Box<int>) {
    println!("This box contains {}", borrowed_box);
}

fn main() {
    let boxed_int = box 5;
    peep_inside_box(&boxed_int);
    peep_inside_box(&boxed_int);
    {
        let _ref_to_int: &int = &*boxed_int;
    }
    eat_box(boxed_int);
}
