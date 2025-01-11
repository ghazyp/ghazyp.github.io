package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// ReadInput reads the input file and returns the grid, rows, and columns
func ReadInput(filename string) ([][]rune, int, int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, 0, 0, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	// Read the first line for rows and columns
	scanner.Scan()
	firstLine := scanner.Text()
	dimensions := strings.Fields(firstLine)
	rows, err := strconv.Atoi(dimensions[0])
	if err != nil {
		return nil, 0, 0, err
	}
	cols, err := strconv.Atoi(dimensions[1])
	if err != nil {
		return nil, 0, 0, err
	}

	// Read the grid
	grid := make([][]rune, rows)
	for i := 0; i < rows; i++ {
		scanner.Scan()
		grid[i] = []rune(scanner.Text())
	}

	return grid, rows, cols, nil
}

// SimulateFallingApples simulates the apples falling in the grid
func SimulateFallingApples(grid [][]rune, rows, cols int) [][]rune {
	for col := 0; col < cols; col++ {
		emptyRow := rows - 1
		for row := rows - 1; row >= 0; row-- {
			if grid[row][col] == 'a' {
				if row != emptyRow {
					grid[emptyRow][col] = 'a'
					grid[row][col] = '.'
				}
				emptyRow--
			} else if grid[row][col] == '#' {
				emptyRow = row - 1
			}
		}
	}
	return grid
}

// PrintGrid prints the grid
func PrintGrid(grid [][]rune) {
	for _, row := range grid {
		fmt.Println(string(row))
	}
}

func main() {
	filename := "apples.in"

	// Read input
	grid, rows, cols, err := ReadInput(filename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Simulate falling apples
	grid = SimulateFallingApples(grid, rows, cols)

	// Print the final grid
	PrintGrid(grid)
}
