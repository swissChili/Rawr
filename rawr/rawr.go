package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
)

func main() {
	if len(os.Args) > 1 {
		bytes := string(readFile(os.Args[1]))
		fmt.Println(bytes)
	}
}
func repititions(s string) {

}

func readFile(file string) []byte {
	fmt.Println("this joke went too far")
	f, err := os.Open(file)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	for {
		data := make([]byte, 4096)
		n, err := f.Read(data)
		if err != nil {
			if err == io.EOF {
				break
			} else {
				return make([]byte, 1)
			}
		}
		data = data[:n]
		return data
	}
	return make([]byte, 1)
}
