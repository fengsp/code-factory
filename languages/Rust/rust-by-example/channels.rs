use std::comm;

static NTASKS: uint = 3;

fn main() {
    let (tx, rx) : (Sender<uint>, Receiver<uint>) = comm::channel();

    for id in range(0, NTASKS) {
        let task_tx = tx.clone();
        spawn(proc() {
            task_tx.send(id);
            println!("task {} finished", id);
        });
    }

    let mut ids = Vec::with_capacity(NTASKS);
    for _ in range(0, NTASKS) {
        ids.push(rx.recv());
    }
    println!("{}", ids);
}
