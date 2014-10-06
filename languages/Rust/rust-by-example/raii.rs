fn create_box() {
    let _function_box = box 3i;
}

fn main() {
    let _boxed_int = box 5i;

    {
        let _short_lived_box = box 4i;
    }

    for _ in range(0u, 1_000) {
        create_box();
    }
}
