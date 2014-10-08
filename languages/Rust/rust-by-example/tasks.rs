static NTASKS: int = 10;

fn main() {
    for i in range(0, NTASKS) {
        spawn(proc() {
            println!("this is task number {}", i)
        });
    }
}
