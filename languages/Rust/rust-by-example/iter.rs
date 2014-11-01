use std::mem;

struct Fibonacci {
    curr: uint,
    next: uint,
}

impl Iterator<uint> for Fibonacci {
    fn next(&mut self) -> Option<uint> {
        let new_next = self.curr + self.next;
        let new_curr = mem::replace(&mut self.next, new_next);

        Some(mem::replace(&mut self.curr, new_curr))
    }
}

fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 1, next: 1 }
}

fn main() {
    let mut sequence = range(0u, 3);
    println!("Four consecutive `next` calls on range(0, 2)")
    println!("> {}", sequence.next());
    println!("> {}", sequence.next());
    println!("> {}", sequence.next());
    println!("> {}", sequence.next());

    println!("Iterate over range(0, 3) using for");
    for i in range(0u, 3) {
        println!("> {}", i);
    }

    println!("The first four terms of the Fibonacci sequence are: ");
    for i in fibonacci().take(4) {
        println!("> {}", i);
    }

    println!("The next four terms of the Fibonacci sequence are: ");
    for i in fibonacci().skip(4).take(4) {
        println!("> {}", i);
    }

    let array = [1u, 3, 3, 7];
    println!("Iterate the following array {}", array.as_slice());
    for i in array.iter() {
        println!("> {}", i);
    }
}
