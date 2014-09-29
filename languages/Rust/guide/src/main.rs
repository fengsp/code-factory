use std::io;


fn main() {
    let x: int;
    let y = 5i;
    x = 100;

    println!("Hello world!");
    println!("The value of x is: {}", x);

    if y == 5i {
        println!("y is five!");
    } else {
        println!("y is not five :(");
    }

    let z = if y == 5i {
        10i
    } else {
        15i
    };

    print_number(z);
    print_sum(1, 2);
    println!("{}", add_one(100));

    let tuple = (1i, "hello");
    let tuple_two: (int, &str) = (1, "hello");
    let (a, b) = tuple;

    let c = (1i, 2i, 3i);
    let d = (2i, 3i, 4i);
    
    if c == d && a == 1 && b == "h" && tuple != tuple_two {
        println!("yes");
    } else {
        println!("no");
    }

    let (e, f) = next_two(5i);
    println!("e, f = {}, {}", e, f);

    let origin = Point { x: 0i, y: 0i };
    println!("The origin is at ({}, {})", origin.x, origin.y);

    let mut point = Point { x: 0i, y: 0i };
    point.x = 5;
    println!("The point is at ({}, {})", point.x, point.y);

    let black = Color(0, 0, 0);
    let d3_origin = D3Point(0, 0, 0);

    let length = Inches(10);
    let Inches(integer_length) = length;
    println!("length is {} inches", integer_length);

    let j = 5i;
    let h = 10i;
    let ordering = cmp(j, h);

    let m = Value(5);
    let n = Missing;

    match m {
        Value(n) => println!("m is {:d}", n),
        Missing  => println!("m is missing!"),
    }

    match n {
        Value(n) => println!("n is {:d}", n),
        Missing  => println!("n is missing!"),
    }

    let o = 5i;
    let r = match o {
        1 => println!("one"),
        2 => println!("two"),
        3 => println!("three"),
        4 => println!("four"),
        5 => println!("five"),
        _ => println!("something else"),
    };

    for u in range(0i, 10i) {
        println!("{:d}", u);
    }

    println!("hello");
    println!("{}", r);
    let s = print(10i);
    println!("{}", s);

    let mut w = 5u;
    let mut done = false;
    
    while !done {
        w += w - 3;
        println!("{}", w);
        if x % 5 == 0 { done = true; }
    }

    main2();
    main3()
}


fn print_number(x: int) {
    println!("number is: {}", x);
}


fn print_sum(x: int, y: int) {
    println!("sum is: {}", x + y);
}


fn add_one(x: int) -> int {
    x + 1
}


fn next_two(x: int) -> (int, int) {
    (x + 1i, x + 2i)
}


struct Point {
    x: int,
    y: int,
}


struct Color(int, int, int);
struct D3Point(int, int, int);
struct Inches(int);


enum Ordering {
    Less,
    Equal,
    Greater,
}


fn cmp(a: int, b: int) -> Ordering {
    if a < b { Less }
    else if a > b { Greater }
    else { Equal }
}


enum OptionalInt {
    Value(int),
    Missing,
}


fn print(value :int) {
    println!("{}", value)
}


fn main2() {
    let mut a = 5u;
    
    loop {
        a += a - 3;
        println!("{}", a);
        if a % 5 == 0 { break; }
    }

    for x in range(0i, 10i) {
        if x % 2 == 0 { continue; }
        println!("{:d}", x);
    }

    let string = "Hello there.";
    let mut b = "Hello".to_string();
    println!("{}", b);
    b.push_str(", world.");
    println!("{}", b);
    let mut s = "Hello".to_string();
    takes_slice(s.as_slice());

    compare("Hello".to_string());

    let mut nums = vec![1i, 2i, 3i];
    nums.push(4i);
    let slice = nums.as_slice();
    let array = [1i, 2i, 3i, 4i];

    for i in slice.iter() {
        println!("{}", i);
    }

    if array == slice {
        println!("true");
    }

    let names = ["Graydon", "Brian", "Niko"];
    println!("The second name is: {}", names[1]);
}


fn takes_slice(slice: &str) {
    println!("Got: {}", slice);
}


fn compare(string: String) {
    if string.as_slice() == "Hello" {
        println!("yes");
    }
}


fn main3() {
    println!("Type something!");
    let input = io::stdin().read_line().ok()
                                       .expect("Failed to read line");
    println!("{}", input);
}
