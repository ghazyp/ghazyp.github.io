package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	alphabet := "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
	results := []string{}

	// Open the file
	file, err := os.Open("rot.in")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Read input lines from the file
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "0" {
			break
		}

		// Split the line by the first space
		parts := strings.SplitN(line, " ", 2)
		if len(parts) < 2 {
			continue // Skip lines without a space
		}

		// Convert the rotation number to an integer
		n, err := strconv.Atoi(parts[0])
		if err != nil {
			continue // Skip invalid input
		}

		// Extract the string to be encoded
		plainText := parts[1]

		// Reverse the string
		reversed := reverseString(plainText)

		// Apply rotation and construct the result
		result := ""
		for _, char := range reversed {
			index := strings.IndexRune(alphabet, char)
			newIndex := (index + n) % len(alphabet)
			result += string(alphabet[newIndex])
		}

		results = append(results, result)
	}

	// Check for errors while reading the file
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Output all results, each on a new line
	for _, res := range results {
		fmt.Println(res)
	}
}

// Helper function to reverse a string
func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
