# Solution to the Instruens Fabulam problem

def parse_input(input_lines):
    """Parses the input and returns a list of tables, where each table is a list of rows."""
    tables = []
    current_table = []
    for line in input_lines:
        if line.strip() == '*':  # End of input signal
            if current_table:
                tables.append(current_table)
            break
        elif set(line.strip()).issubset({'<', '=', '>'}):  # Alignment line
            if current_table:
                tables.append(current_table)
            current_table = [list(line.strip())]  # Start new table
        else:
            current_table.append([cell.strip() for cell in line.split('&')])
    return tables

def calculate_widths(table):
    """Calculates maximum width for each column in the table."""
    return [max(len(cell) for cell in column) for column in zip(*table)]

def format_table(table):
    """Formats the table with given alignments and widths."""
    alignments = table[0]
    widths = calculate_widths(table[1:])
    align_map = {'<': '<', '=': '^', '>': '>'}

    formatted_rows = []
    for row in table[1:]:
        formatted_row = "| " + " | ".join(f"{cell:{align_map[align]}{width}}" for cell, align, width in zip(row, alignments, widths)) + " |"
        formatted_rows.append(formatted_row)

    top_border = "@" + "-" * (len(formatted_rows[0]) - 2) + "@"
    divider = "|" + "+".join("-" * (width + 2) for width in widths) + "|"
    return [top_border] + [formatted_rows[0], divider] + formatted_rows[1:] + [top_border]

def main():
    with open('fab.in', 'r') as file:
        input_lines = file.read().splitlines()
    
    tables = parse_input(input_lines)
    formatted_tables = [format_table(table) for table in tables]
    
    with open('fab.out', 'w') as output_file:
        for i, formatted_table in enumerate(formatted_tables):
            table_str = "\n".join(formatted_table)
            print(table_str)
            output_file.write(table_str)
            if i < len(formatted_tables) - 1:
                print()
                output_file.write('\n')

if __name__ == '__main__':
    main()


    
