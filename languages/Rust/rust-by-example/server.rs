use std::io::fs;
use std::io::fs::PathExtensions;
use std::io::net::pipe::UnixListener;
use std::io::{Acceptor,Listener};

use common::SOCKET_PATH;

mod common;


fn main() {
    let socket = Path::new(SOCKET_PATH);

    if socket.exists() {
        fs::unlink(&socket).unwrap();
    }

    let stream = match UnixListener::bind(&socket) {
        Err(_) => fail!("failed to bind socket"),
        Ok(stream) => stream,
    };

    println!("Server started, waiting for clients");
    for mut client in stream.listen().incoming() {
        println!("Client said: {}", client.read_to_string().unwrap());
    }
}
