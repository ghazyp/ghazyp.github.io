def read_input(file):
    with open(file, 'r') as file:
        rows, cols = map(int, file.readline().split())
        grid = [list(file.readline().strip()) for _ in range(rows)]
    return grid, rows, cols
        
def simulate_falling_apples(grid, rows, cols):
    for col in range(cols):
        # Start from the bottom and move upwards
        empty_row = rows - 1
        for row in range(rows - 1, -1, -1):
            if grid[row][col] == 'a':
                if row != empty_row:
                    grid[empty_row][col], grid[row][col] = grid[row][col], '.'
                empty_row -= 1
            elif grid[row][col] == '#':
                empty_row = row - 1
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    file = 'apples.in'
    grid, rows, cols = read_input(file)
    grid = simulate_falling_apples(grid, rows, cols)
    print_grid(grid)
