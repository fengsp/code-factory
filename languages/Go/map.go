package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex
var n = map[string]Vertex{
	"Bell Labs": {40.68433, -74.399},
	"Google":    {37.42202, -122.084},
}

func main() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -23.333,
	}
	fmt.Println(m["Bell Labs"])
	for name, loca := range n {
		fmt.Println(name + ": ")
		fmt.Println(loca)
	}
}
