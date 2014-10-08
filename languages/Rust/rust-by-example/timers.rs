use std::io::Timer;
use std::io::timer;
use std::time::duration::Duration;
use std::iter;

fn main() {
    let interval = Duration::milliseconds(1000);
    let mut timer = Timer::new().unwrap();

    let oneshot: Receiver<()> = timer.oneshot(interval);
    println!("Wait {} ms...", interval.num_milliseconds());

    oneshot.recv();
    println!("Done");

    println!("Sleep for {} ms...", interval.num_milliseconds());

    timer::sleep(interval);

    println!("Done");

    let metronome: Receiver<()> = timer.periodic(interval);

    println!("Countdown");
    for i in iter::range_step(5i, 0, -1) {
        metronome.recv();

        println!("{}", i);
    }
    metronome.recv();
    println!("Ignition!");
}
