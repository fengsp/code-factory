use std::io::net::pipe::UnixStream;
use std::os;

use common::SOCKET_PATH;

mod common;


fn main() {
    let args = os::args();
    let socket = Path::new(SOCKET_PATH);

    let message = match args.as_slice() {
        [_, ref message] => message.as_slice(),
        _ => fail!("wrong number of arguments"),
    };

    let mut stream = match UnixStream::connect(&socket) {
        Err(_) => fail!("server is not running"),
        Ok(stream) => stream,
    };

    match stream.write_str(message) {
        Err(_) => fail!("couldn't send message"),
        Ok(_) => {}
    }
}

    
