# Solution to the Instruens Fabulam problem

def parse_input(input_lines):

    """Parses the input and returns a list of tables, where each table is a list of rows.
    The first row of each table contains alignment markers."""
    
    tables = []
    current_table = []
    
    for line in input_lines:
        if line.strip() == '*':  # End of input signal
            if current_table:
                tables.append(current_table)
            break
        elif set(line.strip()).issubset({'<', '=', '>'}):  # Alignment line containing only alignment markers
            if current_table:
                tables.append(current_table)
            current_table = [list(line.strip())]  # New table with alignment as first entry
        else:
            current_table.append(line.strip().split('&'))  # Split columns by '&'
    
    return tables

def calculate_widths(table):

    """Calculates the maximum width for each column in the table (including header and data rows)."""
    
    widths = [max(len(str(entry).strip()) for entry in column) for column in zip(*table)]
    return widths

def format_table(table):

    """Formats the table according to the specification.
    Aligns columns based on the alignment markers and calculates column widths."""
    
    alignments = table[0]  # First row contains alignment markers
    widths = calculate_widths(table[1:])  # Calculate widths excluding alignment row
    
    # Define alignment mappings: left (<), center (=), and right (>)
    align_map = {'<': '<', '=': '^', '>': '>'}

    # Format header and data rows based on alignments and calculated widths
    header_parts = []
    for text, align, width in zip(table[1], alignments, widths):
        formatted_text = "{:{align}{width}}".format(text.strip(), align=align_map[align], width=width)
        header_parts.append(formatted_text)
    header = '| ' + ' | '.join(header_parts) + ' |'
    
    # Modified divider with plus signs only at intersections and dashes elsewhere
    divider = '|' + '+'.join('-' * (width + 2) for width in widths) + '|'
    
    # Top border uses @ at the ends and dashes in between
    top_border = '@' + '-' * (len(divider) - 2) + '@'
    
    # Generate formatted rows (starting from the second data row)
    rows = []
    for row in table[2:]:
        row_data = []
        for text, align, width in zip(row, alignments, widths):
            row_data.append("{:{align}{width}}".format(text.strip(), align=align_map[align], width=width))
        rows.append("| " + " | ".join(row_data) + " |")

    
    # Return the formatted table as a full string with exact formatting
    full_table = [top_border, header, divider] + rows + [top_border]
    return '\n'.join(full_table)

def main():
    # Open the input file and read lines
    with open('fab.in', 'r') as file:
        input_lines = file.read().splitlines()
    
    # Parse input and format tables
    tables = parse_input(input_lines)
    
    # Print each table, but skip the newline after the last table
    for i, table in enumerate(tables):
        print(format_table(table))
        if i < len(tables) - 1:
            print()  # Only print a newline if it's not the last table
    
    # Open the output file for writing
    with open('fab.out', 'w') as output_file:
        for i, table in enumerate(tables):
            output_file.write(format_table(table))
            if i < len(tables) - 1:
                output_file.write('\n')  # Only write a newline if it's not the last table
                
if __name__ == '__main__':
    main()
