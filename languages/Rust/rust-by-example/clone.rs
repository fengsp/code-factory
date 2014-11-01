#[deriving(Show)]
struct Nil;

#[deriving(Clone, Show)]
struct Pair(Box<int>, Box<int>);

fn main() {
    let nil = Nil;
    let copied_nil = nil;

    println!("original: {}", nil);
    println!("copy: {}", copied_nil);

    let pair = Pair(box 1, box 2);
    println!("original: {}", pair);

    let moved_pair = pair;
    println!("copy: {}", moved_pair);
    
    let cloned_pair = moved_pair.clone();
    drop(moved_pair);
    println!("clone: {}", cloned_pair);
}
