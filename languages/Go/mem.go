package main

import (
	"fmt"
	"sync"
)

var str string
var w sync.WaitGroup
var c = make(chan int, 10)

// var c2 = make(chan int)
var l sync.Mutex
var once sync.Once

func f() {
	print(str)
	w.Done()
}

func f2() {
	str = "hello, again\n"
	close(c)
}

func f3() {
	str = "hello, over again\n"
	l.Unlock()
}

func setup() {
	str = "hello, once\n"
}

func doprint() {
	once.Do(setup)
	print(str)
	w.Done()
}

func main() {
	fmt.Println("golang.org/ref/mem")
	str = "hello, world\n"
	w.Add(1)
	go f()
	w.Wait()

	go f2()
	<-c
	print(str)

	l.Lock()
	go f3()
	l.Lock()
	print(str)

	w.Add(2)
	go doprint()
	go doprint()
	w.Wait()
}
