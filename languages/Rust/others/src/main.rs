use std::sync::Future;
use std::task;
use std::rand;

fn main() {
    let add_one = |x| { 1i + x };
    println!("The 5 plus 1 is {}.", add_one(5i));

    let x = 5i;
    let printer = || { println!("x is: {}", x); };
    printer();

    let p = proc() { x * x };
    println!("{}", p());

    fn twice(x: int, f: |int| -> int) -> int {
        f(x) + f(x)
    }

    let square = |x: int| { x * x };
    twice(5i, square);

    let mut r = range(0i, 10i);
    loop {
        match r.next() {
            Some(x) => {
                println!("{}", x);
            }
            None => { break }
        }
    }

    let mut range2 = range(1i, 100i);
    let sum = range2.fold(0i, |sum :int, x :int| sum + x);
    let mapped = range(1i, 100i).map(|x| x + 1i);

    let u: Option<int> = Some(5i);
    let v: Option<f64> = Some(5.0f64);

    let i: Result<f64, String> = Ok(2.3f64);
    let y: Result<f64, String> = Err("There was an error.".to_string());

    fn inverse(x: f64) -> Result<f64, String> {
        if x == 0.0f64 { return Err("x cannot be zero!".to_string()); }
        Ok(1.0f64 / x)
    }

    let result = inverse(25.0f64);
    match result {
        Ok(x) => println!("The inverse of 25 is {}", x),
        Err(msg) => println!("Error: {}", msg),
    }

    struct Circle {
        x: f64,
        y: f64,
        radius: f64,
    }

    trait HasArea {
        fn area(&self) -> f64;
    }

    impl HasArea for Circle {
        fn area(&self) -> f64 {
            std::f64::consts::PI * (self.radius * self.radius)
        }
    }

    fn print_area<T: HasArea>(shape: T) {
        println!("This shape has an area of {}", shape.area());
    }

    spawn(proc() {
        println!("Hello from a task!");
    });

    let (tx, rx) = channel();
    spawn(proc() {
        tx.send("Hello from a task!".to_string());
    });
    let message = rx.recv();
    println!("{}", message);

    let (tx1, rx1) = channel();
    let (tx2, rx2) = channel();
    spawn(proc() {
        tx1.send("Hello from a task!".to_string());
        let message = rx2.recv();
        println!("{}", message);
    });
    let message = rx1.recv();
    println!("{}", message);
    tx2.send("Goodbye from main!".to_string());

    let mut delayed_value = Future::spawn(proc() {
        12345i
    });
    println!("value = {}", delayed_value.get());

    let z = task::try(proc() {
        if rand::random() {
            println!("OK");
        } else {
            fail!("oops!");
        }
    });
}
