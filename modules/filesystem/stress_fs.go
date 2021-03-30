package files

import (
	"log"
	"os"
)

// creates a large truncated file
func create_truncated_file(fn string, size uint) {
	f, err := os.Create(fn)
	if err != nil {
		log.Fatal(err)
	}

	if err := f.Truncate(f, size); err != nil {
		log.Fatal(err)
	}

}

func create_file(fn string, size uint) {
	data := []byte(size)
	f, err := os.Create(fn)
	if err != nil {
		log.Fatal(err)
	}
	if err := f.Write(size); err != nil {
		log.Fatal(err)
	}

}
