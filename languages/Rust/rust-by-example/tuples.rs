fn reverse(pair: (int, bool)) -> (bool, int) {
    let (integer, boolean) = pair;

    (boolean, integer)
}

fn main() {
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    println!("long tuple first value: {}", long_tuple.val0());
    println!("long tuple second value: {}", long_tuple.val1());

    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);
    
    println!("tuple of tuples: {}", tuple_of_tuples);

    let pair = (1, true);
    println!("pair is {}", pair);
    println!("the reversed pair is {}", reverse(pair));

    println!("one element tuple: {}", (5u,));
    println!("just an integer: {}", (5u));
}
