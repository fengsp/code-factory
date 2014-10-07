enum Node {
    Cons(uint, Box<Node>),
    Nil,
}

impl Node {
    fn new() -> Node {
        Nil
    }

    fn append(self, elem: uint) -> Node {
        Cons(elem, box self)
    }

    fn len(&self) -> uint {
        match *self {
            Cons(_, ref tail) => 1 + tail.len(),
            Nil => 0
        }
    }

    fn stringify(&self) -> String {
        match *self {
            Cons(head, ref tail) => {
                format!("{}, [ ] -> {}", head, tail.stringify())
            },
            Nil => {
                format!("Nil")
            },
        }
    }
}

fn main() {
    let mut list = Node::new();

    list = list.append(1);
    list = list.append(2);
    list = list.append(3);

    println!("linked list has length: {}", list.len());
    println!("{}", list.stringify());
}
