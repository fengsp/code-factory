struct Point { x: int, y: int }

fn main() {
    let point = Point { x: 0, y: 0 };

    let _copy_of_x = {
        let Point { x: ref ref_to_x, y: _ } = point;
        *ref_to_x
    };

    let mut mutable_point = point;

    {
        let Point { x:_, y: ref mut mut_ref_to_y } = mutable_point;
        *mut_ref_to_y = 1;
    }

    println!("point is ({}, {})", point.x, point.y);
    println!("mutable_point is ({}, {})", mutable_point.x, mutable_point.y);

    let mut tuple = (box 5u, 3u);

    {
        let (box ref mut i, _) = tuple;
        *i = 3;
    }

    println!("tuple is {}", tuple);
}
