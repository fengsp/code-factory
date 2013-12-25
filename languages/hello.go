package main

import (
    "fmt"
    "time"
)

func main() {
    go say("Let's go!\n", 3*time.Second)
    go say("ho!\n", 2*time.Second)
    go say("hey!\n", 1*time.Second)
    time.Sleep(4*time.Second)
}

func say(text string, delay time.Duration) {
    time.Sleep(delay)
    fmt.Print(text)
}
