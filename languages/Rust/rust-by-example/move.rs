fn destroy_box(c: Box<int>) {
    println!("destroying a box that contains {}", c);
}

fn main() {
    let x = 5u;
    let y = x;
    println!("x is {}, and y is {}", x, y);

    let a = box 5;
    println!("a contains: {}", a);
    let b = a;
    destroy_box(b);
}
    
