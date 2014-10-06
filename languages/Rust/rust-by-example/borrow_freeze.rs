fn main() {
    let mut _integer = 5i;
    {
        let _ref_to_integer = &_integer;
    }
    _integer = 4;
}
