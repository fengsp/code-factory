use std::rc::Rc;

fn main() { 
    let x = 5i;
    let y = &x;
    assert_eq!(5i, *y);
    println!("Hello, world!")
    assert_eq!(6, add_one(&5));

    let mut m = 5i;
    let n = &mut m;

    let i = Rc::new(5i);
    let j = i.clone();

    let a = 1i;
    match a {
        1 | 2 => println!("one or two"),
        3 => println!("three"),
        _ => println!("anything"),
    }
    match a {
        1 .. 5 => println!("one through five"),
        _ => println!("anything"),
    }
    match a {
        a @ 1 .. 5 => println!("got {}", a),
        _ => println!("anything"),
    }

    enum OptionalInt {
        Value(int),
        Missing,
    }
    let b = Value(5i);
    match b {
        Value(..) => println!("Got an int!"),
        Missing => println!("No such luck."),
    }
    match b {
        Value(b) if b > 5 => println!("Got an int bigger than five!"),
        Value(..) => println!("Got an int!"),
        Missing => println!("No such luck."),
    }

    let c = &5i;
    match c {
        &c => println!("Got a value: {}", c),
    }
    match c {
        ref c => println!("Got a reference to {}", c),
    }

    let mut d = 5i;
    match d {
        ref mut d => println!("Got a mutable reference to {}", d),
    }

    struct Point {
        x: int,
        y: int,
    }

    let origin = Point { x: 0i, y: 0i };
    match origin {
        Point { x: x, y: y } => println!("({},{})", x, y),
    }
    match origin {
        Point { x: x, .. } => println!("x is {}", x),
    }

    struct Circle {
        x: f64,
        y: f64,
        radius: f64,
    }

    impl Circle {
        fn new(x: f64, y: f64, radius: f64) -> Circle {
            Circle {
                x: x,
                y: y,
                radius: radius,
            }
        }

        fn area(&self) -> f64 {
            std::f64::consts::PI * (self.radius * self.radius)
        }
    }

    let e = Circle { x: 0.0, y: 0.0, radius: 2.0 };
    let f = Circle::new(0.0, 0.0, 2.0);
    println!("{}", e.area());
}

fn add_one(x: &int) -> int { *x + 1 }
