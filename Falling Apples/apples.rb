def read_input(file)
    file = File.open('apples.in', 'r')
    rows, cols = file.readline.split.map(&:to_i)
    grid = []
    rows.times do
      grid << file.readline.strip.chars
    end
    file.close
    return grid, rows, cols
end
  
def simulate_falling_apples(grid, rows, cols)
    cols.times do |col|
        # Start from the bottom and move upwards
        empty_row = rows - 1
        (rows - 1).downto(0) do |row|
            if grid[row][col] == 'a'
                if row != empty_row
                    grid[empty_row][col], grid[row][col] = grid[row][col], '.'
                end
                empty_row -= 1
            elsif grid[row][col] == '#'
                empty_row = row - 1
            end
        end    
    end
    grid
end

def print_grid(grid)
    grid.each do |row|
        puts row.join('')
    end
end
  
def main()
    file = 'apple.in'
    grid, rows, cols = read_input(file)
    grid = simulate_falling_apples(grid, rows, cols) 
    print_grid(grid)
end

main
  