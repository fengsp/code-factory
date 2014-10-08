#[deriving(PartialEq, PartialOrd)]
struct Centimeters(f64);

#[deriving(Show)]
struct Inches(int);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;
        Centimeters(inches as f64 * 2.54)
    }
}

struct Seconds(int);

fn main() {
    let _one_second = Seconds(1);
    let foot = Inches(12);
    println!("One foot ==- {}", foot);
    let meter = Centimeters(100.0);
    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };
    println!("one foot is {} than one meter", cmp);
}
