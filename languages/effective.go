/*
Package main
*/
package main

import (
	"flag"
	"fmt"
	"html/template"
	"io"
	"log"
	"net/http"
	"os"
	"sort"
)

const (
	YSize = 8
	XSize = 8
)

type T struct {
	name  string // name of the object
	value int    // its value
}

type St struct {
	value string
}

type Stringer interface {
	String() string
}

type Handler interface {
	ServeHTTP(http.ResponseWriter, *http.Request)
}

type Counter struct {
	n int
}

func (ctr *Counter) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	ctr.n++
	fmt.Fprintf(w, "counter = %d\n", ctr.n)
}

type Transform [3][3]float64
type LinesOfText [][]byte
type Sequence []int

var text = LinesOfText{
	[]byte("Now is the time"),
	[]byte("for all good gophers"),
	[]byte("to bring some fun to the party."),
}

var timeZone = map[string]int{
	"UTC": 0 * 60 * 60,
	"EST": -5 * 60 * 60,
	"CST": -6 * 60 * 60,
	"MST": -7 * 60 * 60,
	"PST": -8 * 60 * 60,
}

func (t *T) Name() string {
	return t.name
}

func (t *T) SetName(name string) {
	t.name = name
}

func unhex(c byte) byte {
	switch {
	case '0' <= c && c <= '9':
		return c - '0'
	case 'a' <= c && c <= 'f':
		return c - 'a' + 10
	case 'A' <= c && c <= 'F':
		return c - 'A' + 10
	}
	return 0
}

func shouldEscape(c byte) bool {
	switch c {
	case ' ', '?', '&', '=', '#', '+', '%':
		return true
	}
	return false
}

// Compare returns an integer comparing the two byte slices,
// lexicographically.
// The result will be 0 if a == b, -1 if a < b, and +1 if a > b
func Compare(a, b []byte) int {
	for i := 0; i < len(a) && i < len(b); i++ {
		switch {
		case a[i] > b[i]:
			return 1
		case a[i] < b[i]:
			return -1
		}
	}
	switch {
	case len(a) > len(b):
		return 1
	case len(a) < len(b):
		return -1
	}
	return 0
}

/*
func ReadFull(r Reader, buf []byte) (n int, err error) {
    for len(buf) > 0 && err == nil {
        var nr int
        nr, err = r.Read(buf)
        n += nr
        buf = buf[nr:]
    }
    return
}*/

func deferTest() {
	fmt.Println("deferred")
}

// Contents returns the file's contents as a string.
func Contents(filename string) (string, error) {
	f, err := os.Open(filename)
	if err != nil {
		return "", err
	}
	defer f.Close()

	var result []byte
	buf := make([]byte, 100)
	for {
		n, err := f.Read(buf[0:])
		result = append(result, buf[0:n]...)
		if err != nil {
			if err == io.EOF {
				break
			}
			return "", err
		}
	}
	return string(result), nil
}

func sliceModify(sl []string) {
	sl[0] = "valueModified"
}

func structModify(st *St) {
	st.value = "valueModified"
}

func Println(v ...interface{}) {
	fmt.Println(2, fmt.Sprint(v...))
}

func (s Sequence) Len() int {
	return len(s)
}

func (s Sequence) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s Sequence) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s Sequence) String() string {
	sort.Sort(s)
	str := "["
	for i, elem := range s {
		if i > 0 {
			str += " "
		}
		str += fmt.Sprint(elem)
	}
	return str + "]"
}

type PathError struct {
	Op   string
	Path string
	Err  error
}

func (e *PathError) Error() string {
	return e.Op + " " + e.Path + ": " + e.Err.Error()
}

var addr = flag.String("addr", ":1718", "http service address")
var templ = template.Must(template.New("qr").Parse(templateStr))

const templateStr = `
<html>
<head>
<title>QR Link Generator</title>
</head>
<body>
{{if .}}
<img src="http://chart.apis.google.com/chart?chs=300x300&cht=qr&choe=UTF-8&chl={{.}}" />
<br>
{{.}}
<br>
<br>
{{end}}
<form action="/" name=f method="GET"><input maxLength=1024 size=70
name=s value="" title="Text to QR Encode"><input type=submit
value="Show QR" name=qr>
</form>
</body>
</html>
`

func QR(w http.ResponseWriter, req *http.Request) {
	templ.Execute(w, req.FormValue("s"))
}

func main() {
	fmt.Println("Effective go")
	t := &T{}
	t.SetName("fsp")
	fmt.Println(t.name)
	fmt.Println(t.value)
	fmt.Println(t.Name())
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
	m := map[string]string{"key": "value", "key2": "value2"}
	for key := range m {
		fmt.Println(key)
	}
	for pos, char := range "世界很美\x80呀" {
		fmt.Printf("character %#U starts at byte position %d\n", char, pos)
	}
	var b byte
	b = 'a'
	fmt.Println(unhex('A'))
	fmt.Println('a' - 'b')
	fmt.Println(b)
	fmt.Println(Compare([]byte{'a', 'b'}, []byte{'a'}))

	defer deferTest()

	var i interface{}
	i = 10
	switch i := i.(type) {
	default:
		fmt.Printf("unexpected type %T", i)
	case bool:
		fmt.Printf("boolean %t\n", i)
	case int:
		fmt.Printf("integer %d\n", i)
	case *bool:
		fmt.Printf("pointer to boolean %t\n", *i)
	case *int:
		fmt.Printf("pointer to integer %d\n", *i)
	}

	sl := []string{"value1", "value2"}
	sliceModify(sl)
	fmt.Println(sl)

	st := St{value: "value"}
	structModify(&st)
	fmt.Println(st)

	sl2 := []string{}
	sl3 := make([]string, 10)
	fmt.Println(sl2)
	fmt.Println(sl3)

	picture := make([][]uint8, YSize)
	for i := range picture {
		picture[i] = make([]uint8, XSize)
	}

	delete(timeZone, "PDT")

	fmt.Printf("Hello %d\n", 23)
	fmt.Fprint(os.Stdout, "Hello ", 23, "\n")
	fmt.Println("Hello", 23)
	fmt.Println(fmt.Sprint("Hello ", 23))

	Println(3, "wo")

	var value interface{}
	switch str := value.(type) {
	case string:
		fmt.Println(str)
	case Stringer:
		fmt.Println(str.String())
	}

	value = 10
	str, ok := value.(string)
	if ok {
		fmt.Printf("string value is: %q\n", str)
	} else {
		fmt.Printf("value is not a string\n")
	}

	flag.Parse()
	http.Handle("/", http.HandlerFunc(QR))
	err := http.ListenAndServe(*addr, nil)
	if err != nil {
		log.Fatal("ListenAndServe:", err)
	}
}
