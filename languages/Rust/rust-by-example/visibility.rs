fn function() {
    println!("called `function()`");
}

mod my {
    pub fn function() {
        println!("called `my::function()`");
    }

    fn private_function() {
        println!("called `my::private_function()`");
    }

    pub fn indirect_access() {
        print!("called `my::indirect_access()`, that\n> ");
        private_function();
    }

    pub mod nested {
        pub fn function() {
            println!("called `my::nested::function()`");
        }
        
        #[allow(dead_code)]
        fn private_function() {
            println!("called `my::nested::private_function()`");
        }
    }

    mod inaccessible {
        #[allow(dead_code)]
        pub fn public_function() {
            println!("called `my::inaccessible::public_function()`");
        }
    }
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
