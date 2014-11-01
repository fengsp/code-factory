fn main() {
    let collected_iterator: Vec<int> = range(0i, 10).collect();
    println!("Collected range(0, 10) into: {}", collected_iterator);

    let mut xs = vec![1i, 2, 3];
    println!("Initial vector: {}", xs);

    println!("Push 4 into the vector")
    xs.push(4);
    println!("Vector: {}", xs);

    println!("Vector size: {}", xs.len());
    println!("Second element: {}", xs.get(1));
    println!("Pop last element: {}", xs.pop());

    println!("Fourth element: {}", xs.get(3));
}
