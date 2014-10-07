trait Animal {
    fn new(name: &'static str) -> Self;

    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

struct Dog { name: &'static str }

impl Dog {
    fn wag_tail(&self) {
        println!("{} wags tail", self.name);
    }
}

impl Animal for Dog {
    fn new(name: &'static str) -> Dog {
        Dog { name: name }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        "woof!"
    }

    fn talk(&self) {
        self.wag_tail();

        println!("{} says {}", self.name, self.noise());
    }
}

struct Sheep { naked: bool, name: &'static str }

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            // Implementor methods can use the implementor's trait methods
            println!("{} is already naked!", self.name());
        } else {
            println!("{} gets a haircut", self.name);

            self.talk();
            self.naked = true;
        }
    }
}

impl Animal for Sheep {
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaah"
        } else {
            "baaaaaaaaaaaah"
        }
    }
}

fn main() {
    let mut dolly: Sheep = Animal::new("Dolly");
    let spike: Dog = Animal::new("Spike");

    dolly.shear();

    spike.talk();
    dolly.talk();
}
