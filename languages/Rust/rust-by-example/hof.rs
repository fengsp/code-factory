extern crate num;

use std::iter::AdditiveIterator;
use std::iter;

fn main() {
    println!("Find the sum of all the squared odd numbers under 1000");
    let upper = 1000u;

    let mut acc = 0;
    for n in iter::count(0u, 1) {
        let n_squared = n * n;
        if n_squared >= upper {
            break;
        } else if is_odd(n_squared) {
            acc += n_squared;
        }
    }
    println!("imperative style: {}", acc);

    let sum_of_squared_odd_numbers =
        iter::count(0u, 1).
        map(|n| n * n).
        take_while(|&n| n < upper).
        filter(|n| is_odd(*n)).
        sum();
    println!("functional style: {}", sum_of_squared_odd_numbers);
}

fn is_odd(n: uint) -> bool {
    if n % 2 == 1 {
        true
    } else {
        false
    }
}
