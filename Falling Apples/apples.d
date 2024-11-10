import std.stdio;
import std.array;
import std.conv;
import std.string;
import std.typecons;

Tuple!(char[][], int, int) readInput(string file) {
    auto f = File(file, "r");
    auto line = strip(f.readln);
    auto rowsCols = line.split;
    int rows = to!int(rowsCols[0]);
    int cols = to!int(rowsCols[1]);
    char[][] grid;
    foreach (_; 0 .. rows) {
        grid ~= f.readln.strip.dup;
    }
    f.close();
    return tuple(grid, rows, cols);
}

void simulateFallingApples(ref char[][] grid, int rows, int cols) {
    for (int col = 0; col < cols; col++) {
        int emptyRow = rows - 1;
        for (int row = rows - 1; row >= 0; row--) {
            if (grid[row][col] == 'a') {
                if (row != emptyRow) {
                    grid[emptyRow][col] = 'a';
                    grid[row][col] = '.';
                }
                emptyRow--;
            } else if (grid[row][col] == '#') {
                emptyRow = row - 1;
            }
        }
    }
}

void main() {
    auto result = readInput("apples.in");
    auto grid = result[0];
    int rows = result[1];
    int cols = result[2];

    simulateFallingApples(grid, rows, cols);

    foreach (row; grid) {
        writeln(cast(string) row);  // Cast char[] to string
    }
}