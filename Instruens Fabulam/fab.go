package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func parseInput(inputLines []string) [][][]string {
	tables := [][][]string{}
	currentTable := [][]string{}

	for _, line := range inputLines {
		line = strings.TrimSpace(line)
		if line == "*" {
			if len(currentTable) > 0 {
				tables = append(tables, currentTable)
			}
			break
		} else if isAlignmentLine(line) {
			if len(currentTable) > 0 {
				tables = append(tables, currentTable)
			}
			currentTable = [][]string{strings.Split(line, "")}
		} else {
			cells := strings.Split(line, "&")
			for i := range cells {
				cells[i] = strings.TrimSpace(cells[i])
			}
			currentTable = append(currentTable, cells)
		}
	}

	return tables
}

func isAlignmentLine(line string) bool {
	for _, char := range line {
		if char != '<' && char != '=' && char != '>' {
			return false
		}
	}
	return true
}

func calculateWidths(table [][]string) []int {
	widths := make([]int, len(table[0]))
	for i := range widths {
		maxWidth := 0
		for _, row := range table[1:] {
			if len(row[i]) > maxWidth {
				maxWidth = len(row[i])
			}
		}
		widths[i] = maxWidth
	}
	return widths
}

func formatTable(table [][]string) []string {
	alignments := table[0]
	widths := calculateWidths(table)
	formattedRows := []string{}

	for _, row := range table[1:] {
		formattedCells := []string{}
		for i, cell := range row {
			width := widths[i]
			var formattedCell string

			switch alignments[i] {
			case "<":
				formattedCell = fmt.Sprintf("%-*s", width, cell)
			case "=":
				padding := (width - len(cell)) / 2
				formattedCell = fmt.Sprintf("%*s%s%*s", padding, "", cell, width-padding-len(cell), "")
			case ">":
				formattedCell = fmt.Sprintf("%*s", width, cell)
			}
			formattedCells = append(formattedCells, formattedCell)
		}
		formattedRow := "| " + strings.Join(formattedCells, " | ") + " |"
		formattedRows = append(formattedRows, formattedRow)
	}

	topBorder := "@" + strings.Repeat("-", len(formattedRows[0])-2) + "@"
	divider := "|" + strings.Join(makeDivider(widths), "+") + "|"

	formattedTable := []string{topBorder, formattedRows[0], divider}
	formattedTable = append(formattedTable, formattedRows[1:]...)
	formattedTable = append(formattedTable, topBorder)
	return formattedTable
}

func makeDivider(widths []int) []string {
	dividers := []string{}
	for _, width := range widths {
		dividers = append(dividers, strings.Repeat("-", width+2))
	}
	return dividers
}

func main() {
	file, err := os.Open("fab.in")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var inputLines []string
	for scanner.Scan() {
		inputLines = append(inputLines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	outputFile, err := os.Create("fab.out")
	if err != nil {
		fmt.Println("Error creating output file:", err)
		return
	}
	defer outputFile.Close()

	writer := bufio.NewWriter(outputFile)
	defer writer.Flush()

	tables := parseInput(inputLines)
	for i, table := range tables {
		formattedTable := formatTable(table)
		for j, line := range formattedTable {
			if j > 0 || i > 0 {
				fmt.Fprintln(writer) // Add newline only between tables
			}
			fmt.Fprint(writer, line) // Prevent extra trailing newline
		}
	}
}
