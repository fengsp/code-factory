fn main() {
    let mut a = [0; 11];
    let scores = [5, 3, 5, 2, 8];
    for score in scores.into_iter() {
        a[*score] = a[*score] + 1;
    }
    for i in 0..a.len() {
        for _ in 0..a[i] {
            println!("{}", i);
        }
    }
}
