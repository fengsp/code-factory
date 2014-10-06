fn main() {
    let immutable_box = box 5u;
    println!("immutable_box contains {}", immutable_box);

    let mut mutable_box = immutable_box;
    println!("mutable_box contained {}", mutable_box);
    
    *mutable_box = 4;
    println!("mutable_box contained {}", mutable_box);
}
